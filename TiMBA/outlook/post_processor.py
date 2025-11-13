"""Transform TiMBA simulation output for further processing

Unfortunately TiMBA doesn't use snake case for variable names, it's a mixture
of camel case and snake case which makes variables harder to remember and can
be a source of confusion. For example

    output["data_periods"].columns
    Index(['RegionCode', 'CommodityCode', 'domain', 'price', 'quantity',
           'elasticity_price', 'slope', 'intercept', 'Period', 'year',
           'shadow_price', 'lower_bound', 'upper_bound'],
          dtype='object')

In November 2025, we were tempted to fix case issues by replacing all column
names with snake case. We dropped the attempt for now.

"""

from pathlib import Path
import gzip
import pandas
import pickle
import re


def load_timba_output_pickle(file_name):
    """Load Timba simulation output from a pickle file.

    Example:

    >>> from TiMBA.outlook.post_processor import load_timba_output_pickle
    >>> pkl_file = "~/eu_cbm/TiMBA_Data/output/DataContainer_Sc_scenario_input_SSP2v3_2020_2050_new_20251112T17-05-24.pkl"
    >>> output = load_timba_output_pickle(pkl_file)
    >>> print(output.keys())

    """
    file = Path(file_name).expanduser()
    if not file.exists():
        raise FileNotFoundError(file)
    with gzip.open(file, "rb") as f:
        output = pickle.load(f)
    return output


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




# class ScenarioInput():
#
#     def __init__(self):
#         self.
#
#     @property
#     def region
