from random import randint
from PasswordSpecifications import PasswordSpecifications


class PasswordGenerator:
    lowercase: str = "abcdefghijklmnopqrstuvwxyz"
    uppercase: str = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    numbers: str = "0123456789"
    symbols: str = "!@#$%^&*()_+-=[]{};:,./<>?"
    ambiguous: str = "lIO01"

    def generate(self, password_specifications: PasswordSpecifications) -> str:

        password: str
        included_chars: list[str] = []

        if password_specifications.lowercase:
            included_chars.append(self.lowercase)
        if password_specifications.uppercase:
            included_chars.append(self.uppercase)
        if password_specifications.numbers:
            included_chars.append(self.numbers)
        if password_specifications.symbols:
            included_chars.append(self.symbols)

        while True:
            password = self.__generate_password(password_specifications, included_chars)

            if self.__check_password(password_specifications, password):
                break

        return password

    @staticmethod
    def __generate_password(password_specifications: PasswordSpecifications, included_chars: list[str]) -> str:

        password: str = ""

        for i in range(password_specifications.length):
            char_category: int = randint(0, len(included_chars) - 1)
            char_index: int = randint(0, len(included_chars[char_category]) - 1)
            password += included_chars[char_category][char_index]

        return password

    def __check_password(self, password_specifications: PasswordSpecifications, password: str) -> bool:

        if password_specifications.ambiguous:
            for char in password:
                if char in self.ambiguous:
                    return False

        if password_specifications.numbers:
            if len([char for char in password if char in self.numbers]) < password_specifications.min_numbers:
                return False

        if password_specifications.symbols:
            if len([char for char in password if char in self.symbols]) < password_specifications.min_symbols:
                return False

        return True
