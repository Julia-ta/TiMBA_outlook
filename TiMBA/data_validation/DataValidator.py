from typing import Tuple
import pandas as pd
import numpy as np
from TiMBA.parameters.Defines import VarNames


class DataValidator:
    """
    Class to perform quick data validation checks during runtime.
    """
    @staticmethod
    def check_slope_intercept(
            slope: pd.Series, intercept: pd.Series, sign_slope: int, sign_intercept: int
    ) -> Tuple[bool, bool]:
        """
        Checks if all calculated slopes and intercepts are greater than or equal 0
        :param slope: Values of slope
        :param intercept: Values of intercept
        :param sign_slope: 1 or -1 dependent on expected outcome (-1 tells that all slope values shall be <= 0)
        :param sign_intercept:  1 or -1 dependent on expected outcome
        :return: boolean for slope and intercept outcome
        """
        sign_slope, sign_intercept = np.sign(sign_slope), np.sign(sign_intercept)
        slope_check_result = (sign_slope * slope >= 0).all()
        intercept_check_result = (sign_intercept * intercept >= 0).all()
        return bool(slope_check_result), bool(intercept_check_result)

    @staticmethod
    def check_timba_results(Data, DataTest, rel_tolerance):
        """
        Checks if latest TiMBA results (Data) match provided validation results (DataTest).
        :param Data: TiMBA results to validate
        :param DataTest: TiMBA reference results
        """
        timba_validation_data = DataTest["data_periods"]
        timba_data_to_validate = Data["data_periods"]

        max_period = max(timba_data_to_validate[VarNames.PERIOD_COLNAME.value])

        timba_validation_data = timba_validation_data[timba_validation_data[VarNames.PERIOD_COLNAME.value] <= max_period]

        test_result = np.allclose(timba_validation_data[[VarNames.PRICE_COLNAME.value, VarNames.QUANTITY_COLNAME.value]],
                                  timba_data_to_validate[[VarNames.PRICE_COLNAME.value, VarNames.QUANTITY_COLNAME.value]],
                                  rtol=rel_tolerance)

        return test_result