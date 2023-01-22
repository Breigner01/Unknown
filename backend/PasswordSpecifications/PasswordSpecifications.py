from dataclasses import dataclass


@dataclass
class PasswordSpecifications:
    length: int
    lowercase: bool
    uppercase: bool
    numbers: bool
    symbols: bool
    min_numbers: int
    min_symbols: int
    ambiguous: bool

    def __init__(self):
        self.length = 1
        self.lowercase = True
        self.uppercase = True
        self.numbers = True
        self.symbols = True
        self.min_numbers = 1
        self.min_symbols = 1
        self.ambiguous = True

    def __init__(self, length: int, lowercase: bool, uppercase: bool, numbers: bool, symbols: bool, min_numbers: int, min_symbols: int, ambiguous: bool):
        self.length = length
        self.lowercase = lowercase
        self.uppercase = uppercase
        self.numbers = numbers
        self.symbols = symbols
        self.min_numbers = min_numbers
        self.min_symbols = min_symbols
        self.ambiguous = ambiguous
