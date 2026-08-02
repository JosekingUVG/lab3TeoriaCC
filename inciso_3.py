from src.implements.calculator import calculate

if __name__ == "__main__":
    examples = [
        "3 * 4 + 5",
        "3 + 4 * 5",
        "3 * (4 + 5)",
        "10 - 4 + 2",
        "2 * (3 + 4 * 5) + 6",
        "10 / 2 - 3",
    ]

    for expression in examples:
        postfix, result = calculate(expression)
        print(f"Infix:   {expression}")
        print(f"Postfix: {' '.join(postfix)}")
        print(f"Result: {result}")
        print("-" * 40)

    print("\nTabla de pasos para: 3 * (4 + 5)")
    calculate("3 * (4 + 5)", show_steps=True)

    print("\nEscribe una expresión (o 'exit' para terminar):")
    while True:
        expression = input(">> ")
        if expression.strip().lower() == "exit":
            break
        try:
            postfix, result = calculate(expression)
            print(f"Postfix: {' '.join(postfix)}")
            print(f"Result: {result}")
        except Exception as e:
            print(f"Error: {e}")