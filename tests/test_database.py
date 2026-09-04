import unittest
import os
import pandas as pd
from database import DatabaseManager
from sqlalchemy.engine import Engine

class TestDatabaseManager(unittest.TestCase):
    def setUp(self):
        self.database = DatabaseManager()
    def test_database_manager_created(self):
        self.assertIsNotNone(self.database)
    def test_database_path(self):
        self.assertEqual(self.database.database_path,"sqlite:///output/assignment.db")
    def test_engine_created(self):
        self.assertIsNotNone(self.database.get_engine())
    def test_get_engine_returns_engine(self):
        self.assertEqual(self.database.get_engine(), self.database.engine)
    def test_save_dataframe_none(self):
        with self.assertRaises(ValueError):
            self.database.save_dataframe(None, "training_data")
    def test_save_dataframe(self):
        dataframe = pd.DataFrame({"x": [1, 2], "y": [10, 20]})
        self.database.save_dataframe(dataframe, "sample_table")
    def test_create_database(self):
        self.database.create_database()
    def test_engine_type(self):
        self.assertIsInstance(self.database.get_engine(),Engine)