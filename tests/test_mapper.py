import unittest
from data_loader import DataLoader
from function_selector import FunctionSelector
from mapper import TestMapper

class TestMapperModule(unittest.TestCase):
    def setUp(self):
        loader = DataLoader()
        self.training_df = loader.load_training_data()
        self.ideal_df = loader.load_ideal_data()
        self.test_df = loader.load_test_data()
        selector = FunctionSelector(self.training_df, self.ideal_df)
        self.best_functions = selector.select_best_functions()
        self.mapper = TestMapper(self.test_df, self.ideal_df, self.best_functions)
    def test_mapper_created(self):
        self.assertIsNotNone(self.mapper)
    def test_mapping_returns_list(self):
        mapped_points = self.mapper.map_test_data()
        self.assertIsInstance(mapped_points, list)
    def test_mapping_not_empty(self):
        mapped_points = self.mapper.map_test_data()
        self.assertGreater(len(mapped_points), 0)
    def test_each_mapping_is_dictionary(self):
        mapped_points = self.mapper.map_test_data()
        for point in mapped_points:
            self.assertIsInstance(point, dict)
    def test_mapping_contains_required_keys(self):
        mapped_points = self.mapper.map_test_data()
        required_keys = ["x", "y", "ideal_function", "ideal_y", "deviation"]
        for point in mapped_points:
            for key in required_keys:
                self.assertIn(key, point)
    def test_ideal_function_is_string(self):
        mapped_points = self.mapper.map_test_data()
        for point in mapped_points:
            self.assertIsInstance(point["ideal_function"], str)
    def test_deviation_is_numeric(self):
        mapped_points = self.mapper.map_test_data()
        for point in mapped_points:
            self.assertIsInstance(point["deviation"], float)
    def test_x_and_y_are_numeric(self):
        mapped_points = self.mapper.map_test_data()
        for point in mapped_points:
            self.assertIsInstance(point["x"], float)
            self.assertIsInstance(point["y"], float)