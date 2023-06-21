Versión del runtime de Python: 3.11.2

TODO:
GENERAL:
- Sacar MVP y luego hacer los tests y por último, si queda tiempo y lo amerita,
hacer refactor del código usando los tests como soporte (sería como un "TDD" al 
revés).
- Que el paquete incluya el runtime de Python, así es más portátil.
- Habría que definir cuál es el directorio base, ya que hay que parametrizarlo
en algún lado. Ver si ponen el path del directorio remoto (ej, 
\\\OFICINA\FACTURAS) o si se monta dicho path en algúna letra (ej, E:\ 
directamente).

PONER_PRECIOS:
- Analizar si hay algún riesgo de que el patrón P(numeros) no sirva como flag 
para el proceso.
-