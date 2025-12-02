# from TiMBA.logic.model_extensions import TiMBAExtensions
# from TiMBA.data_management.ParameterCollector import ParameterCollector
# from TiMBA.parameters.Defines import ParamNames
# from TiMBA.user_io.default_parameters import (
#     default_year, default_max_period, default_calc_product_price, default_calc_world_price,
#     default_transportation_impexp_factor, default_MB, serialization_flag, constants, dynamization_activated,
#     capped_prices, cleaned_opt_quantity, global_material_balance, verbose_optimization_logger,
#     verbose_calculation_logger, read_additional_information_file, test_timba_results)
# import unittest
# import pandas as pd


# class TestTiMBAExtensionsClass(unittest.TestCase):

#     def test_carbon_module_extension(self):
#         user_input = {
#             # General TiMBA parameters
#             ParamNames.year.value: default_year,
#             ParamNames.max_period.value: default_max_period,
#             ParamNames.product_price.value: default_calc_product_price,
#             ParamNames.world_price.value: default_calc_world_price,
#             ParamNames.transportation_factor.value: default_transportation_impexp_factor,
#             ParamNames.material_balance.value: default_MB,
#             ParamNames.serialization.value: serialization_flag,
#             ParamNames.constants.value: constants,
#             ParamNames.dynamization_activated.value: dynamization_activated,
#             ParamNames.capped_prices.value: capped_prices,
#             ParamNames.cleaned_opt_quantity.value: cleaned_opt_quantity,
#             ParamNames.global_material_balance.value: global_material_balance,
#             ParamNames.verbose_optimization_logger.value: verbose_optimization_logger,
#             ParamNames.verbose_calculation_logger.value: verbose_calculation_logger,
#             ParamNames.addInfo.value: read_additional_information_file,
#             ParamNames.test_timba_results.value: test_timba_results,
#             # Carbon Module related parameters
#             ParamNames.activate_cmodule.value: True,
#             ParamNames.sc_num.value: None,
#             ParamNames.read_in_pkl.value: True,
#             ParamNames.calc_c_forest_agb.value: True,
#             ParamNames.calc_c_forest_bgb.value: True,
#             ParamNames.calc_c_forest_soil.value: True,
#             ParamNames.calc_c_forest_dwl.value: True,
#             ParamNames.calc_c_hwp.value: True,
#             ParamNames.c_hwp_accounting_approach.value: "stock-change",
#             ParamNames.historical_c_hwp.value: "average",
#             ParamNames.hist_hwp_start_year.value: "default",
#             ParamNames.hist_hwp_start_year_default.value: default_year,
#             ParamNames.show_carbon_dashboard.value: False,
#             ParamNames.fao_data_update.value: False
#         }
#         Parameters = ParameterCollector(user_input=user_input)
#         extensions = TiMBAExtensions(UserOptions=Parameters)
#         extensions.run_carbon_module()

#         self.assertIn(extensions.c_module.sc_list[0], extensions.c_module.carbon_data)
#         sc_data = extensions.c_module.carbon_data[extensions.c_module.sc_list[0]]
#         self.assertIsInstance(sc_data, dict)
#         self.assertEqual(len(sc_data), 6)

#         # check that all values are DataFrames
#         for key, value in sc_data.items():
#             self.assertIsInstance(value, pd.DataFrame, f"{key} is not a DataFrame")


# if __name__ == '__main__':
#     unittest.main()
