import os.path
from os import path
from typing import Union, Tuple

from pathlib import Path

from TiMBA.results_logging.ResultsWriter import ResultsWriter
from .headers import RESULTS_HEADER, RESULTS_AGG_HEADER
from .paths import (
    DATA_FOLDER,
    INPUT_WORLD_PATH,
    ADDITIONAL_INFORMATION_PATH,
    WORLDPRICE_PATH,
    PKL_WORLD_PATH,
    PKL_ADD_INFO_PATH,
    PKL_WORLDPRICE_PATH,
    output_name,
    output_agg_name,
    forest_output_name,
    world_price_output_name,
    manufacture_output_name,
    LOGGING_OUTPUT_FOLDER,
    OUTPUT_DIR,
)

def get_results_writer(output_path: Union[str, Path, None], agg_flag: bool) -> ResultsWriter:
    """
    Spawns instance of Resultswriter based on user input. Allows to differentiate between exhaustive and aggregated
    results.
    :param output_path: Folderpath given by user
    :return: Instance of ResultsWriter
    """
    if agg_flag is not True:
        if output_path is None:
            return ResultsWriter(output_name, filetype=".csv", overwrite_file=False, header=RESULTS_HEADER)
        else:
            fp = os.path.join(output_path, r"output/results.csv")
            if not os.path.exists(output_path):
                os.makedirs(fp, exist_ok=True)
            return ResultsWriter(fp, filetype=".csv", overwrite_file=False, header=RESULTS_HEADER)
    else:
        if output_path is None:
            return ResultsWriter(output_agg_name, filetype=".csv", overwrite_file=False, header=RESULTS_AGG_HEADER)
        else:
            fp = os.path.join(output_path, r"output/results_aggregated.csv")
            if not os.path.exists(output_path):
                os.makedirs(fp, exist_ok=True)
            return ResultsWriter(fp, filetype=".csv", overwrite_file=False, header=RESULTS_AGG_HEADER)


def get_pkl_paths(DATA_PATH: Union[str, Path, None]) -> Tuple[str, str, str]:
    """
    Returns correct paths for and of serialized pkl-files based on user input.
    :param output_path: Folderpath given by user
    :return: tuple of strings being paths
    """
    pkl_world_path = DATA_PATH / PKL_WORLD_PATH
    pkl_add_info_path = DATA_PATH / PKL_ADD_INFO_PATH
    pkl_worldprice_path = DATA_PATH / PKL_WORLDPRICE_PATH
    return pkl_world_path, pkl_add_info_path, pkl_worldprice_path


def get_global_paths(data_path: Union[str, Path, None], worldversion: str) -> Tuple[str, str, str]:
    """
    Returns correct paths for files based on user input.
    :param output_path: Folderpath given by user
    :return: tuple of strings being paths
    """
    input_world_path = data_path / INPUT_WORLD_PATH / worldversion
    additional_information_path = data_path / ADDITIONAL_INFORMATION_PATH
    worldprice_path = data_path / WORLDPRICE_PATH
    return input_world_path, additional_information_path, worldprice_path


def get_output_paths(Data_Path: Path, time_stamp: str, sc_name: str):
    """
    Collect outpaths for pkl files.
    :param package_dir: absolute folder of the model on any environment.
    :param time_stamp: time stamp from main
    :param sc_name: scenario name from main
    :param PKL_OUTPUT_PATH: path to pkl output
    :return: output paths for the pkl files
    """
    OUTPUT_DIRECTORY = Data_Path / OUTPUT_DIR
    os.makedirs(OUTPUT_DIRECTORY, exist_ok=True)
    file_name = str(f"DataContainer_Sc_{sc_name}_{time_stamp}.pkl")
    OUTPUT_PATH = OUTPUT_DIRECTORY / file_name

    return OUTPUT_PATH, OUTPUT_DIRECTORY


__all__ = [
    "get_results_writer",
    "get_global_paths",
    "INPUT_WORLD_PATH",
    "ADDITIONAL_INFORMATION_PATH",
    "WORLDPRICE_PATH",
    "RESULTS_OUTPUT",
    "LOGGING_OUTPUT_FOLDER"
]
