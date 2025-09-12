from TiMBA.parameters.Defines import ParamNames

default_year = 2020
default_max_period = 10
default_calc_product_price = "shadow_PP"  # possibilities: "shadow_PP", "calculated_PP" (Only shadow_PP were validated extensively)
default_calc_world_price = "shadow_WP"  # possbilities: "shadow_WP", "constant_WP", "average_WP, exogen_WP" (Only shadow_WP were validated extensively)

default_MB = "C_specific_MB"  # possibilities:"RC_specific_MB"(= region and commodity specific material balance),
#                                              "RCG_specific_MB"(= region and commodity group specific material balance)
#                                              "C_specific_MB"(= commodity specific material balance) (Only C_specific_MB were validated extensively)

default_transportation_impexp_factor = 1

serialization_flag = False  # if true read data from stored pkl files
constants = [False, False, False]  # [constant prices, constant slopes, constant intercep] (Only default options were validated extensively)
dynamization_activated = True
capped_prices = False # (Only default option was validated extensively)
cleaned_opt_quantity = False  # cleaned opt quantity have not been validated extensively
global_material_balance = False  # Results with global material balance activated have not been validated yet
verbose_optimization_logger = True
verbose_calculation_logger = False
read_additional_information_file = True
test_timba_results = True  # activate unittest to compare TiMBA results with validated results

# Carbon module related parameters
activate_add_on_cmodule = True
sc_num = 4  # Activate if run with CLI
read_in_pkl = True  # Caution False option not implemented yet
calc_c_forest_agb = True
calc_c_forest_bgb = True
calc_c_forest_soil = True
calc_c_forest_dwl = True

calc_c_hwp = True
c_hwp_accounting_approach = "stock-change"  # Options: "stock-change" or "production"
historical_c_hwp = "average"  # Options: "average" or "historical"
hist_hwp_start_year = "default"  # Options: "country-specific" or "default"
hist_hwp_start_year_default = default_year
show_carbon_dashboard = True

user_input = {ParamNames.year.value: default_year,
              ParamNames.max_period.value: default_max_period,
              ParamNames.product_price.value: default_calc_product_price,
              ParamNames.world_price.value: default_calc_world_price,
              ParamNames.transportation_factor.value: default_transportation_impexp_factor,
              ParamNames.material_balance.value: default_MB,
              ParamNames.serialization.value: serialization_flag,
              ParamNames.constants.value: constants,
              ParamNames.dynamization_activated.value: dynamization_activated,
              ParamNames.capped_prices.value: capped_prices,
              ParamNames.cleaned_opt_quantity.value: cleaned_opt_quantity,
              ParamNames.global_material_balance.value: global_material_balance,
              ParamNames.verbose_optimization_logger.value: verbose_optimization_logger,
              ParamNames.verbose_calculation_logger.value: verbose_calculation_logger,
              ParamNames.addInfo.value: read_additional_information_file,
              ParamNames.test_timba_results.value: test_timba_results,
              ParamNames.activate_cmodule.value: activate_add_on_cmodule,
              ParamNames.sc_num.value: sc_num,
              ParamNames.read_in_pkl.value: read_in_pkl,
              ParamNames.calc_c_forest_agb.value: calc_c_forest_agb,
              ParamNames.calc_c_forest_bgb.value: calc_c_forest_bgb,
              ParamNames.calc_c_forest_soil.value: calc_c_forest_soil,
              ParamNames.calc_c_forest_dwl.value: calc_c_forest_dwl,
              ParamNames.calc_c_hwp.value: calc_c_hwp,
              ParamNames.c_hwp_accounting_approach.value: c_hwp_accounting_approach,
              ParamNames.historical_c_hwp.value: historical_c_hwp,
              ParamNames.hist_hwp_start_year.value: hist_hwp_start_year,
              ParamNames.hist_hwp_start_year_default.value: hist_hwp_start_year_default,
              ParamNames.show_carbon_dashboard.value: show_carbon_dashboard,
              }
