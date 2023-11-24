# DATAFRAME
# Diccionario a df: 
usuarios = {"juan": {"edad":44, "rol": "ingenierio"},
            "martin": {"edad":34, "rol": "data_ciences"},
            "agustin": {"edad":14, "rol": "tecnico"}}
usuarios
import pandas as pd
df =pd.DataFrame(usuarios)
# Transponemos
df= df.T
# asignamos nombre a la variable nombres
df.index.name = 'nombre_usuario'
df
"juan" in df.index # acordate que nombre_usuario es index
"tecnico" in df["rol"].values 
"tecnico" in df.values # no incluye index, solo columnas
"juan" in df.values
 
 #Observacion_01: Dentro de un dataframe hay 2 partes: INDEX y COLUMNAS.