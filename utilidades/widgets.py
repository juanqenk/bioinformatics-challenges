from ipywidgets import Button, Output
from pathlib import Path
import re


def boton_marcar_completado(
    indice_path=Path("..") / "índice.md",
    checkbox_vacio="☐",
    checkbox_marcado="🗹",
):
    """
    Devuelve un botón de ipywidgets que marca el desafío actual
    como completado en el índice.md.

    El desafío se identifica usando el nombre de la carpeta actual.
    """

    boton = Button(
        description="🗹 Marcar como completado",
        button_style="success"
    )

    salida = Output()

    def marcar_completado(_):
        with salida:
            salida.clear_output()

            if not indice_path.exists():
                print("❌ No se encontró índice.md")
                return

            carpeta_actual = Path.cwd().name

            lineas = indice_path.read_text(encoding="utf-8").splitlines()
            nuevas_lineas = []
            encontrado = False

            for linea in lineas:
                if carpeta_actual in linea:
                    if checkbox_marcado in linea:
                        print("ℹ️ Este desafío ya estaba marcado como completado.")
                        return

                    linea = re.sub(
                        re.escape(checkbox_vacio),
                        checkbox_marcado,
                        linea
                    )
                    encontrado = True

                nuevas_lineas.append(linea)

            if not encontrado:
                print("⚠️ No se encontró la fila del desafío en el índice.")
                return

            indice_path.write_text(
                "\n".join(nuevas_lineas) + "\n",
                encoding="utf-8"
            )

            print("✅ Desafío marcado como completado en el índice.")

    boton.on_click(marcar_completado)

    return boton, salida

