"""GENERAR UN ARBOL DE SINTAXIS ABSTRACTA A PARTIR DE UNA EXPRESIÓN REGULAR"""
from src.implements.regex import regex
from src.implements.syntax_three import print_syntax_tree, visualize_syntax_tree, syntax_tree_from_postfix
import sys

if __name__ == "__main__":
    print("\n" + "=" * 75)
    print("Creación de un Árbol de Sintaxis Abstracta a partir de una expresión regular")
    print("=" * 75)

    print("\nEscribe una expresión aritmética o regular (o 'salir'):")
    print("  - Regular:    usa letras y . | * ( )       ej: (a|b)*.a.b.b")
    while True:
        expression = input(">> ")
        if expression.strip().lower() == "salir":
            break
        try:
            postfix = regex(expression)
            print(f"\nPostfix notation: {''.join(postfix)}")

            # convertir la expresión postfija a un árbol de sintaxis abstracta
            print("\n" + "=" * 55)
            print("Conversión a árbol de sintaxis abstracta")
            print("=" * 55)

            
            root = syntax_tree_from_postfix(postfix)
            print_syntax_tree(root)
            
            visualize_syntax_tree(postfix, filename="syntax_tree", format="png")

            print("\nÁrbol de sintaxis abstracta generado y guardado como 'syntax_tree.png'.")
            print("*"* 55)

        except Exception as e:
            print(f"Error: {e}")

    



 