#from src.types import _OPERATOR_DESCRIPTION
from src.shunting_yard import regex_infix_to_postfix
from src.types import _OPERATOR_DESCRIPTION



def read_postfix_right_to_left(postfix_tokens, print_messages=True):
    """Lee una expresión postfija de derecha a izquierda y genera mensajes.

    postfix_tokens: lista de tokens en notación postfija.
    print_messages: si es True, imprime cada mensaje numerado.
    Devuelve la lista de mensajes generados.
    """
    n = len(postfix_tokens)
    messages = []

    for i, token in enumerate(reversed(postfix_tokens)):
        if token in _OPERATOR_DESCRIPTION:
            message = _OPERATOR_DESCRIPTION[token]
        else:
            is_last = (i == n - 1)
            message = token if is_last else f"{token} of"

        messages.append(message)
        if print_messages:
            print(f"{i + 1}. {message}")

    return messages


def regex(regular_expression, show_steps=False):
    """Convierte una expresión regular a postfijo y la explica.

    regular_expression: cadena con la expresión regular infija.
    show_steps: si es True, muestra los pasos de conversión a postfija.
    Devuelve la lista de tokens en notación postfija.
    """
    postfix = regex_infix_to_postfix(regular_expression, show_steps)
    print(f"\nRegular expression: {regular_expression}")
    print(f"In postfix:         {''.join(postfix)}")

    return postfix

def regex_with_explanation(regular_expression):
    """Convierte una expresión regular a postfijo y la explica paso a paso.

    regular_expression: cadena con la expresión regular infija.
    Devuelve la lista de tokens en notación postfija.
    """
    postfix = regex_infix_to_postfix(regular_expression, show_steps=True)
    print(f"\nRegular expression: {regular_expression}")
    print(f"In postfix:         {''.join(postfix)}")

    print("\nReading postfix from right to left:")
    read_postfix_right_to_left(postfix, print_messages=True)

    return postfix