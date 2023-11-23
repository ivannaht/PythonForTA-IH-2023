""" tests for task 1_3"""
from HomeWork1.task_1_3 import to_minutes, to_hours, is_whole_div


def test_to_minutes():
    """verify to_minutes function"""
    assert to_minutes(1.5) == 90.0


def test_to_hours_case1():
    """verify to_hours function case 1"""
    assert to_hours(12) == 0.2


def test_to_hours_case2():
    """verify to_hours function case 2"""
    assert to_hours(5) == 0.0833


def test_is_whole_div_case1():
    """verify is_whole_div function case 1"""
    assert is_whole_div(2, 3) is False


def test_is_whole_div_case2():
    """verify is_whole_div function case 2"""
    assert is_whole_div(12, 3) is True
