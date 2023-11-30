""" tests for task 3_1"""
import pytest

from HomeWork3.task_3_1 import convert


@pytest.mark.parametrize("input_value1, input_value2, output_value", [
                        ("123456987654", 6, "234561876549"),
                        ("123456987653", 6, "234561356789")
                         ])
def test_convert(input_value1, input_value2, output_value):
    """verify convert function"""
    assert convert(input_value1, input_value2) == output_value