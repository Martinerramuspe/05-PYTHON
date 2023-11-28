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
# FORMAS DE BUSCAR VALORES DENTRO DE UN DATAFRA:----------------------------------------------------------------------------
"juan" in df.index # acordate que nombre_usuario es index
"tecnico" in df["rol"].values 
"tecnico" in df.values # No incluye index, solo columnas
"juan" in df.values # Como poder observar no lo encuentra
 
(df["edad"] != 44).any() # Si existe un valor en la columna edad, distinto de 44, entonces = true.
((df["edad"] <= 14) & (df["edad"] >= 44)).any() # si encuentra valores menores que 14 y mayores que 44, entoces =true.


 # Observacion_01: Dentro de un dataframe hay 2 partes: INDEX y COLUMNAS.
 # Obervacion_02: != ---> Eso significa distinto de ...
 # Observacion_03: == ---> Eso significa exactament igual 