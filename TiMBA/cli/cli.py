from pathlib import Path
import click
import os
import datetime as dt
from TiMBA.main_runner.main_runner import main
from TiMBA.logic.model_extensions import run_extensions
from TiMBA.data_management.ParameterCollector import ParameterCollector
from TiMBA.parameters import INPUT_WORLD_PATH
from TiMBA.parameters.Defines import ParamNames
from c_module.logic.main import C_Module
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)
from TiMBA.user_io.default_parameters import (default_year, default_max_period, default_calc_product_price,
                                              default_calc_world_price, default_transportation_impexp_factor, default_MB,
                                              global_material_balance, serialization_flag, constants,
                                              dynamization_activated, cleaned_opt_quantity, capped_prices,
                                              verbose_optimization_logger, verbose_calculation_logger,
                                              read_additional_information_file, activate_add_on_cmodule, sc_num,
                                              read_in_pkl, calc_c_forest_agb, calc_c_forest_bgb, calc_c_forest_soil,
                                              calc_c_forest_dwl, calc_c_hwp, c_hwp_accounting_approach,
                                              historical_c_hwp, hist_hwp_start_year, hist_hwp_start_year_default,
                                              show_carbon_dashboard)


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
@click.option('-AC', '--activate_cmodule', 'activate_cmodule',
              default=False, show_default=True, required=False, type=bool,
              help="Flag to activate carbon module.")

def timba_cli(year, max_period, calc_product_price, calc_world_price, material_balance, global_material_balance,
              transportation_impexp_factor, serialization, dynamization_activated, cleaned_opt_quantity, capped_prices,
              verbose_optimization_logger, verbose_calculation_logger, folderpath, activate_cmodule):
    
    user_input_cli = {ParamNames.year.value: year,
                      ParamNames.max_period.value: max_period,
                      ParamNames.product_price.value: calc_product_price,
                      ParamNames.world_price.value: calc_world_price,
                      ParamNames.transportation_factor.value: transportation_impexp_factor,
                      ParamNames.material_balance.value: material_balance,
                      ParamNames.global_material_balance.value: global_material_balance,
                      ParamNames.serialization.value: serialization,
                      ParamNames.constants.value: constants,
                      ParamNames.dynamization_activated.value: dynamization_activated,
                      ParamNames.cleaned_opt_quantity.value: cleaned_opt_quantity,
                      ParamNames.capped_prices.value: capped_prices,
                      ParamNames.verbose_optimization_logger.value: verbose_optimization_logger,
                      ParamNames.verbose_calculation_logger.value: verbose_calculation_logger,
                      ParamNames.addInfo.value: read_additional_information_file,
                      ParamNames.activate_cmodule.value: activate_cmodule,
                      ParamNames.sc_num.value: sc_num,
                      ParamNames.read_in_pkl.value: read_in_pkl,
                      ParamNames.calc_c_forest_agb.value: calc_c_forest_agb,
                      ParamNames.calc_c_forest_bgb.value: calc_c_forest_bgb,
                      ParamNames.calc_c_forest_soil.value: calc_c_forest_soil,
                      ParamNames.calc_c_forest_dwl.value: calc_c_forest_dwl,
                      ParamNames.calc_c_hwp.value: calc_c_hwp,
                      ParamNames.c_hwp_accounting_approach.value: c_hwp_accounting_approach,
                      ParamNames.historical_c_hwp.value: historical_c_hwp,
                      ParamNames.hist_hwp_start_year.value: hist_hwp_start_year,
                      ParamNames.hist_hwp_start_year_default.value: hist_hwp_start_year_default,
                      ParamNames.show_carbon_dashboard.value: show_carbon_dashboard,
                      }
    
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

    run_extensions(UserIO=Parameters)


# Carbon Module command
@click.command()
@click.option('-SC', '--sc_num', "sc_num",
              default=sc_num, show_default=True, required=True, type=int,
              help="Flag to control the number of processed scenarios.")
@click.option('-CF_AGB', '--calc_c_forest_agb', "calc_c_forest_agb",
              default=calc_c_forest_agb, show_default=True, required=True, type=bool,
              help="Flag to activate carbon calculation for aboveground forest biomass.")
@click.option('-CF_BGB', '--calc_c_forest_bgb', "calc_c_forest_bgb",
              default=calc_c_forest_bgb, show_default=True, required=True, type=bool,
              help="Flag to activate carbon calculation for belowground forest biomass.")
@click.option('-CF_S', '--calc_c_forest_soil', "calc_c_forest_soil",
              default=calc_c_forest_soil, show_default=True, required=True, type=bool,
              help="Flag to activate carbon calculation for forest soil.")
@click.option('-CF_DWL', '--calc_c_forest_dwl', "calc_c_forest_dwl",
              default=calc_c_forest_dwl, show_default=True, required=True, type=bool,
              help="Flag to activate carbon calculation for dead wood and litter.")
@click.option('-C_HWP', '--calc_c_hwp', "calc_c_hwp",
              default=calc_c_hwp, show_default=True, required=True, type=bool,
              help="Flag to activate carbon calculation for harvested wood products.")
@click.option('-C_HWP_A', '--c_hwp_accounting_approach', "c_hwp_accounting_approach",
              default=c_hwp_accounting_approach, show_default=True, required=True,
              type=str, help="Flag to select the accounting approach for carbon in harvested wood products.")
@click.option('-R', '--read_in_pkl', "read_in_pkl",
              default=read_in_pkl, show_default=True, required=True, type=bool,
              help="Flag to control if pkl- or csv-files are read; reads in if True.")
@click.option('-SD', '--show_carbon_dashboard', 'show_carbon_dashboard',
              default=show_carbon_dashboard, show_default=True, required=False, type=bool,
              help="Flag to launch carbon dashboard.")

def carbon_cli(calc_c_forest_agb, sc_num, calc_c_forest_bgb, calc_c_forest_soil, calc_c_forest_dwl, calc_c_hwp,
               c_hwp_accounting_approach, read_in_pkl, show_carbon_dashboard):

    user_input_cli = {
        ParamNames.activate_cmodule.value: activate_add_on_cmodule,
        ParamNames.sc_num.value: sc_num,
        ParamNames.read_in_pkl.value: read_in_pkl,
        ParamNames.calc_c_forest_agb.value: calc_c_forest_agb,
        ParamNames.calc_c_forest_bgb.value: calc_c_forest_bgb,
        ParamNames.calc_c_forest_soil.value: calc_c_forest_soil,
        ParamNames.calc_c_forest_dwl.value: calc_c_forest_dwl,
        ParamNames.calc_c_hwp.value: calc_c_hwp,
        ParamNames.c_hwp_accounting_approach.value: c_hwp_accounting_approach,
        ParamNames.show_carbon_dashboard.value: show_carbon_dashboard,
        # Adavanced settings not available via CLI
        ParamNames.historical_c_hwp.value: historical_c_hwp,
        ParamNames.hist_hwp_start_year.value: hist_hwp_start_year,
        ParamNames.hist_hwp_start_year_default.value: hist_hwp_start_year_default,
    }

    c_module = C_Module(UserInput=user_input_cli)
    c_module.run()


cli.add_command(timba_cli, name="timba")
cli.add_command(carbon_cli, name="carbon")

