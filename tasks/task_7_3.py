import random

from tasks.json_file_editor import JsonFileEditor


class ClothShopFileEditor(JsonFileEditor):
    """Child class for reading and modifying JSON file """

    def __init__(self, json_file, directory):
        super(self.__class__, self).__init__(json_file, directory)

    def generate_new_item(self):
        """function for generating new item"""
        name_list = ["Hoodie", "Trousers", "Jumper", "T-shirt", "Jacket"]
        name = random.choice(name_list)
        type_list = ["male", "femail"]
        type = random.choice(type_list)

        return dict(
            id=len(self.data) + 1,
            name=name,
            colors=["white", "black", "gray"],
            sizes=["XS", "S", "M", "L", "XL"],
            type=type
        )
