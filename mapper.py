import numpy as np

class TestMapper:
    def __init__(self, test_df, ideal_df, best_functions):
        """
        This function gives rise to the mapper.
        Parameters of the function:
            test_df: Fetches value from test dataset
            ideal_df: Fetches values from ideal dataset
            best_functions: Dictionary returning back the best function with minimum deviation
        """
        self.test_df = test_df
        self.ideal_df = ideal_df
        self.best_functions = best_functions
    def map_test_data(self):
        mapping_results = []
        for row_index, test_row in self.test_df.iterrows():
            x = test_row["x"]
            y = test_row["y"]
            # Initialize best match
            best_deviation = float("inf")
            best_function = None
            best_ideal_y = None
            # Compare with the four selected ideal functions
            for train_function, best_match in self.best_functions.items():
                ideal_function, _, maximum_deviation = best_match
                # Get ideal y-value at the same row
                ideal_y = self.ideal_df.loc[self.ideal_df["x"] == x, ideal_function].iloc[0]
                # Calculate deviation
                deviation = abs(y - ideal_y)
                # Assignment threshold
                threshold = np.sqrt(2) * maximum_deviation
                # Keep the closest acceptable function
                if deviation <= threshold and deviation < best_deviation:
                    best_deviation = deviation
                    best_function = ideal_function
                    best_ideal_y = ideal_y
            # Store accepted mapping
            if best_function is not None:
                mapping_results.append({"x": float(x), "y": float(y), "ideal_function": best_function, "ideal_y": float(best_ideal_y), "deviation": float(best_deviation)})
        return mapping_results