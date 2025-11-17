"""Transform TiMBA simulation output for further processing

Unfortunately TiMBA doesn't use snake case for variable names, it's a mixture
of camel case and snake case which makes variables harder to remember and can
be a source of confusion. For example

    output["data_periods"].columns
    Index(['RegionCode', 'CommodityCode', 'domain', 'price', 'quantity',
           'elasticity_price', 'slope', 'intercept', 'Period', 'year',
           'shadow_price', 'lower_bound', 'upper_bound'],
          dtype='object')

In November 2025, we fixed case issues by replacing all column
names in the output with snake case.

"""

from pathlib import Path
import gzip
import pickle
from TiMBA.outlook.metadata import to_snake_case

def load_timba_output_pickle(file_name):
    """Load Timba simulation output from a pickle file.

    Example:

    >>> from TiMBA.outlook.post_processor import load_timba_output_pickle
    >>> pkl_file = "~/eu_cbm/TiMBA_Data/output/DataContainer_Sc_scenario_input_SSP2v3_2020_2050_new_20251112T17-05-24.pkl"
    >>> output = load_timba_output_pickle(pkl_file)
    >>> print(output.keys())
    >>> print(output["data_periods"])

    """
    file = Path(file_name).expanduser()
    if not file.exists():
        raise FileNotFoundError(file)
    with gzip.open(file, "rb") as f:
        output = pickle.load(f)
    snake_case_output = {}
    for key, df in output.items():
        snake_case_output[to_snake_case(key)] = df.rename(columns=to_snake_case)
    return snake_case_output



