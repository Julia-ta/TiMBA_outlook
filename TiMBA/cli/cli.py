from pathlib import Path
import click
import os
import datetime as dt
from TiMBA.main_runner.main_runner import main
from TiMBA.data_management.ParameterCollector import ParameterCollector
from TiMBA.data_management.Load_Data import load_data
from TiMBA.parameters import INPUT_WORLD_PATH
from TiMBA.parameters.paths import OUTPUT_DIR, ADDINFOPTHTOOLBOX 
import warnings
from Toolbox.toolbox import timba_dashboard, validation_dashboard
warnings.simplefilter(action='ignore', category=FutureWarning)
from TiMBA.user_io.default_parameters import (default_year, default_max_period, default_calc_product_price,
                                              default_calc_world_price, default_transportation_impexp_factor, default_MB,
                                              global_material_balance, serialization_flag, constants,
                                              dynamization_activated, cleaned_opt_quantity, capped_prices,
                                              verbose_optimization_logger, verbose_calculation_logger,
                                              read_additional_information_file)

@click.group()
def cli():
    pass

@click.command()
@click.option('-Y', '--year', default=default_year, 
              show_default=True, required=True, type=int, 
              help="Starting year.")
@click.option('-MP', '--max_period', 'max_period', default=default_max_period, 
              show_default=True, required=True, type=int, 
              help="Maximum amount of periods to forecast.")
@click.option('-PP', '--calc_product_price', "calc_product_price", default=default_calc_product_price,
              show_default=True, required=True, type=str,
              help="Flag to compute product prices as shadow or calculated prices. Choose shadow_PP for shadow prices "
                   "and calculated_PP for calculated prices. (Only shadow prices were validated extensively)")

@click.option('-WP', '--calc_world_price', "calc_world_price", default=default_calc_world_price, 
              show_default=True, required=True, type=str,
              help="Flag to compute world prices as shadow, constant or average prices. Choose shadow_WP for shadow "
                   "prices and constant_WP for constant prices, and average_WP for average prices."
                   "(Only shadow prices were validated extensively)")

@click.option('-MB', '--material_balance', "material_balance", default=default_MB, 
              show_default=True, required=True, type=str,
              help="Flag to specify the adopted material balance. Choose C_specific_MB for commodity specific material"
                   "balance, RC_specific_MB for region and commodity specific material balance, RCG_specific_MB for "
                   "region and commodity group specific material balance.")
@click.option('-GMB', '--global_material_balance', 'global_material_balance', default=global_material_balance,
              show_default=True, required=False, type=bool,
              help='Flag to activate global material balance balancing all wood flows globally')
@click.option('-TF', '--trans_imp_exp_factor', 'transportation_impexp_factor', 
              default=default_transportation_impexp_factor, 
              show_default=True, required=True, type=float,
              help="Computation factor for Transportation Import/Export.")
@click.option('-S', '--serialization', 'serialization', default=serialization_flag, 
              show_default=True, required=False, type=bool,
              help="If true input data will be read from stored pkl files.")
@click.option('-D', '--dynamization', 'dynamization_activated', default=dynamization_activated, 
              show_default=True, required=False, type=bool,
              help="If true dynamization of TiMBA will be activated, if not the model will not develop further.")
@click.option('-COQ', '--cleaned_opt_quantity', 'cleaned_opt_quantity', default=cleaned_opt_quantity, show_default=True,
              required=False, type=bool, help="Flag to clean optimization quantities after extraction")
@click.option('-CP', '--capped_prices', 'capped_prices', default=capped_prices, 
              show_default=True, required=False, type=bool,
              help="If activated prices will be capped by a maximum."
              "(Only not capped prices were validated extensively)")
@click.option('-VO', '--verb_opt_log', 'verbose_optimization_logger', default=verbose_optimization_logger,
              show_default=True, required=False, type=bool,
              help="If true the logs will show verbose optimization output.")
