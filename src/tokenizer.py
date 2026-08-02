from src.types import PRECEDENCE, PRECEDENCE_REGEX


def tokenizer(expression):
    tokens = []
    current_number = ""

    for char in expression:
        if char.isspace():
            if current_number:
                tokens.append(current_number)
                current_number = ""
            continue

        if char.isdigit() or char == '.':
            current_number += char
        else:
            if current_number:
                tokens.append(current_number)
                current_number = ""
            if char in PRECEDENCE or char in "()":
                tokens.append(char)
            else:
                raise ValueError(f"Invalid character '{char}'")

    if current_number:
        tokens.append(current_number)

    return tokens


def tokenizer_regex(expression):
    tokens = []
    for char in expression:
        if char.isspace():
            continue
        if char in PRECEDENCE_REGEX or char in "()":
            tokens.append(char)
        elif char.isalnum():
            tokens.append(char)
        else:
            raise ValueError(f"Invalid character '{char}'")
    return tokens