from tasks.task_7_1 import GeometricShapesFileEditor

file_1 = GeometricShapesFileEditor("geometric_shapes.json", "assets")
file_1.add_item()

print(file_1.data)
print(file_1.select_item("1"))
print(file_1.select_item("40"))
print(file_1.generate_new_item())
