"""Module for User class"""
import re

from helpers.custom_exceptions import InsufficientAgeError, EmptyValueError


class User:
    """Class for user"""

    def __init__(self, name, age, city, phone="+1 (000) 000-0000"):
        """Constructor for user"""
        self.validate_user_info(name, age, city, phone)
        self.name = name
        self.age = age
        self.city = city
        self.phone = phone

    def input_user_data(self):
        """Method for getting user data from input"""
        self.name = input("WHAT IS YOUR NAME?\n")
        self.age = input("HOW OLD ARE YOU?\n")
        self.city = input("WHERE DO YOU LIVE?\n")
        self.phone = input("WHAT IS YOUR PHONE NUMBER?\n")

    @staticmethod
    def validate_user_info(name, age, city, phone):
        """validate user info using regular expressions"""
        min_age = 18
        name_city_pattern = re.compile(r"^([a-z]+)([-'][a-z]+)*(\-[a-z]+)?(( [a-z]+)?([-'][a-z]+)*){0,3}[a-z]*$", re.IGNORECASE)
        phone_pattern = re.compile(r"^\+\d{1,3}[-\s]?\(?\d{1,3}\)?[-\s]?\d{1,3}?[-\s]?\d{1,4}$")
        if name == "" or city == "" or age == "":
            raise EmptyValueError
        if not name_city_pattern.search(name):
            raise ValueError("name must include only letters, spaces, apostrophes, or hyphens")
        if not name_city_pattern.search(city):
            raise ValueError("city must include only letters, spaces, apostrophes, or hyphens")
        if not phone_pattern.search(phone):
            raise ValueError("phone number can include plus sign, 11 digits, brackets, spaces, hyphens")
        if not age.isdigit():
            raise ValueError("age must be a number")
        if int(age) < min_age:
            raise InsufficientAgeError(age, min_age)

    def show_user_info(self):
        """Method for showing formatted user info"""

        return (f"HELLO, {self.name.upper()}! "
                f"YOUR AGE IS {int(self.age)}. "
                f"YOU LIVE IN {self.city.upper()}. "
                f"YOUR PHONE NUMBER IS {self.phone}.")


user1 = User("Anna", "25", "London", "+1(012)3456789")
print(user1.show_user_info())

user2 = User("a", "18", "b")
# user2.input_user_data()
print(user2.show_user_info())
