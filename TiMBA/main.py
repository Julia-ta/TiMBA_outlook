from TiMBA.main_runner.main_runner import main
from TiMBA.logic.model_extensions import run_extensions
from TiMBA.data_management.ParameterCollector import ParameterCollector
from TiMBA.parameters import INPUT_WORLD_PATH
from pathlib import Path
import datetime as dt
import os
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)

PACKAGEDIR = Path(__file__).parent.absolute()

if __name__ == '__main__':
    from TiMBA.user_io.default_parameters import user_input
    Parameters = ParameterCollector(user_input=user_input)
    world_list = os.listdir(INPUT_WORLD_PATH)
    for world in world_list:
        current_dt = dt.datetime.now().strftime("%Y%m%dT%H-%M-%S")
        print(f"The model starts now:", (dt.datetime.now().strftime("%m/%d/%Y, %H:%M:%S")),"\n")
        print(f"Path:", INPUT_WORLD_PATH)
        print(f"Name of input file:", world[:len(world) - 5], "\n")
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

