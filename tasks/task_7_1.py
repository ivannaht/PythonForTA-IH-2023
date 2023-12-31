from collections import namedtuple
import random
from tasks.json_file_editor import JsonFileEditor


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
