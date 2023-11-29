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
 # Observacion_03: == ---> Es significa exactament igual 

#LISTAS DE METODOS APLICADOS A LAS COLUMNAS DE LOS DATAFRAME---------------------------------------------------------------
(df["variable_1"] > 1111).all()
(df["variable_1"] > 1111).any()
(df["variable_1"] > 1111).sum()
(df["variable_1"] > 1111).mean()

# Índice del primer valor True
idx_primero_true = (df["variable_1"] > 1111).idxmax()
# Índice del primer valor False
idx_primero_false = (df["variable_1"] > 1111).idxmin()
# Los 3 mayores valores que cumplen la condición
mayores_que_1111 = df[df["variable_1"] > 1111]["variable_1"].nlargest(3)
# Los 3 menores valores que cumplen la condición
menores_que_1111 = df[df["variable_1"] > 1111]["variable_1"].nsmallest(3)
# Reemplaza los valores que no son mayores que 1111 con NaN
df["variable_1"].mask(df["variable_1"] <= 1111, inplace=True)






# Crear un DataFrame de ejemplo
data = {'variable_1': [100, 150, 190, 120, 130]}
df = pd.DataFrame(data)
df
if (df["variable_1"] > 151).any():
    df=df.drop((df["variable_1"] > 151).idxmax())
    print(f"Acabas de reducir el df{df}")
else:
    print("No se puedo efecturiar lo solicitado")


