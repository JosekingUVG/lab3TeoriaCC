"""Generar un AFD a partir de una expresión regular."""

from src.implements.regex import regex
from src.implements.syntax_three import (
    print_syntax_tree,
    visualize_syntax_tree,
    syntax_tree_from_postfix
)
from src.implements.afd_operations import (
    build_afd,
    visualize_afd
)


def process_regex(expression, index=None):
    """Procesa una expresión regular y genera su árbol y AFD."""

    
    postfix = regex(expression)

    print(f"\nPostfix notation: {''.join(postfix)}")

    # Construir árbol
    print("\n" + "=" * 55)
    print("Conversión a árbol de sintaxis abstracta")
    print("=" * 55)

    root = syntax_tree_from_postfix(postfix)

    print_syntax_tree(root)

    # Elegir nombres de archivos
    if index is None:
        tree_filename = "syntax_tree"
        afd_filename = "afd"
    else:
        tree_filename = f"syntax_tree{index}"
        afd_filename = f"afd{index}"

    # Guardar árbol
    visualize_syntax_tree(
        postfix,
        filename=tree_filename,
        format="png"
    )

    print(
        f"\nÁrbol generado y guardado como "
        f"'{tree_filename}.png'."
    )

    # Construir AFD
    afd = build_afd(root)

    # Guardar AFD
    visualize_afd(
        afd,
        filename=afd_filename,
        format="png"
    )

    print(
        f"AFD generado y guardado como "
        f"'{afd_filename}.png'."
    )

    return afd


if __name__ == "__main__":
    print("\n" + "=" * 75)
    print("Creación de AFD a partir de una expresión regular")
    print("=" * 75)

    while True:
        print("\nEscribe una expresión aritmética o regular (o 'salir'):")
        print("  - Regular:    usa letras y . | * ( )       ej: (a|b)*.a.b.b")
        expression = input("\n>> ")

        if expression.strip().lower() == "salir":
            break

        try:
            process_regex(expression)

        except Exception as e:
            print(f"Error: {e}")