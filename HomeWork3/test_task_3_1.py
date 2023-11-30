""" tests for task 3_1"""
import pytest

from HomeWork3.task_3_1 import convert


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
