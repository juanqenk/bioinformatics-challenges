### 1. Fundamentos, Funciones y Aritmética Computacional

Antes de escribir una sola línea de código, debéis recordar la filosofía del lenguaje. Python valora la legibilidad y la simplicidad (el "Zen de Python"). Sin embargo, la base de todo programa es la capacidad de abstraer operaciones mediante **funciones**.

Una función (`def`) es un bloque de código reutilizable. La teoría clave aquí es el **paso de parámetros** y el **retorno de valores**. Cuando definís una función matemática, como el cálculo de una hipotenusa, estáis traduciendo una expresión algebraica ($a^2 + b^2 = c^2$) a una expresión computacional.

*   **Operadores Aritméticos:** Python distingue entre división clásica (`/`) y división entera (`//`). Para la exponenciación (elevar un número a una potencia), no utilizamos el acento circunflejo (`^`, que es una operación bit a bit XOR), sino el operador de doble asterisco (`**`).
*   **Precedencia:** Al igual que en matemáticas, la exponenciación tiene prioridad sobre la suma. Por tanto, `a**2 + b**2` se evalúa correctamente sin necesidad de paréntesis extra.

### 2. Manipulación de Cadenas y la Teoría del "Slicing"

Las cadenas de texto (*strings*) en Python son secuencias inmutables de caracteres. El concepto teórico más importante para resolver problemas de extracción de texto es la **indexación basada en cero (0-based indexing)**.

*   **Índices:** El primer elemento está en la posición 0, el segundo en la 1, y así sucesivamente.
*   **Slicing (Rebanado):** Esta es la herramienta más potente y fuente común de errores. La sintaxis general es `secuencia[inicio:fin:paso]`.
    *   **La regla de oro del límite superior:** El intervalo en Python es **semi-abierto** `[a, b)`. Esto significa que el corte incluye el índice de `inicio` pero **excluye** el índice de `fin`.
    *   Si os piden extraer desde el índice $A$ hasta el índice $B$ *inclusive*, la teoría dicta que debéis programar el corte hasta $B+1$. Si olvidáis ese `+1`, perderéis el último carácter.
*   **Concatenación:** Las cadenas se pueden unir mediante el operador `+` o, de manera más moderna y eficiente ("Pythonic"), utilizando **f-strings** (cadenas con formato), que permiten insertar variables directamente dentro del texto.

### 3. Control de Flujo: Bucles e Intervalos Numéricos

Para sumar secuencias de números (como los enteros impares), necesitamos entender la iteración.

*   **La función `range()`:** Es un generador de progresiones aritméticas. Su firma completa es `range(start, stop, step)`.
    *   Al igual que en el *slicing*, el `stop` es exclusivo. Para llegar hasta un número $N$ inclusive, el rango debe definirse hasta $N+1$.
    *   El parámetro `step` (paso) es crucial para filtrar números sin usar condicionales internos. Si queréis iterar solo por impares y empezáis en un impar, un paso de 2 (`step=2`) salta los pares automáticamente.
*   **El patrón Acumulador:** Algorítmicamente, para sumar una serie, inicializamos una variable (ej. `total = 0`) fuera del bucle. En cada iteración, actualizamos esta variable (`total += valor`).
*   **Complejidad Computacional (Big O):** Un bucle simple es $O(n)$, donde $n$ es el tamaño del rango. Aunque existen fórmulas matemáticas de progresión aritmética que resuelven esto en $O(1)$ (tiempo constante), en computación básica es fundamental saber implementar la solución iterativa.
*   **Aritmética Modular:** Para verificar paridad (si un número es par o impar), usamos el operador módulo `%`. `n % 2 == 0` implica paridad; `n % 2 != 0` implica imparidad.

### 4. Persistencia de Datos: Manejo de Archivos (File I/O)

El manejo de archivos introduce el concepto de recursos del sistema operativo. Un archivo debe abrirse, procesarse y cerrarse.

*   **Context Managers (`with`):** La teoría moderna de Python desaconseja usar `open()` y `close()` manualmente. En su lugar, usamos el bloque `with open(...) as f:`. Esto garantiza que el archivo se cierre correctamente incluso si ocurre un error (excepción) durante la lectura, evitando fugas de memoria o bloqueos de archivos.
*   **Iteración sobre archivos:** Un objeto archivo es iterable. Podemos recorrerlo línea por línea con un bucle `for`.
*   **Enumeración (`enumerate`):** A menudo necesitamos el contenido de la línea y su número de fila simultáneamente. La función `enumerate(iterable, start=0)` envuelve el iterador y devuelve tuplas `(índice, valor)`.
    *   *Ojo al dato:* Los informáticos contamos desde 0, pero los humanos (y los requerimientos de vuestro examen) suelen contar líneas desde 1. Debéis ajustar el parámetro `start=1` en `enumerate` o sumar 1 manualmente al índice para alinear la lógica del programa con la lógica del problema.
*   **Limpieza de datos:** Las líneas leídas de un archivo suelen contener el carácter de salto de línea (`\n`) al final. Métodos como `.strip()` o `.rstrip()` son esenciales para limpiar la entrada antes de procesarla.

### 5. Estructuras de Datos: Diccionarios y Hashing

Finalmente, para problemas de conteo de frecuencias (como contar palabras), las listas son ineficientes. Aquí entra la teoría de las **Tablas Hash** (implementadas como `dict` en Python).

*   **Tokenización:** Antes de contar, debemos dividir una frase en unidades semánticas (palabras). El método `.split()` divide una cadena basándose en los espacios en blanco, retornando una lista.
*   **Diccionarios (`dict`):** Permiten mapear una clave (la palabra) a un valor (su frecuencia). La búsqueda y actualización en un diccionario tiene una complejidad promedio de $O(1)$, lo cual es mucho más rápido que buscar en una lista ($O(n)$).
*   **`collections.Counter`:** Python ofrece una herramienta especializada en la biblioteca estándar que implementa la lógica de un "multiconjunto" o bolsa. `Counter(lista)` crea automáticamente un diccionario donde las claves son los elementos únicos y los valores son sus recuentos.
*   **Sensibilidad a mayúsculas (Case Sensitivity):** En la tabla ASCII, "Hola" y "hola" tienen valores binarios diferentes. A menos que se normalice el texto (convirtiendo todo a minúsculas), un algoritmo de conteo las tratará como entidades distintas.

### Resumen de estrategia para la resolución de los problemas

1.  **Analizad los límites:** ¿Los rangos son inclusivos o exclusivos? (Recordad: Python excluye el final por defecto).
2.  **Elegid la estructura correcta:** ¿Necesitáis orden (Listas) o asociación rápida (Diccionarios)?
3.  **Gestionad los recursos:** Usad siempre `with` para archivos.
4.  **Matemáticas:** Aprovechad los operadores nativos (`**`, `%`, `//`).


## 🔗 Siguiente paso
➡️ [Ir al enunciado del desafío](desafio.ipynb)

