"""
data_loader.py Module
This module uses Pandas Data Frame
"""
import pandas as pd
from pandas.errors import EmptyDataError, ParserError
from exceptions import InvalidDatasetError
class DataLoader:
    """
    In this step, the code fetches the 3 data sets i.e training data, ideal functions data and test data.
    """

    def __init__(self):
        """
        Location of the files is stored in sepearate varaibles for each of training, ideal and test csv files
        """
        self.train_path = "datasets/train.csv"
        self.ideal_path = "datasets/ideal.csv"
        self.test_path = "datasets/test.csv"
    def load_training_data(self):
        """
        This part of code loads the training data and in case of failure gives a message stating the cause of failure.
        """
        try:
            train_df = pd.read_csv(self.train_path)
            if train_df.shape[1] != 5:
                raise InvalidDatasetError("Training dataset must contain exactly 5 columns.")
            return train_df
        except (FileNotFoundError, EmptyDataError, ParserError, PermissionError):
            raise
    def load_ideal_data(self):
        """
        This section of code loads the ideal dataset and in case of an error it returns with the cause of error.
        """
        try:
            ideal_df = pd.read_csv(self.ideal_path)
            if ideal_df.shape[1] != 51:
                raise InvalidDatasetError("Ideal dataset must contain exactly 51 columns.")
            return ideal_df
        except (FileNotFoundError, EmptyDataError, ParserError, PermissionError):
            raise
    def load_test_data(self):
        """
        Just like the above two sections, it loads the test dataset and in case of unsuccessful loading it returns a message telling the cause of failure.
        """
        try:
            test_df = pd.read_csv(self.test_path)
            if test_df.shape[1] != 2:
                raise InvalidDatasetError("Test dataset must contain exactly 2 columns.")
            return test_df
        except (FileNotFoundError, EmptyDataError, ParserError, PermissionError):
            raise