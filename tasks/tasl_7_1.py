import json
from collections import namedtuple
from pathlib import Path

jsonFile = "geometric_shapes.json"
assetsDirectory = "assets"

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_FILE = BASE_DIR.joinpath(assetsDirectory).joinpath(jsonFile)


def convert_dict_to_namedtuple(d):
    return namedtuple('Item', d.keys())(**d)


def get_item():
    """function for reading items from JSON file"""
    input_id = input("Please select item by id\n")
    with open(DATA_FILE, mode="r") as file:
        data = json.load(file)
        for i in data:
            item = convert_dict_to_namedtuple(i)
            if str(item.id) == input_id:
                print(f"You selected {item.color} {item.name} from {item.material}")
            else:
                print(f"The item with {item.id} does not exist")


def set_items():
    """function for writing items in JSON file"""
    with open(DATA_FILE, mode="a") as file:
        # data = json.load(file)
        # print(data)
        new_item = generate_new_item()
        # data.append(new_item)
        json.dump(new_item, file)


def generate_new_item():
    return dict(id=5, name="sphere", type="3D", radius=4, material="glass", color="green")


set_items()