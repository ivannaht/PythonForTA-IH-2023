import random
from tasks.json_file_editor import JsonFileEditor


class ClothShopFileEditor(JsonFileEditor):
    """Child class for reading and modifying cloth_shop.json file """

    def __init__(self, json_file, directory):
        """Child class for reading and modifying geometric_shapes.json file """
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
            type=type,
            colors=["red", "black", "blue"],
            sizes=["XS", "S", "M", "L", "XL"],
            availability_by_color=[
                {
                    'red': [
                        {'size': 'XS', 'quantity': 3}, {'size': 'S', 'quantity': 2},
                        {'size': 'M', 'quantity': 5}, {'size': 'L', 'quantity': 0},
                        {'size': 'XL', 'quantity': 1}
                    ]
                },
                {
                    'black': [
                        {'size': 'XS', 'quantity': 3}, {'size': 'S', 'quantity': 2},
                        {'size': 'M', 'quantity': 5}, {'size': 'L', 'quantity': 0},
                        {'size': 'XL', 'quantity': 1}
                    ]
                },
                {
                    'blue': [
                        {'size': 'XS', 'quantity': 3}, {'size': 'S', 'quantity': 2},
                        {'size': 'M', 'quantity': 5}, {'size': 'L', 'quantity': 0},
                        {'size': 'XL', 'quantity': 1}
                    ]
                }
            ]
        )


file_2 = ClothShopFileEditor("cloth_shop.json", "assets")
print(file_2.generate_new_item())
file_2.add_item()

print(file_2.data)
print(len(file_2.data))
