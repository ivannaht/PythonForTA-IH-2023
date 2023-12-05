from helpers.custom_exceptions import InsufficientAgeError, EmptyValueError

input_name = input("WHAT IS YOUR NAME?\n")
input_age = input("HOW OLD ARE YOU?\n")
input_city = input("WHERE DO YOU LIVE?\n")


def show_user_info(name, age, city):
    min_age = 18

    if name == "" or city == "" or age == "":
        raise EmptyValueError

    if not age.isdigit():
        raise ValueError("age must be a number")

    if int(age) < min_age:
        raise InsufficientAgeError(age, min_age)

    user_info = (f"HELLO, {name.upper()}! YOUR AGE IS {int(age)}. YOU LIVE IN {city.upper()}.")

    return user_info


print(show_user_info(input_name, input_age, input_city))
