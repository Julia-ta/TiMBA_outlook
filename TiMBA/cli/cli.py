from pathlib import Path
import click
import os
import datetime as dt
import warnings

from TiMBA.main_runner.main_runner import main
from TiMBA.data_management.ParameterCollector import ParameterCollector
from TiMBA.data_management.Load_Data import load_data
from TiMBA.parameters import INPUT_WORLD_PATH
from TiMBA.user_io.default_parameters import (
    default_year, default_max_period, default_calc_product_price,
    default_calc_world_price, default_transportation_impexp_factor, default_MB,
    global_material_balance, serialization_flag, constants,
    dynamization_activated, cleaned_opt_quantity, capped_prices,
    verbose_optimization_logger, verbose_calculation_logger,
    read_additional_information_file
)

warnings.simplefilter(action='ignore', category=FutureWarning)


@click.group()
def cli():
    """Main entry point for TiMBA CLI"""
    pass


@click.command()
@click.option('-Y', '--year', default=default_year, type=int, show_default=True, required=True)
@click.option('-MP', '--max_period', default=default_max_period, type=int, show_default=True, required=True)
@click.option('-PP', '--calc_product_price', default=default_calc_product_price, type=str, show_default=True, required=True)
@click.option('-WP', '--calc_world_price', default=default_calc_world_price, type=str, show_default=True, required=True)
@click.option('-MB', '--material_balance', default=default_MB, type=str, show_default=True, required=True)
@click.option('-GMB', '--global_material_balance', default=global_material_balance, type=bool, show_default=True)
@click.option('-TF', '--trans_imp_exp_factor', default=default_transportation_impexp_factor, type=float, show_default=True, required=True)
@click.option('-S', '--serialization', default=serialization_flag, type=bool, show_default=True)
@click.option('-D', '--dynamization', default=dynamization_activated, type=bool, show_default=True)
@click.option('-COQ', '--cleaned_opt_quantity', default=cleaned_opt_quantity, type=bool, show_default=True)
@click.option('-CP', '--capped_prices', default=capped_prices, type=bool, show_default=True)
@click.option('-VO', '--verb_opt_log', default=verbose_optimization_logger, type=bool, show_default=True)
@click.option('-VT', '--verb_calc_log', default=verbose_calculation_logger, type=bool, show_default=True)
@click.option('-FP', '--folderpath', type=click.Path(file_okay=False, writable=True, path_type=Path))
def timba_cli(year, max_period, calc_product_price, calc_world_price, material_balance, global_material_balance,
              transportation_impexp_factor, serialization, dynamization_activated, cleaned_opt_quantity, capped_prices,
              verbose_optimization_logger, verbose_calculation_logger, folderpath):

    user_input_cli = {
        "year": year, "max_period": max_period, "product_price": calc_product_price,
        "world_price": calc_world_price, "transportation_factor": transportation_impexp_factor,
        "material_balance": material_balance, "global_material_balance": global_material_balance,
        "serialization": serialization, "constants": constants,
        "dynamization_activated": dynamization_activated, "cleaned_opt_quantity": cleaned_opt_quantity,
        "capped_prices": capped_prices, "verbose_optimization_logger": verbose_optimization_logger,
        "verbose_calculation_logger": verbose_calculation_logger,
        "addInfo": read_additional_information_file
    }

    Parameters = ParameterCollector(user_input=user_input_cli, folderpath=folderpath)
    PACKAGEDIR = Path(__file__).parents[1]
    world_list = os.listdir(INPUT_WORLD_PATH)

    for world in world_list:
        current_dt = dt.datetime.now().strftime("%Y%m%dT%H-%M-%S")
        print(f"The model starts now: {dt.datetime.now().strftime('%m/%d/%Y, %H:%M:%S')}")
        print(f"Path: {INPUT_WORLD_PATH}")
        print(f"Name of input file: {world[:-5]}")

        main(UserIO=Parameters,
             world_version=world,
             time_stamp=current_dt,
             package_dir=PACKAGEDIR,
             sc_name=world[:-5])


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
