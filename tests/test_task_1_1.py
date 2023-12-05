import pytest

from helpers.custom_exceptions import InsufficientAgeError
from tasks.task_1_1 import show_user_info

data = [
        ("First", 5, "Second", InsufficientAgeError)
        # ("a", "b", "c", ValueError)
]

@pytest.mark.parametrize("name, age, city, e", data)
def test_show_user_info_with_exceptions(name, age, city, e):
    """verify show_user_info function"""
    with pytest.raises(e):
        assert show_user_info(name, age, city, e)

