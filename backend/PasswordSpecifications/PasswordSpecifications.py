from dataclasses import dataclass


@dataclass
class PasswordSpecifications:

    length: int
    lowercase: bool
    uppercase: bool
    numbers: bool
    symbols: bool
    ambiguous: bool