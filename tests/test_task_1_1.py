import pytest

from helpers.custom_exceptions import InsufficientAgeError, EmptyValueError
from tasks.task_1_1 import User

data = [
    ("first", "5", "second", InsufficientAgeError),
    ("a", "b", "c", ValueError),
    ("", "20", "test", EmptyValueError),
    ("test", "20", "", EmptyValueError),
    ("first", "", "second",  EmptyValueError),
]


@pytest.mark.parametrize("name, age, city, e", data)
def test_show_user_info_with_exceptions(name, age, city, e):
    """verify show_user_info function"""
    with pytest.raises(e):
        user = User(name, age, city)
        user.show_user_info()
