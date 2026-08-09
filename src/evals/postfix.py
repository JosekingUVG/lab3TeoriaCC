from src.utils import is_operator


def eval_postfix(tokens_postfijos):
    """Evalúa una expresión en notación postfija.

    tokens_postfijos: lista de tokens en notación postfija.
    Devuelve el resultado numérico de la evaluación.
    """
    pila = []
 
    for token in tokens_postfijos:
        if is_operator(token):
            if len(pila) < 2:
                raise ValueError("Expresión postfija inválida")
            b = pila.pop()
            a = pila.pop()
            if token == '+':
                pila.append(a + b)
            elif token == '-':
                pila.append(a - b)
            elif token == '*':
                pila.append(a * b)
            elif token == '/':
                if b == 0:
                    raise ZeroDivisionError("División por cero")
                pila.append(a / b)
        else:
            pila.append(float(token))
 
    if len(pila) != 1:
        raise ValueError("Expresión postfija inválida")
 
    return pila[0]