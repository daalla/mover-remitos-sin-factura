"""
1) Revisar qué directorios válidos tienen remitos que se llaman "P"
independientemente de su extensión.
2) Imprimir los paths válidos con remitos tipo "P" en un txt. Esto como MVP. 
Luego se podría iterar hacia un Excel, pero primero lograr el MVP.
"""

import pathlib
import re


DIRECTORIO_BASE = r"C:\Workaround\mover-remitos-sin-factura\sandbox"


def identificar_remitos_sin_precio():
    """
    TODO: Revisar si el objeto en cuestión es un directorio
    """

    remitos_sin_precio = []

    administraciones = pathlib.Path(DIRECTORIO_BASE) 

    for administracion in administraciones.iterdir():
        if administracion.is_dir():
            for service in administracion.iterdir():
                if service.is_dir():
                    for archivo in service.iterdir():
                        nombre_archivo = archivo.stem.lower()
                        if le_falta_precio(nombre_archivo):
                            remitos_sin_precio.append(archivo)

    return remitos_sin_precio


def le_falta_precio(nombre_archivo):
    falta_precio = False 

    # Regex: ^p[\d]*
    if re.match(r"^p[\d]*", nombre_archivo):
        falta_precio = True

    return falta_precio


def generar_reporte(remitos_sin_precio):
    """
    ahí hablé con papá. ir por el lado de que sobreescribe el reporte.
    """

    # if 


def proceso_principal():
    remitos_sin_precio = identificar_remitos_sin_precio()
    generar_reporte(remitos_sin_precio)
    

if __name__ == "__main__":
    proceso_principal()
    