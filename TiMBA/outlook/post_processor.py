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

import re
from pathlib import Path
import gzip
import pickle

import pandas

def to_snake_case(name):
    """Convert column name to snake_case."""
    # Convert to string and strip whitespace
    name = str(name).strip()

    # Replace spaces and non-alphanumeric characters with underscores
    name = re.sub(r"[^\w]+", "_", name)

    # Insert underscore before uppercase letters that follow lowercase letters
    name = re.sub(r"([a-z0-9])([A-Z])", r"\1_\2", name)

    # Insert underscore before uppercase letters that are followed by lowercase letters
    name = re.sub(r"([A-Z]+)([A-Z][a-z])", r"\1_\2", name)

    # Convert to lowercase
    name = name.lower()

    # Remove leading/trailing underscores and collapse multiple underscores
    name = re.sub(r"_+", "_", name).strip("_")

    return name


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


def load_metadata(file_name, sheet_name="Specification"):
    """Load country and product names from the Excel specification sheet

    from TiMBA.outlook.post_processor import load_metadata
    excel_file = "~/eu_cbm/TiMBA_Data/input/01_Input_Files/scenario_input_SSP2v3_2020_2050_new.xlsx"
    metadata = load_metadata(excel_file)
    print(metadata["region"])
    print(metadata["commodity"])

    """
    Path(file_name).expanduser()
    df = pandas.read_excel(file_name, sheet_name)
    df_region = df[["Region Code", "Region Name"]].copy()
    df_commodity = df[["Commodity Code", "Commodity Name"]].copy()
    df_commodity = df_commodity.loc[~df_commodity["Commodity Code"].isna()]
    df_property = df[["Property Name", "Property Value"]].copy()
    df_property = df_property.loc[~df_property["Property Name"].isna()]
    return {"region": df_region, "commodity": df_commodity, "property": df_property}


# runner.df_region
# runner.output.df


# class runner():
#
#     def __init__(self):
#         self.
#
#     @property
#     def region
