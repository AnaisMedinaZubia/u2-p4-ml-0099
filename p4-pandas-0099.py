## Anais Medina NC 0099 fecha 23 octubre 2026
import pandas as pd 
import numpy as np
n_filas=5
n_columnas=5 
tag_columnas= tuple("ABCDE")  # etiquetas para las columnas de una tupla
print(tag_columnas)
matriz=np.random.randint(1, 6, size=(n_filas, n_columnas))
print("Genera matriz de 5 filas por 5 columnas")
print("con numeros aleatorios comprendidos entre 1 y 10")
print(matriz)
# la variable df es DataFrame
df = pd.DataFrame(matriz, columns = tag_columnas)
print("------La tabla o dataframe-----NC=0099")
print(df)
print("---------Anais Medina NC 0099-----")