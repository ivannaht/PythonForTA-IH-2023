""" tests for task 3_1"""
import pytest

from helpers.custom_exceptions import BigNumberError
from tasks.task_3_1 import convert


@pytest.mark.parametrize("input_value1, input_value2, output_value", [
                        ("123456987654", 6, "234561876549"),
                        ("123456987653", 6, "234561356789"),
                        ("66443875", 4, "44668753"),
                        ("66443875", 8, "64438756"),
                        ("66443876 9", 8, "67834466"),
                        ("123456779", 8, "23456771"),
                        ("", 8, ""),
                        ("123456779", 0, ""),
                        ("563000655734469485", 4, "0365065073456944")
])
def test_convert(input_value1, input_value2, output_value):
    """verify convert function"""
    assert convert(input_value1, input_value2) == output_value


data = [
        ("1all23", 5, ValueError),
        ("1.56.37.5", 3, ValueError),
        ("-12", 3, ValueError),
        ("123456", 'a', TypeError),
        ("123456", 1.5, TypeError),
        ("123", 1000, BigNumberError)
]


@pytest.mark.parametrize("str_main, n, e", data)
def test_convert_with_exceptions(str_main, n, e):
    """verify convert function"""
    with pytest.raises(e):
        assert convert(str_main, n)
