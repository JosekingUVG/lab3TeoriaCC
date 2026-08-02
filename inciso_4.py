from src.implements.calculator import calculate
from src.implements.regex import regex

if __name__ == "__main__":
    print("\n" + "=" * 55)
    print("EXTENSIÓN: Shunting Yard para expresiones regulares")
    print("=" * 55)

    regex("(a|b)*.a.b.b")

    print("\nEscribe una expresión aritmética o regular (o 'exit'):")
    print("  - Regular:    usa letras y . | * ( )       ej: (a|b)*.a.b.b")
    while True:
        expression = input(">> ")
        if expression.strip().lower() == "salir":
            break
        try:
            regex(expression)
        except Exception as e:
            print(f"Error: {e}")
 