from src.types import _OPERATOR_DESCRIPTION
from src.shunting_yard import regex_infix_to_postfix


def read_postfix_right_to_left(postfix_tokens, print_messages=True):
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
    """
    Convenience function: converts the regular expression to postfix
    and then explains it by reading it from right to left.
    """
    postfix = regex_infix_to_postfix(regular_expression, show_steps)
    print(f"\nRegular expression: {regular_expression}")
    print(f"In postfix:         {''.join(postfix)}")
    print("Reading from right to left:")
    read_postfix_right_to_left(postfix)
    return postfix