@click.option('-VT', '--verb_calc_log', 'verbose_calculation_logger', default=verbose_calculation_logger, 
              show_default=True, required=False, type=bool,
              help="If true the logs will show verbose calculation informations.")
@click.option('-FP', '--folderpath', 'folderpath', required=False, type=click.Path(
    file_okay=False, writable=True, path_type=Path), help="Path to directory with Input/Output folder.")

def timba_cli(year, max_period, calc_product_price, calc_world_price, material_balance, global_material_balance,
        transportation_impexp_factor, serialization, dynamization_activated, cleaned_opt_quantity, capped_prices,
        verbose_optimization_logger, verbose_calculation_logger, folderpath):
    
    user_input_cli = {"year": year, "max_period": max_period, "product_price": calc_product_price,
                      "world_price": calc_world_price, "transportation_factor": transportation_impexp_factor,
                      "material_balance": material_balance, "global_material_balance": global_material_balance,
                      "serialization": serialization, "constants": constants,
                      "dynamization_activated": dynamization_activated, "cleaned_opt_quantity": cleaned_opt_quantity,
                      "capped_prices": capped_prices, "verbose_optimization_logger": verbose_optimization_logger,
                      "verbose_calculation_logger": verbose_calculation_logger,
                      "addInfo": read_additional_information_file}
    
    Parameters = ParameterCollector(user_input=user_input_cli, folderpath=folderpath)
    PACKAGEDIR = Path(__file__).parents[1]
    world_list = os.listdir(INPUT_WORLD_PATH)
    for world in world_list:
        current_dt = dt.datetime.now().strftime("%Y%m%dT%H-%M-%S")
        print(f"The model starts now:", (dt.datetime.now().strftime("%m/%d/%Y, %H:%M:%S")),"\n")
        print(f"Path:", INPUT_WORLD_PATH)
        print(f"Name of input file:", world[:len(world) - 5],"\n")
        print(f"User input for model settings:\n",
              f"Start year: {Parameters.year}\n",
              f"Number of periods: {Parameters.max_period}\n",
              f"Calculation of prices by: {Parameters.calc_product_prices}\n",
              f"Calculation of world prices by: {Parameters.calc_world_prices}\n",
              f"Material balance: {Parameters.material_balance}\n",
              f"Input data through serialization: {Parameters.serialization}\n",
              f"Dynamization activated: {Parameters.dynamization_activated}\n",
              f"Prices are capped: {Parameters.capped_prices}\n",
              f"Optimization gives verbose logs: {Parameters.verbose_optimization_logger}\n",
              f"TiMBA gives verbose logs: {Parameters.verbose_calculation_logger}\n",
              f"Read additional informations: {Parameters.addInfo}\n")
        main(UserIO=Parameters,
             world_version=world,
             time_stamp=current_dt,
             package_dir=PACKAGEDIR,
             sc_name=world[:len(world) - 5])
        world_count = len(world_list)


@click.command()
@click.option('-U', '--user', default="TI-Forest-Sector-Modelling", show_default=True, required=True)
@click.option('-R', '--repo', default="TiMBA_Additional_Information", show_default=True, required=True)
@click.option('-B', '--branch', default="main_add_TiMBA_input_data", show_default=True, required=True)
@click.option('-F', '--folder', default="Input_Data/default_scenario", show_default=True, required=True)
@click.option('-D', '--destination', default="data/input/", show_default=True, required=True)
def load_data_cli(user, repo, branch, folder, destination):
    """CLI wrapper for loading additional input data from GitHub"""
    PACKAGEDIR = Path(__file__).parents[1]
    load_data(
        user=user,
        repo=repo,
        branch=branch,
        source_folder=folder,
        dest_repo_path=PACKAGEDIR,
        dest_folder=destination
    )

cli.add_command(timba_cli, name="timba")
cli.add_command(load_data_cli, name="load_data")


if __name__ == '__main__':
    cli()
