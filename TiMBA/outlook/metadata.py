"""Load metadata to complement information in TiMBA output tables."""

import re
from pathlib import Path
import pandas

EU_COUNTRIES_LIST = [
    "Austria",
    "Belgium",
    "Bulgaria",
    "Croatia",
    "Czech Republic",
    "Denmark",
    "Finland",
    "France",
    "Germany",
    "Greece",
    "Hungary",
    "Luxembourg",
    "Ireland",
    "Italy",
    "Netherlands",
    "Poland",
    "Portugal",
    "Romania",
    "Slovakia",
    "Slovenia",
    "Spain",
    "Sweden",
    "Estonia",
    "Latvia",
    "Lithuania"
]


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


def load_metadata_from_world_input_file(file_name, sheet_name="Specification"):
    """Load country and product names from the Excel specification sheet

    Example use:

    >>> from TiMBA.outlook.metadata import load_metadata_from_world_input_file
    >>> excel_file = "~/eu_cbm/TiMBA_Data/input/01_Input_Files/scenario_input_SSP2v3_2020_2050_new.xlsx"
    >>> metadata = load_metadata_from_world_input_file(excel_file)
    >>> print(metadata["region"])
    >>> print(metadata["commodity"])
    >>> print(metadata["property"])

    """
    Path(file_name).expanduser()
    df = pandas.read_excel(file_name, sheet_name)
    df = df.rename(columns=to_snake_case)
    df_region = df[["region_code", "region_name"]].copy()
    df_commodity = df[["commodity_code", "commodity_name"]].copy()
    df_commodity = df_commodity.loc[~df_commodity["commodity_code"].isna()]
    df_property = df[["property_name", "property_value"]].copy()
    df_property = df_property.loc[~df_property["property_name"].isna()]
    return {"region": df_region, "commodity": df_commodity, "property": df_property}


def add_region_and_commodity_columns(df, world_input_file):
    """Prepare TIMBA data for CBM by merging region and commodity metadata and reordering columns.

    Args:
        df (pd.DataFrame): The data_periods DataFrame from TIMBA output.
        world_input_file (Path): Path to the world input Excel file.

    Returns:
        pd.DataFrame: The prepared DataFrame with merged metadata and reordered columns.


    Example using the first available pickle file and excel files in the output
    and input directories respectively:

    >>> from TiMBA.outlook import TIMBA_DATA_DIR
    >>> from TiMBA.outlook.post_processor import load_timba_output_pickle
    >>> from TiMBA.outlook.metadata import add_region_and_commodity_columns
    >>> pkl_file = next((TIMBA_DATA_DIR / "output").glob("*.pkl"))
    >>> output = load_timba_output_pickle(pkl_file)
    >>> df_raw = output['data_periods']
    >>> world_input_file = TIMBA_DATA_DIR / next((TIMBA_DATA_DIR / "input/01_Input_Files").glob("*.xlsx"))
    >>> df = add_region_and_commodity_columns(df_raw, world_input_file)

    """
    metadata = load_metadata_from_world_input_file(world_input_file)
    df = df.merge(metadata["region"], on="region_code", how="left")
    df = df.merge(metadata["commodity"], on="commodity_code", how="left")
    # Place region and commodity columns first
    columns_to_front = ['region_name', 'region_code', 'commodity_name', 'commodity_code']
    remaining_columns = [col for col in df.columns if col not in columns_to_front]
    df = df[columns_to_front + remaining_columns]
    return df

