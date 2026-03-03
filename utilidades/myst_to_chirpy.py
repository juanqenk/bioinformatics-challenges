import re
import sys
import os
from datetime import datetime

def get_chirpy_header(date_str):
    # Formato completo de fecha para el interior del archivo
    full_date = f"{date_str} 12:00:00 +0100"
    
    header = f"""---
title: ""
math: true
date: {full_date}
description: ""
author: jqenk
categories: [bioinformatica]
tags: [bioinformatica, python]
comments: false
---

"""
    return header

def convert_myst_to_chirpy(content, date_str):
    # Normalizar saltos de línea
    content = content.replace('\r\n', '\n')

    # Mapeo de alertas
    mapping = {
        'tip': 'prompt-tip',
        'info': 'prompt-info',
        'warning': 'prompt-warning',
        'danger': 'prompt-danger',
        'note': 'prompt-info',
        'important': 'prompt-info',
        'caution': 'prompt-warning'
    }

    # Regex flexible para :::tip, :::tip Titulo, o :::{tip} Titulo
    pattern = r":{3,}\{?(\w+)\}?[ \t]*(.*)\n([\s\S]*?)\n\s*:{3,}"

    def replace_admonition(match):
        ad_type = match.group(1).lower().strip()
        title = match.group(2).strip()
        body = match.group(3)
        
        if not title:
            title = ad_type.capitalize()
            
        chirpy_class = mapping.get(ad_type, 'prompt-info')
        
        # Convertir cuerpo a blockquote de Chirpy
        lines = body.split('\n')
        quoted_lines = [f"> {line}" if (line.strip() or line == "") else ">" for line in lines]
        quoted_body = "\n".join(quoted_lines)
        
        return f"> **{title}**\n{quoted_body}\n{{: .{chirpy_class} }}"

    # Aplicar conversión e inyectar el header
    converted_body = re.sub(pattern, replace_admonition, content)
    return get_chirpy_header(date_str) + converted_body

def main():
    if len(sys.argv) < 2:
        print("Uso: python jupyter_to_chirpy.py archivo.md")
        return

    input_path = sys.argv[1]
    if not os.path.exists(input_path):
        print(f"❌ No se encuentra el archivo: {input_path}")
        return

    # 1. Obtener fechas y nombres
    now = datetime.now()
    date_prefix = now.strftime("%Y-%m-%d")
    
    with open(input_path, 'r', encoding='utf-8') as f:
        data = f.read()

    # 2. Procesar contenido
    final_content = convert_myst_to_chirpy(data, date_prefix)

    # 3. Calcular nuevo nombre de archivo (Formato Jekyll: AAAA-MM-DD-nombre.md)
    dir_name = os.path.dirname(input_path)
    base_name = os.path.basename(input_path)
    
    # Limpiamos el nombre original de espacios y caracteres raros
    clean_name = base_name.lower().replace(" ", "-").replace("_", "-")
    # Si el nombre ya empezaba por una fecha, se la quitamos para no duplicar
    clean_name = re.sub(r'^\d{4}-\d{2}-\d{2}-', '', clean_name)
    
    new_filename = f"{date_prefix}-{clean_name}"
    output_path = os.path.join(dir_name, new_filename)

    # 4. Guardar
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(final_content)

    print(f"✅ ¡Procesado con éxito!")
    print(f"📁 Nuevo nombre: {new_filename}")
    print(f"📍 Ruta: {output_path}")

if __name__ == "__main__":
    main()