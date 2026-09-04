"""
exceptions.py
This file comprises of custom exceptions that will be used with several other files.
Custom exception or user-defined exceptions are utilized in this file because it is an integral requirement of the assignement as per assignment guidelines
"""
class InvalidDatasetError(Exception):
    """
    Raised when the structure of a dataset is not in conformity with the desired format.
    """
    def __init__(self, message):
        """
        Commences the exception with a specified error message.
        """
        super().__init__(message)
        