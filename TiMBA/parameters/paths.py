import datetime as dt

current_dt = dt.datetime.now().strftime("%Y%m%dT%H-%M-%S")

# input
INPUT_WORLD_PATH = r"data/input/01_Input_Files/"
ADDITIONAL_INFORMATION_PATH = r"data/input/02_Additional_Information/additional_information.xlsx"
WORLDPRICE_PATH = r"data/input/02_Additional_Information/worldprice_world500.xlsx"
PKL_WORLD_PATH = r"data/input/03_Serialization/WorldDataContent.pkl"
PKL_ADD_INFO_PATH = r"data/input/03_Serialization/AddInfoContent.pkl"
PKL_WORLDPRICE_PATH = r"data/input/03_Serialization/WorldPriceContent.pkl"
PKL_OUTPUT_PATH = "E:\\GFPM\\Toolbox for TiMBA\\Archive\\BEPASO_results_with_TiMBA\\"

# output
RESULTS_OUTPUT = "data/output/results_D"
RESULTS_OUTPUT_AGG = "data/output/results_aggregated_D"
FOREST_OUTPUT = "data/output/forest_D"
WORLD_PRICE_OUTPUT = "data/output/world_prices_D"
MANUFACTURE_OUTPUT = "data/output/manufacture_D"
LOGGING_OUTPUT_FOLDER = r"data/output"

# plot
ADDINFOPTHTOOLBOX = r"data/input/02_Additional_Information/"
OUTPUT_FILE = "\\data\\output\\results_D*.csv"
OUTPUT_DIR = "\\data\\output\\"
INPUT_DIR = "\\analysis\\Data\\TiMBA\\"
