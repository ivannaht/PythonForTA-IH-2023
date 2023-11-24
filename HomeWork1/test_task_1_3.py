""" tests for task 1_3"""
import pytest

from HomeWork1.task_1_3 import to_minutes, to_hours, is_whole_div


@pytest.mark.parametrize("input_value, output_value", [(1.5, 90.0), (0.01, 0.6), (0, 0)])
def test_to_minutes(input_value, output_value):
    """verify to_minutes function"""
    assert to_minutes(input_value) == output_value


@pytest.mark.parametrize("input_value, output_value", [(12, 0.2), (5, 0.0833), (0, 0)])
def test_to_hours(input_value, output_value):
    """verify to_hours function"""
    assert to_hours(input_value) == output_value


@pytest.mark.parametrize("input_value1, input_value2, output_value", [(2, 3, False), (12, 3, True), (-22, -2, True)])
def test_is_whole_div_case1(input_value1, input_value2, output_value):
    """verify is_whole_div function"""
    assert is_whole_div(input_value1, input_value2) is output_value
