from helpers.custom_exceptions import NegativeValueError

input_a = float(input("Please enter the first number\n"))
input_b = float(input("Please enter the second number\n"))


def verify_arithmetic_operators(a, b):
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
    print(result)


try:
    verify_arithmetic_operators(input_a, input_b)
except ValueError as e:
    print(e)
finally:
    print("verify_arithmetic_operators() function was run")
