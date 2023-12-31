import re
import secrets
import string
from tasks.csv_file_editor import CsvFileEditor


class CredsFileEditor(CsvFileEditor):
    """Child class for reading and modifying creds.csv file """

    def __init__(self, csv_file, directory):
        """Constructor for creds.csv file"""
        super(self.__class__, self).__init__(csv_file, directory)
        self.passwords = self.get_passwords

    @property
    def get_passwords(self):
        """function for reading passwords from creds.csv file"""
        passwords = []
        for creds in self.data:
            password = creds[1]
            passwords.append(password)

        return passwords

    @staticmethod
    def validate_password(password):
        """function for password validation"""
        password_pattern = r"^(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[@#$])[A-Za-z0-9@#$].{6,16}$"
        if re.search(password_pattern, password):
            return True

    def find_invalid_passwords(self):
        """function for finding of invalid passwords in creds.csv file"""
        invalid_passwords = set()
        for password in self.passwords:
            if self.validate_password(password):
                continue
            invalid_passwords.add(password)

        return (f"Passwords {invalid_passwords} are invalid.\n"
                f"Password should be greater than 6 characters and less than 16 characters.\n"
                f"Password should contain at least 1 digit, 1 lower case letter, 1 upper case letter, "
                f"1 of $@# special character.\n")

    def find_valid_passwords(self):
        """function for finding of valid passwords in creds.csv file"""
        valid_passwords = set()
        for password in self.passwords:
            if self.validate_password(password):
               valid_passwords.add(password)

        return f"Passwords {valid_passwords} are valid.\n"

    def generate_new_data(self):
        """function for generating the username and password (valid or invalid)"""
        password_combination = (string.ascii_lowercase + string.ascii_uppercase + string.digits
                                + "@#$")
        username_combination = string.ascii_lowercase
        new_username = "user"
        new_password = ""
        for i in range(6, 16):
            new_username += username_combination[secrets.randbelow(len(username_combination))]
            new_password += password_combination[secrets.randbelow(len(password_combination))]
        new_creds = [new_username, new_password]

        return new_creds


file_creds = CredsFileEditor("creds.csv", "assets")
print(file_creds.generate_new_data())
file_creds.add_data()
print(file_creds.data)
print(len(file_creds.data))
print(file_creds.passwords)
print(file_creds.find_invalid_passwords())
print(file_creds.find_valid_passwords())
