"""
Ejecutar estas expresiones regulares en la terminal de Linux:
a. (a*|b*)+
b. ((s|a)|b*)*
c. (a|b)*.a.b.b.(a|b)*
d. 0?.(1?)?.0*

usando la estructura de inciso_2.py, y generar el AFD correspondiente para cada expresión regular usando un ciclo [i].
"""
import inciso_2

expressions = [
    "(a*|b*)+",
    "((s|a)|b*)*",
    "(a|b)*.a.b.b.(a|b)*",
    "0?.(1?)?.0*"
]

for i, expression in enumerate(expressions, start=1):
    print("\n")
    print("=" * 75)
    print(f"EXPRESIÓN {i}: {expression}")
    print("=" * 75)

    try:
        inciso_2.process_regex(expression, index=i)

    except Exception as e:
        print(f"Error procesando expresión {i}: {e}")

