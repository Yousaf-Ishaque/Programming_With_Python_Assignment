"""
Name of file: database.py
This file examines and then subsequently manages SQL Lite database
"""
from sqlalchemy import create_engine
from sqlalchemy.exc import SQLAlchemyError

class DatabaseManager:
    """
    This is the class that incepts and manages the SQL Lite database
    """
    def __init__(self, database_path="sqlite:///output/assignment.db"):
        """
        This class function handles the initialization SQLite database.
        The path of database is parameterized into this class function
        """
        self.database_path = database_path
        self.engine = create_engine(self.database_path)
    def create_database(self):
        """
        This step gives rise to SQL Lite database and display Database created successfully
        otherwise it returns an error stating the reason for failure using the method of standard exceptions
        """
        try:
            with self.engine.connect():
                print("Database created successfully!")
        except SQLAlchemyError as e:
            print(f"Database Error: {e}")
    def get_engine(self):
        """
        SQL Alchemy return so further commands can be incorporated to the database
        """
        return self.engine
    def save_dataframe(self, dataframe, table_name):
        """
        This function saves all the Pandas Data Frames to a SQLite Table.
        Parameters of this Function:
            dataframe (DataFrame): The Pandas Data Frame that needs to be saved
            table_name (str): This will be the name of the SQL table that will be created
        """
        if dataframe is None:
            raise ValueError("DataFrame cannot be None.")
        """
        This validation check ensures that the file return is not None. If it returns non it
        gives rise to exception.
        """
        try:
            dataframe.to_sql(name = table_name, con = self.engine, if_exists = "replace", index = False)
            print(f"'{table_name}' table saved successfully.")
        except SQLAlchemyError as e:
            raise RuntimeError(f"Database Error: {e}")