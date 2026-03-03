---
title: "Python básico"
math: true
date: 2026-03-03
description: "Un vistazo a python para bioinformáticos"
author: jqenk
categories: [bioinformatica]
tags: [bioinformatica, python]
comments: false
---

# Python básico

> **El Zen de Python**
> Lee el poema The Zen of Python, de Tim Peters ejecutando:
> ```python
>     import this
> ```
{: .prompt-tip }


```python
import this
```

    The Zen of Python, by Tim Peters
    
    Beautiful is better than ugly.
    Explicit is better than implicit.
    Simple is better than complex.
    Complex is better than complicated.
    Flat is better than nested.
    Sparse is better than dense.
    Readability counts.
    Special cases aren't special enough to break the rules.
    Although practicality beats purity.
    Errors should never pass silently.
    Unless explicitly silenced.
    In the face of ambiguity, refuse the temptation to guess.
    There should be one-- and preferably only one --obvious way to do it.
    Although that way may not be obvious at first unless you're Dutch.
    Now is better than never.
    Although never is often better than *right* now.
    If the implementation is hard to explain, it's a bad idea.
    If the implementation is easy to explain, it may be a good idea.
    Namespaces are one honking great idea -- let's do more of those!


> **El cuadrado de la hipotenusa**
> **Dado**: dos enteros positivos a y b, cada uno menor que 1000.   
> 
> **Devuelve**: el entero correspondiente al cuadrado de la hipotenusa del triángulo rectángulo cuyos catetos tienen longitudes a y b.
{: .prompt-tip }


```python
def square_of_hypotenuse(a, b):
    """
    Calcula el cuadrado de la hipotenusa de un triángulo rectángulo
    dados los catetos a y b.
    
    Parámetros:
    a (int): Longitud del primer cateto (0 < a < 1000)
    b (int): Longitud del segundo cateto (0 < b < 1000)
    
    Retorna:
    int: El valor de a² + b² (cuadrado de la hipotenusa)
    """
    return a**2 + b**2

```


```python
square_of_hypotenuse(3, 5)
```




    34




```python
square_of_hypotenuse(987, 907)
```




    1796818




Esta pregunta es más sencilla de lo que podría parecer. ¡De hecho, es una consecuencia directa del **Teorema de Pitágoras**!

Para encontrar la hipotenusa de un triángulo rectángulo, utilizamos las variables $a$, $b$ y $c$, donde $c$ representa la hipotenusa.

La fórmula para calcular $c$ dados los catetos $a$ y $b$ es:

$$a^2 + b^2 = c^2$$

Como necesitamos encontrar específicamente el **cuadrado de la hipotenusa** (es decir, $c^2$), nos evitamos realizar la raíz cuadrada y simplemente calculamos:

$$c^2 = a^2 + b^2$$

Primero se nos asignan dos valores dados para los catetos de un triángulo rectángulo. Por ejemplo:

$$a = 222$$
$$b = 365$$

Entonces podemos escribir una expresión básica e imprimir el resultado:

```python
c_squared = a * a + b * b
print(c_squared)
```

Alternativamente, también puedes usar el operador de potencia de Python:

```python
c_squared = a**2 + b**2
print(c_squared)
```

**Resultado para el ejemplo:**  
$222^2 + 365^2 = 49284 + 133225 = 182509$

> **Cadenas y slices**
> 
> **Dado:** Una cadena `s` de longitud máxima de 200 letras y cuatro enteros `a`, `b`, `c` y `d`.
> 
> **Devuelve:** La rebanada (slice) de esta cadena desde los índices `a` hasta `b` e `c` hasta `d` (con un espacio entre ellas), de forma inclusiva. En otras palabras, debemos incluir los elementos `s[b]` y `s[d]` en nuestra rebanada.
{: .prompt-tip }

**Conjunto de datos de ejemplo:**
```
HumptyDumptysatonawallHumptyDumptyhadagreatfallAlltheKingshorsesandalltheKingsmenCouldntputHumptyDumptyinhisplaceagain.
22 27 97 102
```

**Salida de ejemplo:**
```
Humpty Dumpty
```


