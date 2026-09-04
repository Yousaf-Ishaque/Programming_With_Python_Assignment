import numpy as np

class FunctionSelector:
    """
    This class will make choice of the best of the best ideal function for each training
    function. The criteria for selecting the best ideal function is the Smallest Square
    Method (SSE).
    """
    def __init__(self, training_df, ideal_df):
        """
        This command will intialize the Function selector algorithm.
        Parameters of the Function selector:
            training_df (DataFrame): This is the value that will be picked from training dataset.
            ideal_df (DataFrame): These values will be fetched from ideal dataset.
        """
        self.training_df = training_df
        self.ideal_df = ideal_df
    def calculate_sse(self, training_column, ideal_column):
            """
            This method estimates the sum of difference between a training function
            and a ideal function at a time.
            Parameters of the  calculate_sse method:
                training_column (Series): This fetches the value of one training function.
                ideal_column (Series): This brings forth the value of one ideal function.
            Return of the calculate_sse function: This function is returning sse and it will
            always be a positive value due to the squares. Since, the values can be decimal
            values so the class of SSE will be float.
            """
            difference = training_column - ideal_column
            squared_difference = np.square(difference)
            sse = np.sum(squared_difference)
            maximum_deviation = np.max(np.abs(difference))
            return float(sse), float(maximum_deviation)
            """
            This result returns two tuples. The elaboration of both tuples is listed below.
                    - float: Sum of all the Squared Errors (SSE)
                    - float: Maximum Absolute Deviation 
            """
    def select_best_functions(self):
            """
               This function determines the best ideal functions for each training
               function by making use of Smallest Squares (SSE) Method.
               Returns: This function returns the mapping/ pairing of training functions to
               their best suited ideal function values.
               """
            best_functions = {}
            for train_col in self.training_df.columns[1:]:
                sse_results = []
                for ideal_col in self.ideal_df.columns[1:]:
                    sse, maximum_deviation = self.calculate_sse(self.training_df[train_col], self.ideal_df[ideal_col])
                    sse_results.append((ideal_col, sse, maximum_deviation))
                    best_match = min(sse_results, key=lambda x: x[1])
                    best_functions[train_col] = best_match
            return best_functions