""" tests for task 2_1"""
import pytest

from HomeWork2.task_2_1 import stat


@pytest.mark.parametrize("input_value, output_value",
                         [
                             ([1, 9, 9, 9, 9, 9, 9, 2, 2, 2, 2, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5, 5, 6, 7, 8], [29, 9, 4, [9, 2, 5], 6]),
                             ([-1, 0, 1], [3, 3, 3, [-1, 0, 1], 1])
                         ])
def test_stat(input_value, output_value):
    """verify stat function"""
    assert stat(input_value) == output_value

