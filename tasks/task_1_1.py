from helpers.custom_exceptions import InsufficientAgeError, EmptyValueError


class User:

    def __init__(self, name, age, city):
        self.name = name
        self.age = age
        self.city = city

    def get_data(self):
        self.name = input("WHAT IS YOUR NAME?\n")
        self.age = input("HOW OLD ARE YOU?\n")
        self.city = input("WHERE DO YOU LIVE?\n")

    def show_user_info(self):
        min_age = 18
        if self.name == "" or self.city == "" or self.age == "":
            raise EmptyValueError
        if not self.age.isdigit():
            raise ValueError("age must be a number")
        if int(self.age) < min_age:
            raise InsufficientAgeError(self.age, min_age)
        return f"HELLO, {self.name.upper()}! YOUR AGE IS {int(self.age)}. YOU LIVE IN {self.city.upper()}."


user1 = User("Anna", "25", "London")
user2 = User("", "", "")
user2.get_data()
print(user1.show_user_info())
print(user2.show_user_info())
