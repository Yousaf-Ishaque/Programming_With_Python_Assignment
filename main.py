# Main execution workflow: load, process, map, test and visualize the datasets.

""" Main execution workflow: Load, Process, Map, Test, and Visualization of datasets """


from database import DatabaseManager
from data_loader import DataLoader
from function_selector import FunctionSelector
from mapper import TestMapper
import pandas as pd
from visualizer import DataVisualizer
from pandas.errors import EmptyDataError, ParserError
from exceptions import InvalidDatasetError


def main():

    print("=" * 60)
    print("PROGRAM STARTED")
    print("=" * 60)
    # --------------------------------------------------
    # 1st Step: Inception of Database
    # --------------------------------------------------
    db = DatabaseManager()
    db.create_database()
    # --------------------------------------------------
    # 2nd Step: Datasets Loading
    # --------------------------------------------------
    loader = DataLoader()

    try:
        training_df = loader.load_training_data()
        ideal_df = loader.load_ideal_data()
        test_df = loader.load_test_data()

    except InvalidDatasetError as error:
        print(f"\nDataset validation error: {error}")
        return

    except (FileNotFoundError, EmptyDataError, ParserError, PermissionError) as error:
        print(f"\nDataset loading error: {error}")
        return

    print("\n✓ All datasets loaded successfully.")
    # --------------------------------------------------
    # 3rd Step: Exhibiting the Shapes of Datasets
    # --------------------------------------------------
    print("\nDataset Shapes")
    print("-" * 40)
    print(f"Training Dataset : {training_df.shape}")
    print(f"Ideal Dataset    : {ideal_df.shape}")
    print(f"Test Dataset     : {test_df.shape}")
    # --------------------------------------------------
    # 4th Step: Loading the Datasets into SQLite
    # --------------------------------------------------
    db.save_dataframe(training_df, "training_data")
    db.save_dataframe(ideal_df, "ideal_data")
    db.save_dataframe(test_df, "test_data")
    print("\n✓ All datasets saved into SQLite.")
    # --------------------------------------------------
    # 5th Step: Choosing the Most Suitable Ideal Functions
    # --------------------------------------------------
    selector = FunctionSelector(training_df, ideal_df)
    best_functions = selector.select_best_functions()
    print("\nSelected Ideal Functions")
    print("=" * 60)
    for training_function, best_match in best_functions.items():
        print(f"\nTraining Function : {training_function}")
        print(f"Ideal Function    : {best_match[0]}")
        print(f"SSE               : {best_match[1]:.6f}")
        print(f"Maximum Deviation : {best_match[2]:.6f}")
    # --------------------------------------------------
    # 6th Step: Mapping the Test Data
    # --------------------------------------------------
    mapper = TestMapper(test_df, ideal_df, best_functions)
    mapping_results = mapper.map_test_data()
    mapping_df = pd.DataFrame(mapping_results)
    print("\nMapped Test Data")
    print("=" * 60)
    print(f"Total mapped test points : {len(mapping_results)}")
    print("\nFirst 10 Mapped Test Points\n")
    for result in mapping_results[:10]:
        print(result)
    db.save_dataframe(mapping_df, "mapped_test_data")
    print("\n" + "=" * 60)
    print("DATA PROCESSING COMPLETED SUCCESSFULLY")
    print("=" * 60)
    visualizer = DataVisualizer(training_df, ideal_df, test_df, mapping_df, best_functions, mapping_results)
    visualizer.create_figure()
    visualizer.plot_training_functions()
    visualizer.plot_chosen_ideal_functions()
    visualizer.plot_mapped_points()
    visualizer.plot_test_data()
    visualizer.setup_dropdown()
    visualizer.show_visualization()

if __name__ == "__main__":
    main()