"""
testing good csv
"""
from csvreader import CsvReader

if __name__ == "__main__":
    with CsvReader('good.csv') as file:
        data = file.getdata()
        header = file.getheader()
        print(data)
        print(header)
