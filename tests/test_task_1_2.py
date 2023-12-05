import pytest

from helpers.custom_exceptions import NegativeValueError
from tasks.task_1_2 import verify_arithmetic_operators

data = [
    (5, 0, ZeroDivisionError),
    (5, -5, NegativeValueError),
]


@pytest.mark.parametrize("a, b, e", data)
def test_arithmetic_operators_with_exceptions(a, b, e):
    """verify_arithmetic_operators function"""
    with pytest.raises(e):
        verify_arithmetic_operators(a, b)
