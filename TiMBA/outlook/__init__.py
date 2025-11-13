"""TiMBA Runner object and scenario mechanisms for the purpose of outlook simulations


from TiMBA.outlook import TIMBA_DATA_DIR
"""

import os
from pathlib import Path

# TODO: use upstream behaviour once issue 72 is solved
# https://github.com/TI-Forest-Sector-Modelling/TiMBA/issues/72
timba_data_dir = os.environ.get('TIMBA_DATA_DIR')
if timba_data_dir is None:
    raise ValueError("Environment variable TIMBA_DATA_DIR is not set")

TIMBA_DATA_DIR = Path(timba_data_dir)



