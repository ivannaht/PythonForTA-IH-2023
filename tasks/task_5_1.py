import csv
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
    incorrect_passwords = []
    for password in passwords:
        if 6 <= len(password) <= 16:
            continue
        incorrect_passwords.append(password)
    return (f"Passwords {incorrect_passwords} are incorrect. "
            f"Password should be greater than 6 characters and less than 16 characters.")


print(check_passwords(get_passwords()))

