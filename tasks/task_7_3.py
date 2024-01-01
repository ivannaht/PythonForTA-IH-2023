from tasks.cloth_shop import ClothShop, AvailabilityByColor
from tasks.task_7_2 import ClothShopFileEditor


class Shops(ClothShopFileEditor):
    """Child class for selecting items from cloth_shop.json file """

    def __init__(self, json_file, directory):
        """Child class for reading and modifying geometric_shapes.json file """
        ClothShopFileEditor.__init__(self, json_file, directory)

    @staticmethod
    def convert_dict_to_dataclass(d, className):
        """function to create tuple-like objects with named fields and fixed length"""
        return className.from_dict(d)

    def select_item_as_dataclass(self, input_name, input_color, input_size):
        """function selecting item from cloth_shop.json file by id"""
        for d in self.data:
            item = self.convert_dict_to_dataclass(d, ClothShop)
            if item.name == input_name:
                for a in range(len(item.availability)):
                    if item.availability[a].color == input_color and item.availability[a].size == input_size:
                        if item.availability[a].quantity == 0:
                            return (
                                f"You selected {item.availability[a].color} {item.name} in size {item.availability[a].size} "
                                f"that costs {item.price}$. Unfortunately, no such items are left in our shop.")
                        else:
                            return (
                                f"You selected {item.availability[a].color} {item.name} in size {item.availability[a].size} "
                                f"that costs {item.price}$. There are(is) {item.availability[a].quantity} item(s) in our shop.")

        return "Unfortunately, there is no such item in our shop."


shop1 = Shops("cloth_shop.json", "assets")
print(shop1.select_item_as_dataclass("Skirt", "red", "S"))
