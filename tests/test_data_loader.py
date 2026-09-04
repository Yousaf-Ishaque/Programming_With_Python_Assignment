import unittest
from data_loader import DataLoader
class TestDataLoader(unittest.TestCase):

    def setUp(self):
        self.loader = DataLoader()
    def test_training_data_loaded(self):
        training_df = self.loader.load_training_data()
        self.assertIsNotNone(training_df)
    def test_training_data_shape(self):
        training_df = self.loader.load_training_data()
        self.assertEqual(training_df.shape, (400, 5))
    def test_training_columns(self):
        training_df = self.loader.load_training_data()
        expected_columns = ["x", "y1", "y2", "y3", "y4"]
        self.assertEqual(list(training_df.columns), expected_columns)
    def test_training_not_empty(self):
        training_df = self.loader.load_training_data()
        self.assertFalse(training_df.empty)
    def test_ideal_data_loaded(self):
        ideal_df = self.loader.load_ideal_data()
        self.assertIsNotNone(ideal_df)
    def test_ideal_data_shape(self):
        ideal_df = self.loader.load_ideal_data()
    def test_ideal_dataframe_not_empty(self):
        ideal_df = self.loader.load_ideal_data()
        self.assertFalse(ideal_df.empty)
    def test_ideal_columns_exist(self):
        ideal_df = self.loader.load_ideal_data()
        self.assertIn("x", ideal_df.columns)
        self.assertIn("y1", ideal_df.columns)
        self.assertIn("y50", ideal_df.columns)
        self.assertEqual(ideal_df.shape, (400, 51))