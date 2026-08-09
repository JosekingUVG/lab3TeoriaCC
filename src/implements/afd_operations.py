# Este archivo contiene las funciones necesarias para calcular nullable, firstpos, lastpos y followpos de un árbol de sintaxis abstracta.
from src.implements.syntax_three import SyntaxTreeNode

def iterate_leaves(node):
    if node is None:
        return

    if node.is_leaf():
        yield node
        return

    yield from iterate_leaves(node.left)
    yield from iterate_leaves(node.right)

def assign_leaf_positions(root):
    """Numera las hojas del árbol en orden de izquierda a derecha.

    Se asigna `position` solo a las hojas que no son `ε`.
    """
    next_position = 1

    def visit(node):
        nonlocal next_position
        if node is None:
            return

        visit(node.left)
        visit(node.right)

        if node.is_leaf():
            if node.value == 'ε':
                node.position = None
            else:
                node.position = next_position
                next_position += 1

    visit(root)
    return next_position - 1


def compute_functions(node):
    """Calcula nullable, firstpos y lastpos para todo el árbol."""

    if node is None:
        return

    if node.is_leaf():
        if node.value == 'ε':
            node.nullable = True
            node.firstpos = set()
            node.lastpos = set()
        else:
            node.nullable = False
            node.firstpos = {node.position}
            node.lastpos = {node.position}
        return

    compute_functions(node.left)
    compute_functions(node.right)

    if node.value == '|':
        node.nullable = (
            node.left.nullable
            or node.right.nullable
        )

        node.firstpos = (
            node.left.firstpos
            | node.right.firstpos
        )

        node.lastpos = (
            node.left.lastpos
            | node.right.lastpos
        )

    elif node.value == '.':
        node.nullable = (
            node.left.nullable
            and node.right.nullable
        )

        if node.left.nullable:
            node.firstpos = (
                node.left.firstpos
                | node.right.firstpos
            )
        else:
            node.firstpos = set(node.left.firstpos)

        if node.right.nullable:
            node.lastpos = (
                node.left.lastpos
                | node.right.lastpos
            )
        else:
            node.lastpos = set(node.right.lastpos)

    elif node.value == '*':
        node.nullable = True
        node.firstpos = set(node.left.firstpos)
        node.lastpos = set(node.left.lastpos)

def compute_followpos(root):
    """Calcula followpos para todas las posiciones del árbol."""

    assign_leaf_positions(root)
    compute_functions(root)

    positions = [
        node.position
        for node in iterate_leaves(root)
        if node.position is not None
    ]

    followpos = {
        position: set()
        for position in positions
    }

    def visit(node):
        if node is None:
            return

        visit(node.left)
        visit(node.right)

        if node.value == '.':
            for position in node.left.lastpos:
                followpos[position].update(
                    node.right.firstpos
                )

        elif node.value == '*':
            for position in node.left.lastpos:
                followpos[position].update(
                    node.left.firstpos
                )

    visit(root)

    return followpos


def build_afd(root):
    """Construye directamente el AFD a partir del árbol sintáctico."""

    # Preparar árbol
    assign_leaf_positions(root)
    compute_functions(root)

    # Obtener followpos
    follow = compute_followpos(root)

    # posición -> símbolo
    position_symbols = {
        node.position: node.value
        for node in iterate_leaves(root)
        if node.position is not None
    }

    # Alfabeto, sin #
    alphabet = {
        symbol
        for symbol in position_symbols.values()
        if symbol != '#'
    }

    # Estado inicial
    initial_state = frozenset(root.firstpos)

    states = [initial_state]
    pending = [initial_state]

    transitions = {}

    while pending:
        state = pending.pop(0)

        transitions[state] = {}

        for symbol in alphabet:
            next_state = set()

            for position in state:

                if position_symbols[position] == symbol:
                    next_state.update(
                        follow[position]
                    )

            next_state = frozenset(next_state)

            if next_state:
                transitions[state][symbol] = next_state

                if next_state not in states:
                    states.append(next_state)
                    pending.append(next_state)

    # Encontrar posición de #
    final_position = next(
        position
        for position, symbol in position_symbols.items()
        if symbol == '#'
    )

    final_states = {
        state
        for state in states
        if final_position in state
    }

    return {
        "states": states,
        "initial": initial_state,
        "finals": final_states,
        "transitions": transitions,
        "positions": position_symbols,
        "followpos": follow,
    }

# visualizar el AFD
def visualize_afd(afd, filename="afd", format="png"):
    from graphviz import Digraph

    dot = Digraph(comment="AFD")
    dot.attr(rankdir="LR")

    states = afd["states"]
    initial = afd["initial"]
    finals = afd["finals"]
    transitions = afd["transitions"]

    # Crear nodos
    for state in states:

        label = "{" + ",".join(
            str(x) for x in sorted(state)
        ) + "}"

        shape = (
            "doublecircle"
            if state in finals
            else "circle"
        )

        dot.node(
            str(state),
            label=label,
            shape=shape
        )

    # Flecha inicial
    dot.node("start", shape="point")
    dot.edge("start", str(initial))

    # Transiciones
    for state, state_transitions in transitions.items():

        for symbol, target in state_transitions.items():

            dot.edge(
                str(state),
                str(target),
                label=symbol
            )

    dot.render(
        filename,
        format=format,
        cleanup=True
    )

    return dot
