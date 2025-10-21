import unittest
from pathlib import Path
import shutil
from TiMBA.data_management.DataManager import DataManager
from TiMBA.data_management.ParameterCollector import ParameterCollector
from TiMBA.data_validation.DataValidator import DataValidator
from TiMBA.main import run_timba
from TiMBA.user_io.default_parameters import user_input
from TiMBA.parameters.paths import (
    DATA_FOLDER, GIT_USER, GIT_REPO, GIT_BRANCH,
    GIT_FOLDER, DESTINATION_PATH, OUTPUT_DIR
)
from TiMBA.data_management.Load_Data import load_data

INPUT_UNIT_TEST_TIMBA_RESULT = Path("test_data/DataContainer_Sc_scenario_input.pkl")

class TestTiMBAClass(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.PACKAGEDIR = Path(__file__).parent.absolute()
        cls.INPUT_FOLDER = cls.PACKAGEDIR / DESTINATION_PATH

        # Prepare parameters
        user_input["max_period"] = 1
        cls.Parameters = ParameterCollector(user_input=user_input)

        # load input data from GitHub AddInfo repo
        load_data(
            user=GIT_USER,
            repo=GIT_REPO,
            branch=GIT_BRANCH,
            source_folder=GIT_FOLDER,
            dest_repo_path=DESTINATION_PATH,
            dest_folder=cls.INPUT_FOLDER
        )

        # run TiMBA
        run_timba(Parameters=cls.Parameters, folderpath=cls.PACKAGEDIR)

        # Load reference data
        cls.data_timba_test = DataManager.restore_from_pickle(cls.PACKAGEDIR / INPUT_UNIT_TEST_TIMBA_RESULT)

        # reload TiMBA results
        results_folder = cls.PACKAGEDIR / DATA_FOLDER / OUTPUT_DIR
        results_file = list(results_folder.glob("*.pkl"))[0]
        cls.data_timba = DataManager.restore_from_pickle(results_file)

    def test_timba_results(self):
        if user_input.get("test_timba_results", False):
            test_result = DataValidator.check_timba_results(
                Data=self.data_timba,
                DataTest=self.data_timba_test,
                rel_tolerance=5e-02
            )
            self.assertTrue(test_result, "TiMBA results are not in line with reference data.")

    @classmethod
    def tearDownClass(cls):
        tiMBA_path = cls.PACKAGEDIR / "TiMBA"
        if tiMBA_path.exists():
            shutil.rmtree(tiMBA_path)


if __name__ == '__main__':
    unittest.main()