```python
def slice_string(s, a, b, c, d):
    """
    Extrae dos slices de la cadena s de forma inclusiva:
    - Primera slice: desde el índice a hasta b (incluyendo b)
    - Segunda slice: desde el índice c hasta d (incluyendo d)
    
    Retorna ambas rebanadas concatenadas con un espacio en medio.
    
    Parámetros:
    s (str): Cadena de entrada (longitud ≤ 200)
    a, b, c, d (int): Índices enteros
    
    Retorna:
    str: Las dos subcadenas extraídas separadas por un espacio
    """
    slice1 = s[a:b+1]  # +1 porque el slicing en Python es exclusivo en el extremo derecho
    slice2 = s[c:d+1]
    return f"{slice1} {slice2}"
```


```python

s = "HumptyDumptysatonawallHumptyDumptyhadagreatfallAlltheKingshorsesandalltheKingsmenCouldntputHumptyDumptyinhisplaceagain."
a, b, c, d = 22, 27, 97, 102
    
resultado = slice_string(s, a, b, c, d)
print(resultado)  
```

    Humpty Dumpty



```python
s = "crcQ5H2E33jy4vNeVEUd1tHwu8mng8Cpbrcx53FAAlaudarZ9yEjR150j3uO8Ri30FIw849HGqUl3cQGRrSND3wrbg9GMKwWnNcbZizeqP28IZiOGvflqsWnYx14grsTsemipalmatusxcDc8SrNOe1ZxKZJOoxH."
a, b, c, d = 40, 45, 128, 139
    
resultado = slice_string(s, a, b, c, d)
print(resultado)  
```

    Alauda semipalmatus



```python
s = "platelmintoR2D2Bienrepercusion654Panderetahechopetricor"
a, b, c, d = 15, 18, 42, 46
resultado = slice_string(s, a, b, c, d)
print(resultado)  
```

    Bien hecho


En Python, las subcadenas se pueden especificar utilizando la notación de *slicing*. Múltiples cadenas pueden concatenarse simplemente sumándolas.

> **Nota importante:** Python **no incluye** el índice final en los slices. Para incluirlo, debemos sumar 1 al índice final.

Ten cuidado con el lenguaje de programación que utilices:
- Algunos usan **indexación basada en 0**, donde el primer elemento tiene índice `0` y el enésimo elemento tiene índice `n-1` (por ejemplo, **Python**).
- Otros usan **indexación basada en 1**, donde el primer elemento tiene índice `1` y el enésimo elemento tiene índice `n` (por ejemplo, **R**).


```python
input_string = leer_desde_archivo()
output_string = input_string[a : b+1] + ' ' + input_string[c : d+1]
print(output_string)
```

> **Enteros impares**
> 
> **Dado:** Dos enteros positivos $a$ y $b$ ($a < b < 10000$).  
> **Retornar:** La suma de todos los enteros impares desde $a$ hasta $b$, inclusivamente.
{: .prompt-tip }
    
**Conjunto de datos de ejemplo**  
```
100 200
```

**Salida de ejemplo**  
```
7500
```

Dados dos valores, $a$ y $b$, queremos determinar la suma de todos los enteros impares desde $a$ hasta $b$, incluyendo ambos extremos $a$ y $b$.


La idea principal del algoritmo es utilizar un bucle para sumar todos los enteros impares presentes en el rango desde $a$ hasta $b$, inclusivo. **Nota:** La diferencia entre cada par de enteros impares consecutivos es **2** (no 1).


```python
a, b = 4138, 8214

# Asegurar que 'a' sea un número impar:
if a % 2 == 0:
    a += 1

# Calcular la suma de números impares entre a y b:
suma = 0 
for i in range(a, b + 1, 2):
    suma += i

print(suma) 
```

    12586688



```
suma = 0
para i = a; i <= b; i++
  si i % 2 == 1
    suma += i
  fin si
fin para
imprimir suma
```

El algoritmo requiere tiempo $O(n)$, donde $n = b - a$.


Como el problema describe una progresión aritmética (cada elemento está separado por una diferencia constante de 2), podemos calcular la suma mediante la fórmula:

$$\text{Suma} = \frac{(E_1 + E_2) \cdot n}{2}$$

donde:
- $E_1$ es el primer elemento impar del rango,
- $E_2$ es el último elemento impar del rango,
- $n$ es la cantidad de elementos impares en la serie.



