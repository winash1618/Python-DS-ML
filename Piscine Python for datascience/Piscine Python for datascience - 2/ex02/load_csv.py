import pandas as pd
from pandas import DataFrame

def load(path: str) -> DataFrame:
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