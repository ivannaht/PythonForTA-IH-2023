"""Module for User class"""
from helpers.custom_exceptions import InsufficientAgeError, EmptyValueError


class User:
    """Class for user"""

    def __init__(self, name, age, city):
        """Constructor for user"""
        self.name = name
        self.age = age
        self.city = city

    def get_data(self):
        """Method for getting user data from input"""
        self.name = input("WHAT IS YOUR NAME?\n")
        self.age = input("HOW OLD ARE YOU?\n")
        self.city = input("WHERE DO YOU LIVE?\n")

    def show_user_info(self):
        """Method for showing formatted user info"""
        min_age = 18
        if self.name == "" or self.city == "" or self.age == "":
            raise EmptyValueError
        if not self.age.isdigit():
            raise ValueError("age must be a number")
        if int(self.age) < min_age:
            raise InsufficientAgeError(self.age, min_age)
        return f"HELLO, {self.name.upper()}! YOUR AGE IS {int(self.age)}. YOU LIVE IN {self.city.upper()}."


user1 = User("Anna", "25", "London")
print(user1.show_user_info())

user2 = User("", "", "")
user2.get_data()
print(user2.show_user_info())
