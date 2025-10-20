from pathlib import Path
import click
import os
import datetime as dt
from urllib.error import URLError
from TiMBA.main import run_timba
from TiMBA.data_management.ParameterCollector import ParameterCollector
from TiMBA.data_management.Load_Data import load_data
from TiMBA.parameters import INPUT_WORLD_PATH
from TiMBA.parameters.paths import OUTPUT_DIR, GIT_USER,GIT_REPO,GIT_BRANCH,GIT_FOLDER,DESTINATION_PATH
import warnings
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
    run_timba(Parameters=Parameters,folderpath=folderpath)


@click.command()
@click.option('-U', '--user', default=GIT_USER, show_default=True, required=True,
              help="Name of the GitHub user who stored the data.")
@click.option('-R', '--repo', default=GIT_REPO, show_default=True, required=True,
              help="Name of the GitHub repository where stored the data.")
@click.option('-B', '--branch', default=GIT_BRANCH, show_default=True, required=True,
              help="Name of the branch where stored the data.")
@click.option('-F', '--folder', default=GIT_FOLDER, show_default=True, required=True,
              help="The folder path within the repository where stored the data.")
@click.option('-D', '--destination', default=DESTINATION_PATH, show_default=True, required=True,
              help="The destination where the data should be copied to.")
def load_data_cli(user, repo, branch, folder, destination):
    """CLI wrapper for loading additional input data from GitHub"""
    PACKAGEDIR = Path(__file__).parents[1]
    try:
        load_data(
            user=user,
            repo=repo,
            branch=branch,
            source_folder=folder,
            dest_repo_path=PACKAGEDIR,
            dest_folder=destination
        )
    except URLError:
        print(f"Failed to download input data from GitHub.\n",
              "Please check your internet connection, ensure that",
              "'https://github.com' is reachable from your environment and try again.")

cli.add_command(timba_cli, name="timba")
cli.add_command(load_data_cli, name="load_data")


if __name__ == '__main__':
    cli()
