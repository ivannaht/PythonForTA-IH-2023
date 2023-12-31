from tasks.task_7_3 import ClothShopFileEditor

file_2 = ClothShopFileEditor("cloth_shop.json", "assets")
file_2.generate_new_item()
file_2.add_item()

print(file_2.data)
