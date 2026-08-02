from src.evals.postfix import eval_postfix
from src.shunting_yard import infix_to_postfix


def calculate(expression, show_steps=False):
    postfix = infix_to_postfix(expression, show_steps)
    result = eval_postfix(postfix)
    return postfix, result