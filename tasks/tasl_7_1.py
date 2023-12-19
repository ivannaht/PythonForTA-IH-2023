import json
from collections import namedtuple
from pathlib import Path
import random

jsonFile = "geometric_shapes.json"
assetsDirectory = "assets"

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_FILE = BASE_DIR.joinpath(assetsDirectory).joinpath(jsonFile)


def convert_dict_to_namedtuple(d):
    """function for """
    return namedtuple('item', d.keys())(**d)


def get_items():
    """function for reading items from JSON file"""
    with open(DATA_FILE, mode="r") as file:
        return json.load(file)


data = get_items()


def set_items():
    """function for writing items in JSON file"""
    with open(DATA_FILE, mode="w") as file:
        new_item = generate_new_item()
        data.append(new_item)
        json.dump(data, file, indent=4, separators=(',', ': '))


def generate_new_item():
    """function"""
    colors_list = ["green", "blue", "red", "pink"]
    color = random.choice(colors_list)
    materials_list = ["wood", "glass", "paper", "metal"]
    material = random.choice(materials_list)
    radius = random.randint(1, 9)
    figure_list = [{"name": "sphere", "type": "3D"}, {"name": "circle", "type": "2D"}]
    figure = random.choice(figure_list)
    return dict(id = len(data) + 1, name = figure["name"], type = figure["type"], radius = radius, material = material, color = color)


def select_item():
    """function"""
    input_id = input("Please select item by id\n")
    for i in data:
        item = convert_dict_to_namedtuple(i)
        if str(item.id) == input_id:
            return f"You selected {item.color} {item.name} from {item.material}"


set_items()
print(select_item())
