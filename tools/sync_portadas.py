# -*- coding: utf-8 -*-
"""
Auditor y Sincronizador Completo de Portadas para index.html
"""

import os
import sys
import re

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')
    sys.stderr.reconfigure(encoding='utf-8', errors='replace')

BASE_DIR = r"C:\D DCT\programas\hsefemeride"
ASSETS_DIR = os.path.join(BASE_DIR, "assets", "efemerides")
INDEX_PATH = os.path.join(BASE_DIR, "index.html")

def main():
    with open(INDEX_PATH, "r", encoding="utf-8") as f:
        content = f.read()

    # Dividir el array historias en bloques individuales
    # Cada bloque empieza con { y termina con }
    start_pos = content.find("const historias = [")
    end_pos = content.find("    ];\n\n    // Placeholder visual")
    if end_pos == -1:
        end_pos = content.find("    ];\r\n\r\n    // Placeholder visual")
    if end_pos == -1:
        end_pos = content.find("    ];")

    if start_pos == -1 or end_pos == -1:
        print("Error al localizar array historias")
        return

    historias_text = content[start_pos:end_pos]
    
    # Procesar línea por línea o por bloques
    # Buscamos cada carpetaAssets y su respectiva línea imagen
    lineas = content.splitlines(keepends=True)
    nuevas_lineas = []
    
    carpeta_actual = None
    reemplazos = 0

    for i, line in enumerate(lineas):
        # Detectar carpetaAssets
        m_carpeta = re.search(r'carpetaAssets:\s*"(assets/efemerides/([^/]+)/)"', line)
        if m_carpeta:
            carpeta_actual = m_carpeta.group(2)
        
        # Detectar imagen
        m_img = re.search(r'(\s*imagen:\s*")([^"]+)(".*)', line)
        if m_img and carpeta_actual:
            folder_path = os.path.join(ASSETS_DIR, carpeta_actual)
            files = os.listdir(folder_path) if os.path.exists(folder_path) else []
            
            # Prioridad: portada.jpeg > portada.jpg > portada.png
            img_ideal = "portada.png"
            if "portada.jpeg" in files:
                img_ideal = "portada.jpeg"
            elif "portada.jpg" in files:
                img_ideal = "portada.jpg"
            elif "portada.png" in files:
                img_ideal = "portada.png"

            img_actual = m_img.group(2)
            if img_actual != img_ideal:
                prefix = m_img.group(1)
                suffix = m_img.group(3)
                line = f"{prefix}{img_ideal}{suffix}\n"
                reemplazos += 1
                print(f"[{carpeta_actual}] {img_actual} -> {img_ideal}")
            
            carpeta_actual = None # reset para siguiente historia
            
        nuevas_lineas.append(line)

    print(f"\nTotal reemplazos de imagen realizados: {reemplazos}")

    with open(INDEX_PATH, "w", encoding="utf-8") as f:
        f.writelines(nuevas_lineas)

    print("index.html guardado exitosamente.")

if __name__ == "__main__":
    main()
