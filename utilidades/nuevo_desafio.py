#!/usr/bin/env python3

import sys
import shutil
import unicodedata
from pathlib import Path

def slugify(text):
    text = unicodedata.normalize("NFKD", text)
    text = text.encode("ascii", "ignore").decode("ascii")
    text = text.lower().replace(" ", "_")
    return text

def actualizar_indice(numero, titulo, carpeta):
    indice = Path("desafios") / "índice.md"

    if not indice.exists():
        print("⚠️  índice.md no encontrado. No se actualiza el índice.")
        return

    fila = (
        f"| {numero} | {titulo} | "
        f"[📘]({carpeta}/teoría.md) | "
        f"[🧩]({carpeta}/desafio.ipynb) | "
        f"[✅]({carpeta}/solución.ipynb) | "
        f" |\n"
    )

    with open(indice, "a", encoding="utf-8") as f:
        f.write(fila)

    print("🧾 Índice actualizado.")

def main():
    if len(sys.argv) < 3:
        print("Uso: python nuevo_desafio.py <numero> <titulo>")
        sys.exit(1)

    numero = sys.argv[1].zfill(2)
    titulo = " ".join(sys.argv[2:])
    slug = slugify(titulo)

    base = Path("desafios")
    carpeta = f"desafio_{numero}_{slug}"
    destino = base / carpeta

    if destino.exists():
        print(f"❌ El desafío {destino.name} ya existe.")
        sys.exit(1)

    print(f"📁 Creando {destino}...")
    destino.mkdir(parents=True)

    plantillas = Path("manuales")

    shutil.copy(plantillas / "plantilla_teoria.md", destino / "teoría.md")
    shutil.copy(plantillas / "plantilla_desafio.ipynb", destino / "desafio.ipynb")
    shutil.copy(plantillas / "plantilla_solucion.ipynb", destino / "solución.ipynb")

    (destino / "solución.py").touch()
    (destino / "data").mkdir()
    (destino / "tests").mkdir()
    (destino / "tests" / "test.py").touch()

    actualizar_indice(numero, titulo, carpeta)

    print("✅ Desafío creado correctamente.")

if __name__ == "__main__":
    main()

