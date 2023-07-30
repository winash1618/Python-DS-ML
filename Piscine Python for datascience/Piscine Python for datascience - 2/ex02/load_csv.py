import pandas as pd
from pandas import DataFrame


def load(path: str) -> DataFrame:
    """
    Load data from a CSV file into a pandas DataFrame.

    Args:
        path (str): The file path of the CSV file.

    Returns:
        DataFrame: The pandas DataFrame containing the data from the CSV file.

    Raises:
        FileNotFoundError: If the CSV file is not found at the specified path.
        pd.errors.ParserError: If there is an issue parsing the CSV file.
        Exception: For any other unexpected errors during loading.
    """
    try:
        df = pd.read_csv(path)
        num_rows, num_cols = df.shape
        print(f"DataFrame dimensions: {num_rows} rows x {num_cols} columns")
        return df
    except FileNotFoundError:
        print(f"Error: File not found at '{path}'")
    except pd.errors.ParserError:
        print(f"Error: Failed to parse CSV file at '{path}'")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
