from src.types import PRECEDENCE
from src.types import RIGHT_ASSOCIATIVE


def is_operator(token):
    """Determina si un token es un operador aritmético válido."""
    return token in PRECEDENCE

# rules 5 and 6
def greater_or_equal_precedence(incoming_operator, stack_operator):
    """Comprueba si el operador en la pila tiene mayor o igual precedencia.

    Se usa para decidir si se deben desapilar operadores durante la conversión.
    """
    incoming_precedence = PRECEDENCE[incoming_operator]
    stack_precedence = PRECEDENCE[stack_operator]

    if stack_precedence > incoming_precedence:
        return True
    if stack_precedence == incoming_precedence and incoming_operator not in RIGHT_ASSOCIATIVE:
        return True
    return False


def _must_unstack(incoming_operator, stack_operator, precedence, right_associative):
    """Determina si se deben desapilar operadores en una expresión regular.

    incoming_operator: operador actual en el recorrido.
    stack_operator: operador en la cima de la pila.
    precedence: diccionario de precedencias.
    right_associative: conjunto de operadores asociativos a la derecha.
    """
    incoming_precedence = precedence[incoming_operator]
    stack_precedence = precedence[stack_operator]

    if stack_precedence > incoming_precedence:
        return True
    if stack_precedence == incoming_precedence and incoming_operator not in right_associative:
        return True
    return False