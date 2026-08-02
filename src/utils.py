from src.types import PRECEDENCE
from src.types import RIGHT_ASSOCIATIVE


def is_operator(token):
    return token in PRECEDENCE

# rules 5 and 6
def greater_or_equal_precedence(incoming_operator, stack_operator):
    incoming_precedence = PRECEDENCE[incoming_operator]
    stack_precedence = PRECEDENCE[stack_operator]

    if stack_precedence > incoming_precedence:
        return True
    if stack_precedence == incoming_precedence and incoming_operator not in RIGHT_ASSOCIATIVE:
        return True
    return False


def _must_unstack(incoming_operator, stack_operator, precedence, right_associative):
    incoming_precedence = precedence[incoming_operator]
    stack_precedence = precedence[stack_operator]

    if stack_precedence > incoming_precedence:
        return True
    if stack_precedence == incoming_precedence and incoming_operator not in right_associative:
        return True
    return False