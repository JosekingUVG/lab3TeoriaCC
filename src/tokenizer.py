from src.types import PRECEDENCE, PRECEDENCE_REGEX

"""
def tokenizer(expression):
    ""Separa una expresión aritmética en tokens.

    expression: cadena con la expresión infija.
    Maneja números con punto decimal, operadores y paréntesis.
    Devuelve la lista de tokens.
    ""
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
"""

def tokenizer_regex(expression):
    """Separa una expresión regular infija en tokens.

    expression: cadena con la expresión regular.
    Los operadores válidos son los definidos en PRECEDENCE_REGEX,
    además de paréntesis y símbolos alfanuméricos.
    Devuelve la lista de tokens.
    """
    expresion = expression + '.#'   #Agregar un símbolo de fin de expresión para evitar errores
    tokens = []
    for char in expresion:
        if char.isspace():
            continue
        if char in PRECEDENCE_REGEX or char in "()":
            tokens.append(char)
        elif char.isalnum():
            tokens.append(char)
        elif char == '.':
            tokens.append(char) # Agregar el operador de concatenación a la lista de tokens
        elif char == '#':
            tokens.append(char) # Agregar el símbolo de fin de expresión a la lista de tokens
        else:
            raise ValueError(f"Invalid character '{char}'")
    return tokens