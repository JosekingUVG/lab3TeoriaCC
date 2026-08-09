from src.tokenizer import  tokenizer_regex
from src.types import PRECEDENCE_REGEX, RIGHT_ASSOCIATIVE_REGEX
from src.utils import _must_unstack, is_operator, greater_or_equal_precedence

"""
def infix_to_postfix(expression, show_steps=False):
    ""Convierte una expresión aritmética infija a notación postfija.

    expression: cadena con la expresión infija.
    show_steps: si es True, imprime los pasos de la conversión.
    Devuelve una lista de tokens en notación postfija.
    ""
    tokens = tokenizer(expression)

    operator_stack = []
    postfix_output = []

    if show_steps:
        print(f"{'Symbol':<10}{'Stack':<15}{'Output'}")

    for token in tokens:
        if token.replace('.', '', 1).isdigit():
            postfix_output.append(token)

        elif token == '(':
            operator_stack.append(token)

        elif token == ')':
            while operator_stack and operator_stack[-1] != '(':
                postfix_output.append(operator_stack.pop())
            if not operator_stack:
                raise ValueError("Unbalanced parentheses")
            operator_stack.pop()

        elif is_operator(token):
            while (operator_stack
                   and operator_stack[-1] != '('
                   and greater_or_equal_precedence(token, operator_stack[-1])):
                postfix_output.append(operator_stack.pop())
            operator_stack.append(token)

        else:
            raise ValueError(f"Token not recognized: '{token}'")

        if show_steps:
            print(f"{token:<10}{' '.join(operator_stack):<15}{' '.join(postfix_output)}")

    while operator_stack:
        top = operator_stack.pop()
        if top == '(':
            raise ValueError("Unbalanced parentheses")
        postfix_output.append(top)

    if show_steps:
        print(f"{'':<10}{'':<15}{' '.join(postfix_output)}")

    return postfix_output
"""

def regex_infix_to_postfix(expression, show_steps=False):
    """Convierte una expresión regular infija a notación postfija.

    expression: cadena con la expresión regular infija.
    show_steps: si es True, imprime los pasos de la conversión.
    Devuelve una lista de tokens en notación postfija.
    """
    tokens = tokenizer_regex(expression)

    operator_stack = []
    postfix_output = []

    if show_steps:
        print(f"{'Symbol':<10}{'Stack':<15}{'Output'}")

    for token in tokens:
        if token == '(':
            operator_stack.append(token)

        elif token == ')':
            while operator_stack and operator_stack[-1] != '(':
                postfix_output.append(operator_stack.pop())
            if not operator_stack:
                raise ValueError("Unbalanced parentheses")
            operator_stack.pop()

        elif token in PRECEDENCE_REGEX:
            while (operator_stack
                   and operator_stack[-1] != '('
                   and operator_stack[-1] in PRECEDENCE_REGEX
                   and _must_unstack(token, operator_stack[-1],
                                     PRECEDENCE_REGEX, RIGHT_ASSOCIATIVE_REGEX)):
                postfix_output.append(operator_stack.pop())
            operator_stack.append(token)

        else:
            postfix_output.append(token)

        if show_steps:
            print(f"{token:<10}{' '.join(operator_stack):<15}{' '.join(postfix_output)}")

    while operator_stack:
        top = operator_stack.pop()
        if top == '(':
            raise ValueError("Unbalanced parentheses")
        postfix_output.append(top)

    if show_steps:
        print(f"{'':<10}{'':<15}{' '.join(postfix_output)}")

    return postfix_output