from helpers.custom_exceptions import NegativeValueError

input_a = float(input("Please enter the first number\n"))
input_b = float(input("Please enter the second number\n"))


def decorator_with_arguments(outer_message, start_message, finish_message):
    def decorator(fun):
        print(outer_message)

        def wrapper_accepting_arguments(a, b):
            print(start_message)
            print(f"The arguments are: {a}, {b}")
            print(fun(a, b))
            print(finish_message)

        return wrapper_accepting_arguments

    return decorator


@decorator_with_arguments("decorator for function verify_arithmetic_operators",
                          "started", "finished")
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
    return result


try:
    verify_arithmetic_operators(input_a, input_b)
except ValueError as e:
    print(e)
