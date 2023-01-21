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
