def verify_arithmetic_operators():
    a = float(input("Please enter the first number\n"))
    b = float(input("Please enter the second number\n"))
    if b < 0:
        raise ValueError("the second number should be positive")
    if b == 0:
        raise ValueError("the second number should not be zero")
    result = (f"a + b = {a + b}\n"
              f"a - b = {a - b}\n"
              f"a * b = {a * b}\n"
              f"a / b = {a / b}\n"
              f"a ** b = {a ** b}\n"
              f"a // b = {a // b}\n"
              f"a % b = {a % b}\n")
    print(result)


try:
    verify_arithmetic_operators()
except ValueError as e:
    print(e)
finally:
    print("verify_arithmetic_operators() function was run")

