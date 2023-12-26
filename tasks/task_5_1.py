import csv
import re
import secrets
import string
from pathlib import Path


credsFile = "creds.csv"
assetsDirectory = "assets"

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_FILE = BASE_DIR.joinpath(assetsDirectory).joinpath(credsFile)


def get_passwords():
    """function for reading passwords from CSV file"""
    with open(DATA_FILE, mode="r") as file:
        reader = csv.reader(file)
        # skip the first row with table headers
        next(reader)
        passwords = [tuple(row)[1] for row in reader]

    return passwords


def set_passwords():
    """function for writing passwords in CSV file"""
    with open(DATA_FILE, mode="a") as file:
        writer = csv.writer(file)
        new_creds = generate_new_creds()
        writer.writerow(new_creds)


def validate_password(password):
    """function for password validation"""
    password_pattern = r"^(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[@#$])[A-Za-z0-9@#$].{6,16}$"
    if re.search(password_pattern, password):
        return True


def find_invalid_passwords(passwords):
    """function for finding of invalid passwords"""
    invalid_passwords = set()
    for password in passwords:
        if validate_password(password):
            continue
        invalid_passwords.add(password)

    return (f"Passwords {invalid_passwords} are invalid.\n"
            f"Password should be greater than 6 characters and less than 16 characters.\n"
            f"Password should contain at least 1 digit.\n"
            f"Password should contain at least 1 lower case letter.\n"
            f"Password should contain at least 1 upper case letter.\n"
            f"Password should contain at least 1 of $@# special character.\n")


def generate_new_creds():
    """function for generating the username and password (valid or invalid)"""
    password_combination = (string.ascii_lowercase + string.ascii_uppercase + string.digits
                            + string.punctuation.replace(",",""))
    username_combination = string.ascii_lowercase
    new_username = "user"
    new_password = ""
    for i in range(6, 16):
        new_username += username_combination[secrets.randbelow(len(username_combination))]
        new_password += password_combination[secrets.randbelow(len(password_combination))]
    new_creds = [new_username, new_password]

    return new_creds


def generate_passwords():
    """function for generating set of passwords (valid or invalid)"""
    random_passwords = set()
    for i in range(10):
        random_password = generate_new_creds()[1]
        random_passwords.add(random_password)

    return random_passwords


set_passwords()
print(find_invalid_passwords(get_passwords()))
print(find_invalid_passwords(generate_passwords()))
