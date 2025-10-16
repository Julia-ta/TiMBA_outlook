from TiMBA.main_runner.main_runner import main
from TiMBA.data_management.ParameterCollector import ParameterCollector
from TiMBA.parameters import INPUT_WORLD_PATH, DATA_FOLDER
from pathlib import Path
import datetime as dt
import os
import warnings
import sys
warnings.simplefilter(action='ignore', category=FutureWarning)
from TiMBA.user_io.default_parameters import user_input
Parameters = ParameterCollector(user_input=user_input)

def run_timba(Parameters=Parameters,folderpath:str=None):
    PACKAGEDIR = Path(__file__).parent.absolute()
    if folderpath is None:
            folderpath = PACKAGEDIR
    INPUT_PATH = folderpath / DATA_FOLDER / INPUT_WORLD_PATH
    try:
        world_list = os.listdir(INPUT_PATH)
    except FileNotFoundError:
        print("FileNotFoundError at: ",INPUT_PATH)
        print(f"Make sure input data is downloaded to {INPUT_PATH} \nor change the folder path where the data is stored.")
        sys.exit(1)
    for world in world_list:
        current_dt = dt.datetime.now().strftime("%Y%m%dT%H-%M-%S")
        print("The model starts now:", (dt.datetime.now().strftime("%m/%d/%Y, %H:%M:%S")),"\n")
        print(f"Path: {folderpath}")
        print(f"Name of input file: {world[:len(world) - 5]} \n")
        print("User input for model settings:\n",
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
             Data_Path=folderpath / DATA_FOLDER,
             sc_name=world[:len(world) - 5])     

if __name__ == '__main__':
     run_timba(Parameters=Parameters)#,folderpath=Path(r"E:/"))


