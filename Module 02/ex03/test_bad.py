"""
testing bad csv
"""
from csvreader import CsvReader

if __name__ == "__main__":
    with CsvReader('bad.csv') as file:
        if file is None:
            print("File is corrupted")
        data = file.getdata()
        print(data)
