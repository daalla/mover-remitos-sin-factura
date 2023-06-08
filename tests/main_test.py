"""
Funciones que no voy a testear:
- choose_source_folder: no posee lógica condicional.
- choose_destination_folder: no posee lógica condicional.
- inform_copy_completion: no posee lógica condicional.
- inform_copy_cancellation: no posee lógica condicional.


Funciones a testear:
- get_folders_without_invoice
- main?
"""
from unittest import mock
import pathlib
import pytest

from source import main

@pytest.fixture
def my_fixture():
    pass

# Hacer que solo funcione si detecta un WindowsPath?
# qué pasa si no entiende el nombre del objeto?

def test_get_folders_without_invoice(my_fixture):
    """
    1) Setear carpeta y ficheros de prueba.
    2) Hacer que la función identifique cuáles son las órdenes de servicio sin 
    factura de ese set.
    3) Verificar que la función devuelva los resultados esperados.

    ---

    Input:
    - string con path de carpeta fuente
    
    Output:
    - (ver)
    
    creo que tengo que armar fixture que cree carpeta temporal.

    primer hacer el happy path y luego ir probando demás condicionales.
    """


    
