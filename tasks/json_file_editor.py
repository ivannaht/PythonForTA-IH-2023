import json
from pathlib import Path


class JsonFileEditor:
    """Parent class for reading and modifying JSON file"""

    def __init__(self, json_file="geometric_shapes.json", directory="assets"):
        """Constructor for JSON file"""
        base_dir = Path(__file__).resolve().parent.parent
        self.data_file = base_dir.joinpath(directory).joinpath(json_file)
        self.data = self.get_items

    @property
    def get_items(self):
        """function for reading items from JSON file"""
        with open(self.data_file) as file:
            return json.load(file)

    def generate_new_item(self):
        """function for generating new item JSON file"""
        raise NotImplementedError("Child class must implement this abstract method")

    def add_item(self):
        """function for writing items in JSON file"""
        with open(self.data_file, mode="w") as file:
            new_item = self.generate_new_item()
            self.data.append(new_item)
            json.dump(self.data, file, indent=4)