```python
def sum_odd_integers(a, b):
    """
    Calcula la suma de todos los enteros impares en el rango [a, b] (inclusivo).
    
    Parámetros:
    a (int): Límite inferior del rango (a < b < 10000)
    b (int): Límite superior del rango
    
    Retorna:
    int: Suma de todos los enteros impares entre a y b, inclusivamente
    """
    # Encontrar el primer número impar >= a
    start = a if a % 2 != 0 else a + 1
    
    # Encontrar el último número impar <= b
    end = b if b % 2 != 0 else b - 1
    
    # Si no hay números impares en el rango
    if start > end:
        return 0
    
    # Método 1: Usando fórmula de progresión aritmética (más eficiente)
    n = (end - start) // 2 + 1  # Número de términos
    return n * (start + end) // 2

    # Alternativa (menos eficiente para rangos grandes):
    # return sum(i for i in range(start, end + 1, 2))

```


```python
a, b = 4138, 8214
sum_odd_integers(a, b)
```




    12586688



> **Archivos**
> **Dado:** Un archivo que contiene como máximo 1000 líneas.  
> **Retornar:** Un archivo que contenga todas las líneas con número par del archivo original. Se asume numeración basada en 1 (es decir, la primera línea es la línea 1, la segunda es la línea 2, etc.).
{: .prompt-tip }
**Conjunto de datos de ejemplo**  
```
Bravely bold Sir Robin rode forth from Camelot
Yes, brave Sir Robin turned about
He was not afraid to die, O brave Sir Robin
And gallantly he chickened out
He was not at all afraid to be killed in nasty ways
Bravely talking to his feet
Brave, brave, brave, brave Sir Robin
He beat a very brave retreat
```

**Salida de ejemplo**  
```
Yes, brave Sir Robin turned about
And gallantly he chickened out
Bravely talking to his feet
He beat a very brave retreat
```


```python
def extract_even_lines(input_file, output_file=None):
    """
    Extrae las líneas con número par (numeración 1-based) de un archivo.
    
    Parámetros:
    input_file (str): Ruta al archivo de entrada
    output_file (str, opcional): Ruta al archivo de salida. Si es None, imprime por pantalla.
    
    Retorna:
    list: Lista de líneas pares extraídas
    """
    even_lines = []
    
    with open(input_file, 'r', encoding='utf-8') as f:
        # enumerate con start=1 para numeración 1-based
        for line_num, line in enumerate(f, start=1):
            if line_num % 2 == 0:  # Línea par en numeración 1-based
                even_lines.append(line.rstrip('\n'))
    
    # Salida a archivo o a pantalla
    if output_file:
        with open(output_file, 'w', encoding='utf-8') as f_out:
            f_out.write('\n'.join(even_lines))
    else:
        for line in even_lines:
            print(line)
    
    return even_lines
```


```python
extract_even_lines("data/input.txt", "data/output.txt")
```




    ['Yes, brave Sir Robin turned about',
     'And gallantly he chickened out',
     'Bravely talking to his feet',
     'He beat a very brave retreat']




```python
extract_even_lines("data/questioni.txt", "data/questiono.txt")
```




    ['Some things in life are bad, they can really make you mad',
     'Other things just make you swear and curse',
     "When you're chewing on life's gristle, don't grumble give a whistle",
     'This will help things turn out for the best',
     'Always look on the bright side of life',
     'Always look on the right side of life',
     "If life seems jolly rotten, there's something you've forgotten",
     "And that's to laugh and smile and dance and sing",
     "When you're feeling in the dumps, don't be silly, chumps",
     "Just purse your lips and whistle, that's the thing",
     'So, always look on the bright side of death',
     'Just before you draw your terminal breath',
     "Life's a counterfeit and when you look at it",
     "Life's a laugh and death's the joke, it's true",
     "You see, it's all a show, keep them laughing as you go",
     'Just remember the last laugh is on you',
     'Always look on the bright side of life',
     'And always look on the right side of life',
     'Always look on the bright side of life',
     'And always look on the right side of life']



> **Diccionarios**
> **Dado:** Una cadena `s` de longitud máxima de 10000 letras.  
> **Retornar:** El número de ocurrencias de cada palabra en `s`, donde las palabras están separadas por espacios. Las palabras distinguen mayúsculas y minúsculas (*case-sensitive*), y las líneas en la salida pueden aparecer en cualquier orden.
{: .prompt-tip }
**Conjunto de datos de ejemplo**  
```
We tried list and we tried dicts also we tried Zen
```

