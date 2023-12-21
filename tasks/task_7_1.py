import json
from collections import namedtuple
from pathlib import Path
import random


class JsonFileEditor:
    """Parent class for reading and modifying JSON file"""

    def __init__(self, json_file="geometric_shapes.json", directory="assets"):
        """Constructor for user"""
        self.json_file = json_file
        self.directory = directory
        self.base_dir = Path(__file__).resolve().parent.parent
        self.data_file = self.base_dir.joinpath(self.directory).joinpath(self.json_file)
        self.data = self.get_items

    @property
    def get_items(self):
        """function for reading items from JSON file"""
        with open(self.data_file) as file:
            return json.load(file)

    def generate_new_item(self):
        pass

    def set_items(self):
        """function for writing items in JSON file"""
        data = self.get_items
        with open(self.data_file, mode="w") as file:
            new_item = self.generate_new_item()
            data.append(new_item)
            json.dump(data, file, indent=4)


class GeometricShapesFileEditor(JsonFileEditor):
    """Child class for reading and modifying JSON file """

    def __init__(self, json_file, directory):
        super(self.__class__, self).__init__(json_file, directory)

    @staticmethod
    def convert_dict_to_namedtuple(d):
        """function to create tuple-like objects with named fields and fixed length"""
        return namedtuple('Item', d.keys())(**d)

    def generate_new_item(self):
        """function for generating new item"""
        colors_list = ["green", "blue", "red", "pink"]
        color = random.choice(colors_list)
        materials_list = ["wood", "glass", "paper", "metal"]
        material = random.choice(materials_list)
        radius = random.randint(1, 9)
        figure_list = [{"name": "sphere", "type": "3D"}, {"name": "circle", "type": "2D"}]
        figure = random.choice(figure_list)
        return dict(id=len(self.data) + 1, name=figure["name"], type=figure["type"], radius=radius, material=material,
                    color=color)

    def select_item(self, input_id):
        """function selecting item from JSON file by id"""
        for i in self.data:
            item = self.convert_dict_to_namedtuple(i)
            if str(item.id) == input_id:
                return f"You selected {item.color} {item.name} from {item.material}"
