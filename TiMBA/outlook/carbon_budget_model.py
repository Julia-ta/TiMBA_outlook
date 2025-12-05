"""Prepare harvest and production data for the EU Carbon Budget Model"""

from pathlib import Path
import pandas
from TiMBA.outlook.metadata import EU_COUNTRIES_LIST


def interpolate_quantity(df):
    """Interpolate quantity

    input data frame has these columns of interest

    In [7]: df[['region_name', 'region_code', 'commodity_name', 'commodity_code','domain',  'quantity','period', "year"]]
    Out[7]:
           region_name region_code commodity_name  commodity_code  domain      quantity  period  year
    0          Algeria          a0     IndRoundNC            78.0  Demand  1.000000e-10       0  2020
    1          Algeria          a0     SawnwoodNC            79.0  Demand  5.700022e+01       0  2020
    2          Algeria          a0       Fuelwood            80.0  Demand  8.791000e+03       0  2020
    3          Algeria          a0       IndRound            81.0  Demand  1.000000e-10       0  2020
    4          Algeria          a0    OthIndRound            82.0  Demand  5.200001e+01       0  2020
    ...            ...         ...            ...             ...     ...           ...     ...   ...
    159275         NaN          zy      OthFbrPlp            89.0  Supply  1.000000e-10      10  2050
    159276         NaN          zy     WastePaper            90.0  Supply  1.000000e-10      10  2050
    159277         NaN          zy      Newsprint            91.0  Supply  1.000000e-10      10  2050
    159278         NaN          zy        PWPaper            92.0  Supply  1.000000e-10      10  2050
    159279         NaN          zy       OthPaper            93.0  Supply  1.000000e-10      10  2050

    [159280 rows x 8 columns]

    Year have sometimes a 5 year spacing for example 2030, 2035, create all
    years and group by region commodity and domain, then interpolate quantity
    for the missing year, using pandas interpolate.

    Some years are missing, e.g.:
    In [11]: df.year.unique()
    Out[11]: array([2020, 2021, 2022, 2023, 2024, 2025, 2030, 2035, 2040, 2045, 2050])

    Example use :

    >>> from TiMBA.outlook.carbon_budget_model import interpolate_quantity
    >>> df2 = interpolate_quantity(df)

    """
    index = ['region_name', 'region_code', 'commodity_name', 'commodity_code', 'domain']
    years = list(range(df['year'].min(), df['year'].max() + 1))
    unique_groups = df[index].drop_duplicates()
    # Create all combinations of groups and years using cross join
    years_df = pandas.DataFrame({'year': years})
    index_with_all_years = unique_groups.assign(key=1).merge(years_df.assign(key=1), on='key').drop('key', axis=1)
    # Merge with original df
    full_df = index_with_all_years.merge(df, on=index + ['year'], how='outer')
    # Interpolate
    full_df["quantity"] = full_df.groupby(index)["quantity"].transform(pandas.Series.interpolate)
    return full_df


def create_cbm_harvest_demand_input(df, dest_dir):
    """Create CBM harvest demand input by transforming TIMBA output to the required format.

    The input data frame has columns including region_name, commodity_name, domain, year, quantity, etc.
    The output is a wide-format table with faostat_name, element, unit, country, and value_year columns.

    - faostat_name: Aggregated commodity names (e.g., 'Industrial roundwood' from sum of IndRoundNC, IndRound, OthIndRound)
    - element: Mapped from domain (e.g., 'Production' for 'Demand')
    - unit: '1000m3' for all
    - country: from region_name
    - value_year: Pivoted quantity values for each year

    Args:
        df (pd.DataFrame): The prepared TIMBA data DataFrame.
        dest_dir (Path): Directory to save the output CSV file.

    Example load data from the first available pickle output file, complement
    with metadata from the first available world input file and create CBM
    harvest demand input in a temporary directory:

    >>> from TiMBA.outlook import TIMBA_DATA_DIR
    >>> from TiMBA.outlook.post_processor import load_timba_output_pickle
    >>> from TiMBA.outlook.carbon_budget_model import create_cbm_harvest_demand_input
    >>> from TiMBA.outlook.metadata import add_region_and_commodity_columns
    >>> pkl_file = next((TIMBA_DATA_DIR / "output").glob("*.pkl"))
    >>> output = load_timba_output_pickle(pkl_file)
    >>> df_raw = output['data_periods']
    >>> world_input_file = TIMBA_DATA_DIR / next((TIMBA_DATA_DIR / "input/01_Input_Files").glob("*.xlsx"))
    >>> df = add_region_and_commodity_columns(df_raw, world_input_file)
    >>> create_cbm_harvest_demand_input(df, "/tmp")

    """
    commodity_map = pandas.DataFrame(
        {
            "commodity_name": ["IndRoundNC", "IndRound", "OthIndRound", "Fuelwood"],
            "faostat_name": [
                "Industrial roundwood",
                "Industrial roundwood",
                "Industrial roundwood",
                "fuelwood",
            ],
        }
    )
    df = df.merge(commodity_map, on="commodity_name", how="left")
    df = df.dropna(subset=["faostat_name"])
    element_map = pandas.DataFrame(
        {"domain": ["Demand", "Supply"], "element": ["Production", "Production"]}
    )
    df = df.merge(element_map, on="domain", how="left")
    df["unit"] = "1000m3"
    df["country"] = df["region_name"]
    df_agg = (
        df.groupby(["country", "faostat_name", "element", "unit", "year"])["quantity"]
        .sum()
        .reset_index()
    )
    df_agg["year_text"] = "value_" + df_agg["year"].astype(str)
    df_agg.drop(columns=["year"], inplace=True)
    # Pivot to wide format
    df_wide = df_agg.pivot(
        index=["country", "faostat_name", "element", "unit"],
        columns="year_text",
        values="quantity",
    ).reset_index()
    # Keep only EU countries
    selector = df_wide["country"].isin(EU_COUNTRIES_LIST)
    df_wide = df_wide.loc[selector].copy()
    # Filter and write to separate files
    df_irw = df_wide[df_wide['faostat_name'] == 'Industrial roundwood']
    df_fw = df_wide[df_wide['faostat_name'] == 'fuelwood']
    irw_file = Path(dest_dir) / "irw_harvest.csv"
    fw_file = Path(dest_dir) / "fw_harvest.csv"
    df_irw.to_csv(irw_file, index=False)
    df_fw.to_csv(fw_file, index=False)
    print(f"Industrial roundwood output saved to {irw_file}")
    print(f"Fuelwood output saved to {fw_file}")

