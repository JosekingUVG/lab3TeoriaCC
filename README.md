# Laboratorio 2 - CC2019

## Ejecución

- Instalacion de uv en terminal

```powershell
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

- Activación del entorno virtual

```bash
uv venv
.venv/Scripts/activate.bat
```

- Ejecucion del inciso 3

```bash
python inciso_3.py
```

- Ejecucion del inciso 4

```bash
python inciso_4.py
```


## Descripción general

Implementacion del algoritmo de Shunting Yard para convertir expresiones desde notación infix a notación postfix y, luego, evaluarlas. La idea central es transformar una expresión como `3 * (4 + 5)` en una forma equivalente más fácil de procesar por una máquina, por ejemplo `3 4 5 + *`.

El algoritmo usa una pila para organizar operadores mientras se recorre la expresión de izquierda a derecha. Gracias a esta estructura, se preservan las reglas de precedencia y asociatividad sin necesidad de usar recursión ni evaluar la expresión de forma ambigua.

## Cómo funciona el algoritmo

El proceso se realiza en tres etapas principales:

1. Tokenización
   - La entrada se separa en tokens, como números, operadores y paréntesis.
   - En este proyecto, la tokenización se realiza en el módulo de tokenización para preparar la expresión para el algoritmo.

2. Conversión de infix a postfix
   - Se recorre la expresión de izquierda a derecha.
   - Si el token es un operando, se envía directamente a la salida.
   - Si es un paréntesis de apertura, se apila.
   - Si es un paréntesis de cierre, se desapilan los operadores hasta encontrar el paréntesis de apertura.
   - Si es un operador, se comparan sus prioridades con las del operador que está en la cima de la pila.
   - Cuando el operador entrante tiene mayor precedencia, o igual precedencia y corresponde a una operación asociativa por la derecha, se apila.
   - Si tiene menor precedencia, o igual precedencia pero es asociativa por la izquierda, se desapilan operadores hasta que sea posible apilar el nuevo operador.
   - Al finalizar, se vacía la pila de operadores y se agregan al resultado final.

3. Evaluación de la expresión postfix
   - Una vez obtenida la notación postfix, se recorre nuevamente para evaluar la expresión.
   - Cada vez que aparece un operador, se toman los dos valores más recientes de la pila, se aplica la operación y el resultado se vuelve a apilar.
   - Al final queda un único valor, que es el resultado de la expresión original.

## Aplicación en el inciso 3

El inciso 3 se enfoca en expresiones aritméticas. El flujo es el siguiente:

- Se recibe una expresión como `3 * (4 + 5)`.
- El algoritmo la convierte a notación postfix.
- Luego se evalúa esa versión postfix para obtener el resultado.

Ejemplo:

- Expresión infix: `3 * (4 + 5)`
- Expresión postfix: `3 4 5 + *`
- Resultado: `27`

El programa puede mostrar una tabla de pasos para observar cómo cambia la pila y la salida durante la conversión, lo cual ayuda a comprender mejor el algoritmo.

## Aplicación en el inciso 4

El inciso 4 amplía el mismo algoritmo para trabajar con expresiones regulares. En este caso, los operadores cambian:

- `*`: cerradura de Kleene, operador unario
- `.`: concatenación
- `|`: unión o alternancia
- `(` y `)`: agrupan subexpresiones

La lógica del algoritmo sigue siendo la misma, pero ahora se aplica sobre un conjunto de operadores distintos. El cambio principal es que la expresión regular se convierte también a notación postfix, por ejemplo:

- Expresión infix: `(a|b)*.a.b.b`
- Expresión postfix: `ab|*a.b.b.`

Una vez obtenida la forma postfix, el programa la interpreta y la explica leyendo de derecha a izquierda para describir cómo se construyó la expresión regular paso a paso.

## Relación entre ambos incisos

Aunque el inciso 3 trabaja con aritmética y el inciso 4 con expresiones regulares, ambos comparten la misma estructura conceptual:

- tokenizar la entrada.
- convertir de infix a postfix con Shunting Yard.
- usar una pila para respetar reglas de precedencia y asociatividad.
- procesar la expresión resultante de forma sistemática.

La diferencia principal está en el conjunto de operadores y en el propósito final: en el inciso 3 se evalúa un valor numérico, mientras que en el inciso 4 se transforma y explica una expresión regular.

## Referencia utilizada

https://mathcenter.oxford.emory.edu/site/cs171/shuntingYardAlgorithm/
    