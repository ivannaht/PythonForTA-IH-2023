from helpers.custom_exceptions import NegativeValueError
from helpers.logger import logger_with_arguments


@logger_with_arguments("logger for function",
                       "started", "finished")
def verify_arithmetic_operators(a, b):
    """function for verifying arithmetic operators"""
    if b < 0:
        raise NegativeValueError(b)
    if b == 0:
        raise ZeroDivisionError("the second number should not be zero")
    result = (f"a + b = {a + b}\n"
              f"a - b = {a - b}\n"
              f"a * b = {a * b}\n"
              f"a / b = {a / b}\n"
              f"a ** b = {a ** b}\n"
              f"a // b = {a // b}\n"
              f"a % b = {a % b}\n")
    return result


def show_user_arithmetic_operators():
    """function for verifying arithmetic operators from user input"""
    input_a = float(input("Please enter the first number\n"))
    input_b = float(input("Please enter the second number\n"))
    try:
        verify_arithmetic_operators(input_a, input_b)
    except NegativeValueError as e:
        print(e)
    except ZeroDivisionError as e:
        print(e)


# show_user_arithmetic_operators()
