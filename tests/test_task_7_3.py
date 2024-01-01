import pytest

from tasks.task_7_3 import Shops

data = [
    ("Skirt", "red", "S", "You selected red Skirt in size S that costs 50$. There are(is) 3 item(s) in our shop."),
    ("Dress", "blue", "M",
     "You selected blue Dress in size M that costs 89$. Unfortunately, no such items are left in our shop."),
    ("Coat", "blue", "M", "Unfortunately, there is no such item in our shop."),
    ("Dress", "red", "XS", "Unfortunately, there is no such item in our shop."),
    ("Dress", "pink", "S", "Unfortunately, there is no such item in our shop.")
]


@pytest.mark.parametrize("input_name, input_color, input_size, expected_result", data)
def test_select_item_as_dataclass(input_name, input_color, input_size, expected_result):
    """verify select_item_as_dataclass function"""
    shop1 = Shops("cloth_shop.json", "assets")
    assert shop1.select_item_as_dataclass(input_name, input_color, input_size) == expected_result
