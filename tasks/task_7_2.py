import random
from tasks.json_file_editor import JsonFileEditor


class ClothShopFileEditor(JsonFileEditor):
    """Child class for reading and modifying cloth_shop.json file """

    def __init__(self, json_file, directory):
        """Child class for reading and modifying geometric_shapes.json file """
        JsonFileEditor.__init__(self, json_file, directory)

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
            price=random.randint(40, 99),
            availability=[
                {
                    "color": "red",
                    "size": "S",
                    "quantity": random.randint(0, 10)
                },
                {
                    "color": "red",
                    "size": "M",
                    "quantity": random.randint(0, 10)
                },
                {
                    "color": "red",
                    "size": "L",
                    "quantity": random.randint(0, 10)
                },
                {
                    "color": "black",
                    "size": "S",
                    "quantity": random.randint(0, 10)
                },
                {
                    "color": "black",
                    "size": "M",
                    "quantity": random.randint(0, 10)
                },
                {
                    "color": "black",
                    "size": "L",
                    "quantity": random.randint(0, 10)
                },
                {
                    "color": "blue",
                    "size": "S",
                    "quantity": random.randint(0, 10)
                },
                {
                    "color": "blue",
                    "size": "M",
                    "quantity": random.randint(0, 10)
                },
                {
                    "color": "blue",
                    "size": "L",
                    "quantity": random.randint(0, 10)
                }
            ]
        )


file_2 = ClothShopFileEditor("cloth_shop.json", "assets")
file_2.add_item()
