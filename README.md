# Bioinformatics Challenges in Python

Colección de problemas de bioinformática resueltos en **Python** usando **Jupyter Lab**, con un enfoque práctico, reproducible y orientado al aprendizaje.

---

## 🎯 Objetivos del proyecto

- Practicar algoritmos y conceptos fundamentales de bioinformática
- Aplicar Python a problemas reales de genética y biología computacional
- Fomentar buenas prácticas: código reutilizable, tests y documentación
- Servir como material de apoyo para estudiantes e investigadores en formación

---

## 🧬 Contenido

Los problemas cubren, entre otros, los siguientes temas:

- Manipulación de secuencias de ADN y proteínas
- Formato FASTA y parsing de datos biológicos
- Algoritmos básicos de genética
- Distancias y alineamientos simples
- Estadística básica aplicada a secuencias
- Introducción a la bioinformática algorítmica


---

## 📁 Estructura del repositorio

bioinformatics-challenges/
│
├── README.md
├── requirements.txt
├── .gitignore
│
├── desafios/
│   ├── índice.md          # índice de problemas
│   │
│   ├── desafio_01_/
│   │   ├── teoría.md      # marco teórico
│   │   │── desafio.ipynb   # enunciado del problema y cuestionario de solución
│   │   ├── solución.ipynb
│   │   ├── solución.py    # versión script
│   │   ├── data/
│   │   └── tests/
│   │       └── test.py
│   ├── desafio_02_/
│   │   ├── teoría.md 
│   │   │── desafio.ipynb 
│   │   ├── solución.ipynb
│   │   ├── solución.py 
│   │   ├── data/
│   │   └── tests/
│   │       └── test.py
│   │
│   └── ...
│
├── utilidades/ # Contiene funciones reutilizables.
│
├── data/ 
│
└── manuales/ # Documentación y tutoriales.

## 🛠️ Requisitos

Python ≥ 3.9
Jupyter Lab


Puedes instalar el entorno con:

pip install -r requirements.txt


##  Cómo usar este repositorio

### Descargar el repositorio

Clona el repositorio en tu equipo:

```bash
git clone https://github.com/juanqenk/bioinformatics-challenges.git
cd bioinformatics-challenges
```
### Instalar dependencias
Se recomienda usar un entorno virtual. Por ejemplo:

```bash
python -m venv venv
source venv/bin/activate   # Linux / macOS
# venv\Scripts\activate    # Windows
```
Instala las dependencias:

```bash
pip install -r requirements.txt
```
Asegúrate de tener Jupyter Lab instalado:

```bash
jupyter lab
```
### Flujo recomendado de trabajo
El repositorio está diseñado para seguir un itinerario de aprendizaje guiado.

1. Elegir un desafío
Abre el índice general de problemas:
> desafios/índice.md

Ahí encontrarás la lista de desafíos disponibles y los conceptos que se trabajan en cada uno.

2. Leer la teoría
Dentro del desafío elegido, comienza por el archivo:
> teoría.md

Aquí se introduce el marco teórico, los conceptos biológicos y computacionales necesarios para abordar el problema.

3. Resolver el enunciado
Abre el notebook del desafío:
> desafio.ipynb

Este notebook contiene:

- El enunciado del problema

- Un cuestionario interactivo (basado en jupyterquiz)

- Espacios para razonar y plantear la solución

4. Comparar con la solución
Una vez hayas trabajado el problema, revisa:
> solución.ipynb

También puedes consultar la versión en script:
> solución.py

útil para ver una implementación más limpia y reutilizable.
___________________

Nota: se pueden crear desafios con las plantillas que hay en la carpeta manuales. Para ello hay un script que hay que ejecutar desde la raiz del repositorio

```bash
python3 utilidades/nuevo_desafio.py 06 "Alineamiento global"
``` 

