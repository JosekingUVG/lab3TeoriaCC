"""GENERAR UN ÁRBOL DE SINTAXIS ABSTRACTA A PARTIR DE UNA EXPRESIÓN POSFIJA."""
from src.shunting_yard import regex_infix_to_postfix
from src.implements.regex import regex
from graphviz import Digraph


class SyntaxTreeNode:
    """Nodo de árbol de sintaxis abstracta."""

    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def is_leaf(self):
        return self.left is None and self.right is None


def syntax_tree_from_postfix(postfix_tokens):
    """Genera un árbol de sintaxis abstracta a partir de una expresión postfija.

    postfix_tokens: lista de tokens en notación postfija.
    Devuelve el nodo raíz del árbol de sintaxis.
    """
    stack = []

    for token in postfix_tokens:
        if token == '*':
            if len(stack) < 1:
                raise ValueError("Expresión postfija inválida para operador '*'")
            operand = stack.pop()
            stack.append(SyntaxTreeNode(token, left=operand))
        elif token in {'.', '|'}:
            if len(stack) < 2:
                raise ValueError(f"Expresión postfija inválida para operador '{token}'")
            right = stack.pop()
            left = stack.pop()
            stack.append(SyntaxTreeNode(token, left=left, right=right))
        else:
            stack.append(SyntaxTreeNode(token))

    if len(stack) != 1:
        raise ValueError("Expresión postfija inválida: quedan varios nodos en la pila")

    return stack[0]

def print_syntax_tree(root):
    """Muestra el árbol sintáctico directamente en la terminal."""

    def print_node(node, prefix="", is_left=True):
        if node is None:
            return

        # Primero mostramos el hijo derecho
        if node.right:
            print_node(
                node.right,
                prefix + ("│   " if is_left else "    "),
                False
            )

        # Mostramos el nodo actual
        print(
            prefix
            + ("└── " if is_left else "┌── ")
            + str(node.value)
        )

        # Finalmente el hijo izquierdo
        if node.left:
            print_node(
                node.left,
                prefix + ("    " if is_left else "│   "),
                True
            )

    print_node(root)



def visualize_syntax_tree(postfix_tokens, filename="syntax_tree", format="png"):
    """Visualiza el árbol de sintaxis abstracta utilizando Graphviz.

    postfix_tokens: lista de tokens en notación postfija.
    filename: nombre base del archivo de salida.
    format: formato de salida de Graphviz (png, svg, etc.).
    Devuelve el objeto Digraph generado.
    """
    root = syntax_tree_from_postfix(postfix_tokens)
    dot = Digraph(comment="Árbol de sintaxis")

    def add_node(node):
        node_id = str(id(node))
        dot.node(node_id, label=node.value)
        if node.left:
            left_id = add_node(node.left)
            dot.edge(node_id, left_id)
        if node.right:
            right_id = add_node(node.right)
            dot.edge(node_id, right_id)
        return node_id

    add_node(root)
    dot.render(filename, format=format, cleanup=True)
    return dot

