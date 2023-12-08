import csv
import re
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


def check_passwords(passwords):
    incorrect_passwords = set()
    for password in passwords:
        if (6 <= len(password) <= 16 and
                re.search(r'\d+', password) and
                re.search(r'[a-z]+', password) and
                re.search(r'[A-Z]+', password) and
                re.search(r'\W+', password) and not
                re.search(r'\s+', password)):
            continue
        incorrect_passwords.add(password)

    return (f"Passwords {incorrect_passwords} are incorrect.\n"
            f"Password should be greater than 6 characters and less than 16 characters.\n"
            f"Password should contain at least 1 digit.\n"
            f"Password should contain at least 1 lower case letter.\n"
            f"Password should contain at least 1 upper case letter.\n"
            f"Password should contain at least 1 special character.\n")


print(check_passwords(get_passwords()))
