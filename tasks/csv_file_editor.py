import csv
from pathlib import Path


class CsvFileEditor:
    """Parent class for reading and modifying CSV file"""

    def __init__(self, csv_file="creds.csv", directory="assets"):
        """Constructor for user"""
        base_dir = Path(__file__).resolve().parent.parent
        self.data_file = base_dir.joinpath(directory).joinpath(csv_file)
        self.data = self.get_data

    @property
    def get_data(self):
        """function for reading data from CSV file"""
        with open(self.data_file) as file:
            reader = csv.reader(file)
            # skip the first row with table headers
            next(reader)
            data = [tuple(row) for row in reader]

        return data

    def generate_new_data(self):
        raise NotImplementedError("Child class must implement this abstract method")

    def add_data(self):
        """function for writing data in CSV file"""
        with open(self.data_file, mode="a") as file:
            writer = csv.writer(file)
            new_data = self.generate_new_data()
            writer.writerow(new_data)
