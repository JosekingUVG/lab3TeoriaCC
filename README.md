# Laboratorio 3 - CC2019

## Ejecución

### Windows PowerShell

1. Clona el repositorio:

```powershell
git clone git@github.com:JosekingUVG/lab3TeoriaCC.git
cd ~/lab3TeoriaCC/CC2019-lab02
```

2. Crea el entorno virtual si no existe:

```powershell
python -m venv .venv
```

3. Activa el entorno virtual:

```powershell
.\.venv\Scripts\Activate.ps1
```

4. Instala dependencias desde `requirements.txt`:

```powershell
pip install -r requirements.txt
```

5. Ejecuta el inciso deseado o los ejemplos de la tarea:

```powershell
python ejemplos.py
python inciso_1.py
python inciso_2.py
```

el inciso 2 descarga una imagen llamada afd.png

6. Cuando termines, desactiva el entorno:

```powershell
deactivate
```

### WSL

Si el entorno `.venv` ya existe, abre WSL y ejecuta:

```bash
cd ~/lab3TeoriaCC/CC2019-lab02
source .venv/bin/activate
```

Deberías ver algo como:

```bash
(.venv) username@username:~/lab3TeoriaCC/CC2019-lab02$
```

Ejecuta el inciso deseado o los ejemplos de la tarea:


```bash
python ejemplos.py
python inciso_1.py
python inciso_2.py
```
el inciso 2 descarga una imagen llamada afd.png


Puedes comprobar qué Python está usando:

```bash
which python
```

Debería apuntar a algo parecido a:

```bash
/home/username/lab3TeoriaCC/CC2019-lab02/.venv/bin/python
```

Cuando termines:

```bash
deactivate
```

### Si estás creando el entorno desde cero en WSL

```bash
cd ~/lab3TeoriaCC/CC2019-lab02
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Después ejecuta:

```bash
python inciso_2.py
```


Una regla práctica: cuando veas `(.venv)` al inicio de tu terminal, estás trabajando dentro del entorno virtual; si no aparece, ejecuta `source .venv/bin/activate`.

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



## Referencia utilizada

https://mathcenter.oxford.emory.edu/site/cs171/shuntingYardAlgorithm/
    
