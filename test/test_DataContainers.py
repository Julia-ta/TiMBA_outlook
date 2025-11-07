# import os
# import unittest


# from TiMBA.parameters import INPUT_WORLD_PATH
# from TiMBA.parameters.Domains import Domains
# from TiMBA.data_management.DataManager import DataManager
# from TiMBA.data_management.DataContainer import DataContainer, InterfaceWorldData, WorldDataCollector

# world_version_unit_test = os.listdir(INPUT_WORLD_PATH)[0]


# class TestDataContainerClasses(unittest.TestCase):

#     def test_DataContainer(self):
#         DC = DataContainer("test")
#         self.assertIsInstance(DC, DataContainer)
#         self.assertTrue(hasattr(DC, "filepath"))
#         self.assertTrue(DC.data.empty)
#         self.assertTrue(DC.domain is None)

#     def test_Interface(self):
#         def test_interface():
#             Interface = InterfaceWorldData("test")
#             print(Interface)
#         self.assertRaises(TypeError, test_interface)
#         self.assertTrue(hasattr(InterfaceWorldData, "set_attribute"))
#         self.assertTrue(issubclass(InterfaceWorldData, DataContainer))

#     def test_Class_WorldDataCollector(self):
#         self.assertTrue(issubclass(WorldDataCollector, (InterfaceWorldData, DataContainer)))
#         self.assertTrue(hasattr(WorldDataCollector, "set_attribute"))

#     def test_Instance_WorldDataCollector(self):
#         WDC = WorldDataCollector(INPUT_WORLD_PATH + "/" + world_version_unit_test)

#         self.assertFalse(hasattr(WDC, "attr_test_1"))
#         DataManager.set_attribute(WDC, "attr_test_1", [1, 2, 3])
#         self.assertTrue(hasattr(WDC, "attr_test_1"))
#         self.assertTrue(WDC.attr_test_1 == [1, 2, 3])
#         self.assertTrue(WDC["attr_test_1"] == [1, 2, 3])

#         self.assertFalse(hasattr(WDC, "attr_test_2"))
#         WDC["attr_test_2"] = [4, 5, 6]
#         self.assertTrue(hasattr(WDC, "attr_test_2"))
#         self.assertTrue(WDC.attr_test_2 == [4, 5, 6])
#         self.assertTrue(WDC["attr_test_2"] == [4, 5, 6])

#         name = str(Domains.Specification)
#         self.assertFalse(hasattr(WDC, name))
#         DataManager.set_attribute(WDC, name, DataContainer(WDC.filepath))
#         self.assertTrue(hasattr(WDC, name))
#         self.assertTrue(hasattr(WDC[name], "data"))
#         self.assertTrue(WDC.filepath == INPUT_WORLD_PATH + "/" + world_version_unit_test)

#         self.assertTrue(WDC[name].data.empty)
#         self.assertTrue(WDC.Specification.data.empty)
#         WDC[name].data = DataManager.read_excel(WDC.filepath, str(Domains.Specification))
#         comparison = DataManager.read_excel(WDC.filepath, str(Domains.Specification))
#         self.assertTrue(WDC[name].data.compare(comparison).empty)

#         TEST_NAME = "TEST_NAME"
#         INPUT_WORLD_PATH_LOOPED = INPUT_WORLD_PATH + "/" + world_version_unit_test
#         expected_repr = f"Content from {os.path.basename(INPUT_WORLD_PATH_LOOPED)}; Sheet: {TEST_NAME}"
#         WDC[name].update_domain_name("TEST_NAME")
#         self.assertTrue(repr(WDC[name]).replace("\'", "") == expected_repr)


# if __name__ == '__main__':
#     unittest.main()
#     print("Finished")
