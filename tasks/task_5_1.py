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
    with open(DATA_FILE, mode="r") as file:
        csvfile = csv.reader(file)
        # skip the first row with table headers
        next(csvfile)
        passwords = [tuple(row)[1] for row in csvfile]
    return passwords


def validate_password(password):
    expected_password = r"^(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[@#$])[A-Za-z0-9@#$].{6,16}$"
    if re.search(expected_password, password):
        return True


def find_invalid_passwords(passwords):
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


def generate_new_password():
    combination = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation
    new_password = ""
    for i in range(6, 16):
        new_password += combination[secrets.randbelow(len(combination))]
    return new_password


def generate_passwords():
    random_passwords = set()
    for i in range(10):
        random_password = generate_new_password()
        random_passwords.add(random_password)
    return random_passwords


print(find_invalid_passwords(get_passwords()))
print(find_invalid_passwords(generate_passwords()))

