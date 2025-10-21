from typing import Union
import os
from pathlib import Path
import logging
from TiMBA.parameters import LOGGING_OUTPUT_FOLDER


def get_logger(user_path: Union[str, Path, None],time_stamp:str):
    filename = rf"{time_stamp}_TiMBA.log"

    if user_path is None:
        filepath = LOGGING_OUTPUT_FOLDER / filename
    else:
        filepath = user_path / LOGGING_OUTPUT_FOLDER / filename
    if not os.path.exists(filepath):
        os.makedirs(user_path / LOGGING_OUTPUT_FOLDER, exist_ok=True)

    Logger = logging.getLogger("TiMBA")
    if not Logger.hasHandlers():
        Logger.setLevel(logging.DEBUG)
        formatter = logging.Formatter(
            '%(asctime)s %(levelname)s %(lineno)s: %(message)s',
            '%d.%m.%y %H:%M:%S'
        )
        handler = logging.FileHandler(filepath, 'a+')
        handler.setFormatter(formatter)
        Logger.addHandler(handler)

        console = logging.StreamHandler()
        console.setLevel(logging.INFO)
        console_formatter = logging.Formatter('%(name)-10s: %(levelname)-10s %(message)s')
        console.setFormatter(console_formatter)
        Logger.addHandler(console)
    return Logger

def close_logger():
    logging.shutdown()
