import unittest
from data_loader import DataLoader
from function_selector import FunctionSelector
class TestFunctionSelector(unittest.TestCase):

    def setUp(self):
        loader = DataLoader()
        self.training_df = loader.load_training_data()
        self.ideal_df = loader.load_ideal_data()
        self.selector = FunctionSelector(self.training_df, self.ideal_df)
    def test_selector_created(self):
        self.assertIsNotNone(self.selector)
    def test_best_functions_return_dictionary(self):
        best_functions = self.selector.select_best_functions()
        self.assertIsInstance(best_functions, dict)
    def test_number_of_selected_functions(self):
        best_functions = self.selector.select_best_functions()
        self.assertEqual(len(best_functions), 4)
    def test_training_function_keys(self):
        best_functions = self.selector.select_best_functions()
        expected_keys = ["y1", "y2", "y3", "y4"]
        self.assertEqual(list(best_functions.keys()), expected_keys)
    def test_best_function_value_is_tuple(self):
        best_functions = self.selector.select_best_functions()
        for value in best_functions.values():
            self.assertIsInstance(value, tuple)
    def test_tuple_contains_three_elements(self):
        best_functions = self.selector.select_best_functions()
        for value in best_functions.values():
            self.assertEqual(len(value), 3)
    def test_sse_is_numeric(self):
        best_functions = self.selector.select_best_functions()
        for value in best_functions.values():
            self.assertIsInstance(value[1], float)
    def test_maximum_deviation_is_numeric(self):
        best_functions = self.selector.select_best_functions()
        for value in best_functions.values():
            self.assertIsInstance(value[2], float)