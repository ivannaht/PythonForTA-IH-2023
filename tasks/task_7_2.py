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
            price=random.randint(40, 90),
            colors=["red", "black", "blue"],
            sizes=["XS", "S", "M", "L", "XL"],
            availability_by_color=[
                {
                    'red': [
                        {'size': 'XS', 'quantity': random.randint(0, 10)}, {'size': 'S', 'quantity': random.randint(0, 10)},
                        {'size': 'M', 'quantity': random.randint(0, 10)}, {'size': 'L', 'quantity': random.randint(0, 10)},
                        {'size': 'XL', 'quantity': random.randint(0, 10)}
                    ]
                },
                {
                    'black': [
                        {'size': 'XS', 'quantity': random.randint(0, 10)}, {'size': 'S', 'quantity': random.randint(0, 10)},
                        {'size': 'M', 'quantity': random.randint(0, 10)}, {'size': 'L', 'quantity': random.randint(0, 10)},
                        {'size': 'XL', 'quantity': random.randint(0, 10)}
                    ]
                },
                {
                    'blue': [
                        {'size': 'XS', 'quantity': random.randint(0, 10)}, {'size': 'S', 'quantity': random.randint(0, 10)},
                        {'size': 'M', 'quantity': random.randint(0, 10)}, {'size': 'L', 'quantity': random.randint(0, 10)},
                        {'size': 'XL', 'quantity': random.randint(0, 10)}
                    ]
                }
            ]
        )


file_2 = ClothShopFileEditor("cloth_shop.json", "assets")
print(file_2.generate_new_item())
file_2.add_item()

print(file_2.data)
print(len(file_2.data))
