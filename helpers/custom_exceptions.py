class EmptyValueError(ValueError):
    """Custom exception for empty value in task 1_1"""

    def __init__(self):
        super().__init__(f"input value must not be empty")


class InsufficientAgeError(Exception):
    """Custom exception for age in task 1_1"""

    def __init__(self, age, min_age):
        super().__init__(f"{age} is insufficient age. Age must be greater than or equal {min_age} years")


class NegativeValueError(Exception):
    """Custom exception for second number in task 1_2"""
    def __init__(self, b):
        super().__init__(f"invalid number: {b}. The number should be positive")


class BigNumberError(Exception):
    """Custom exception for task 3_1"""

    def __init__(self, str_main, n):
        super().__init__(f"{n} is invalid value for n. n must be less than or equal {len(str_main)}")
