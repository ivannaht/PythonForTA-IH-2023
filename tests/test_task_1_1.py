import pytest

from helpers.custom_exceptions import InsufficientAgeError, EmptyValueError
from tasks.task_1_1 import User

data_1 = [
    ("first", "5", "second", "+3 (805) 055-5555", InsufficientAgeError),
    ("a", "b", "c", "d", ValueError),
    ("", "20", "test", "+3 (805) 055-5555", EmptyValueError),
    ("test", "20", "", "+3 (805) 055-5555", EmptyValueError),
    ("first", "", "second", "+3 (805) 055-5555", EmptyValueError),
    ("9ds *", "20", "Lviv", "+3 (805) 055-5555", ValueError),
    ("ds fdf9", "20", "Lviv", "+3 (805) 055-5555", ValueError),
    ("d's f-f j'j hh ss gt i", "20", "Lviv", "+3 (805) 055-5555", ValueError),
    ("abc", "20", "Lviv*fdf P8fdfd", "+3 (805) 055-5555", ValueError),
    ("abc", "20", "Lviv''fdf P--fdfd", "+3 (805) 055-5555", ValueError),
    ("abc", "20", "'Paris-", "+3 (805) 055-5555", ValueError),
    ("Anna", "25", "London", "312345678905", ValueError),
    ("Anna", "25", "London", "+312+34567+8905", ValueError),
]


@pytest.mark.parametrize("name, age, city, phone, e", data_1)
def test_show_user_info_with_exceptions(name, age, city, phone, e):
    """verify show_user_info function"""
    with pytest.raises(e):
        user1 = User(name, age, city, phone)
        user1.show_user_info()


data_2 = [
    ("Anna", "25", "London", "+3 (123) 456-7890",
     "HELLO, ANNA! YOUR AGE IS 25. YOU LIVE IN LONDON. YOUR PHONE NUMBER IS +3 (123) 456-7890."),
    ("Oo'hgh H-JH", "20", "London", "+3(123)4567890",
     "HELLO, OO'HGH H-JH! YOUR AGE IS 20. YOU LIVE IN LONDON. YOUR PHONE NUMBER IS +3(123)4567890."),
    ("O-o l'k", "20", "London", "+3-123-456-7890",
     "HELLO, O-O L'K! YOUR AGE IS 20. YOU LIVE IN LONDON. YOUR PHONE NUMBER IS +3-123-456-7890."),
    ("O-o'p l'k j'k-o h'h", "20", "London", "+31234567890",
     "HELLO, O-O'P L'K J'K-O H'H! YOUR AGE IS 20. YOU LIVE IN LONDON. YOUR PHONE NUMBER IS +31234567890."),
    ("Anna", "25", "London-l'p New-y't Old'oo'wd-i", "+3 (123) 456-7890",
     "HELLO, ANNA! YOUR AGE IS 25. YOU LIVE IN LONDON-L'P NEW-Y'T OLD'OO'WD-I. YOUR PHONE NUMBER IS +3 (123) 456-7890.")
]


@pytest.mark.parametrize("name, age, city, phone, expected_result", data_2)
def test_show_user_info(name, age, city, phone, expected_result):
    """verify show_user_info function"""
    user2 = User(name, age, city, phone)
    assert user2.show_user_info() == expected_result