**Salida de ejemplo**  
```
and 1
We 1
tried 3
dicts 1
list 1
we 2
also 1
Zen 1
```


```python
from collections import Counter
import sys

def count_word_occurrences(s):
    """
    Cuenta las ocurrencias de cada palabra en la cadena s.
    Las palabras están separadas por espacios y son case-sensitive.
    
    Parámetros:
    s (str): Cadena de entrada
    
    Retorna:
    dict: Diccionario con palabras como claves y conteos como valores
    """
    words = s.split()  # split() maneja múltiples espacios y separa por cualquier whitespace
    return dict(Counter(words))
```


```python
s = "We tried list and we tried dicts also we tried Zen"

# Contar ocurrencias
word_counts = count_word_occurrences(s)

# Imprimir resultados (orden arbitrario, como permite el problema)
for word, count in word_counts.items():
    print(f"{word} {count}")
```

    We 1
    tried 3
    list 1
    and 1
    we 2
    dicts 1
    also 1
    Zen 1



```python
s = "When I find myself in times of trouble Mother Mary comes to me Speaking words of wisdom let it be And in my hour of darkness she is standing right in front of me Speaking words of wisdom let it be Let it be let it be let it be let it be Whisper words of wisdom let it be And when the broken hearted people living in the world agree There will be an answer let it be For though they may be parted there is still a chance that they will see There will be an answer let it be Let it be let it be let it be let it be There will be an answer let it be Let it be let it be let it be let it be Whisper words of wisdom let it be Let it be let it be let it be let it be Whisper words of wisdom let it be And when the night is cloudy there is still a light that shines on me Shine until tomorrow let it be I wake up to the sound of music Mother Mary comes to me Speaking words of wisdom let it be Let it be let it be let it be yeah let it be There will be an answer let it be Let it be let it be let it be yeah let it be Whisper words of wisdom let it be"

# Contar ocurrencias
word_counts = count_word_occurrences(s)

# Imprimir resultados (orden arbitrario, como permite el problema)
for word, count in word_counts.items():
    print(f"{word} {count}")
```

    When 1
    I 2
    find 1
    myself 1
    in 4
    times 1
    of 11
    trouble 1
    Mother 2
    Mary 2
    comes 2
    to 3
    me 4
    Speaking 3
    words 7
    wisdom 7
    let 30
    it 36
    be 41
    And 3
    my 1
    hour 1
    darkness 1
    she 1
    is 4
    standing 1
    right 1
    front 1
    Let 6
    Whisper 4
    when 2
    the 4
    broken 1
    hearted 1
    people 1
    living 1
    world 1
    agree 1
    There 4
    will 5
    an 4
    answer 4
    For 1
    though 1
    they 2
    may 1
    parted 1
    there 2
    still 2
    a 2
    chance 1
    that 2
    see 1
    night 1
    cloudy 1
    light 1
    shines 1
    on 1
    Shine 1
    until 1
    tomorrow 1
    wake 1
    up 1
    sound 1
    music 1
    yeah 2



1. **Separación de palabras:**  
   Usamos `s.split()` que:
   - Separa la cadena por cualquier espacio en blanco (incluyendo múltiples espacios consecutivos)
   - Elimina espacios al inicio y final automáticamente
   - Funciona correctamente incluso si hay saltos de línea en la entrada

2. **Case-sensitivity:**  
   Python es *case-sensitive* por defecto, por lo que `"We"` y `"we"` se tratan como palabras distintas (como requiere el problema).

3. **Conteo eficiente:**  
   `collections.Counter` proporciona un conteo óptimo en tiempo $O(n)$ donde $n$ es el número de palabras.

4. **Formato de salida:**  
   Cada línea muestra `palabra conteo`, en orden arbitrario (cumpliendo con el requisito del problema).


⬅️ [Volver al desafío](desafio.ipynb)  

⬅️ [Volver al índice](../índice.md)



```python
%%html
<div class="prompt-tip">
  <p><strong>Tip:</strong> Este cuadro se verá verde en Chirpy.</p>
</div>

```


<div class="prompt-tip">
  <p><strong>Tip:</strong> Este cuadro se verá verde en Chirpy.</p>
</div>




```python

```
