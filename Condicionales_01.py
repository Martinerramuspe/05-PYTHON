# Ejercicio n°1: Realizamos una condicion dentro de otra..............................................
import pandas as pd
import numpy as np

np.random.seed(42)
categorias = ['A', 'B', 'C', 'D', 'E']
columnas_categoricas = ['categoria_1', 'categoria_2']
columnas_enteras = ['variable_1', 'variable_2', 'variable_3', 'variable_4', 'variable_5']
data = {
    'categoria_1': np.random.choice(categorias, 20),
    'categoria_2': np.random.choice(categorias, 20),
    'variable_1': np.random.randint(1, 100, 20),
    'variable_2': np.random.randint(1, 100, 20),
    'variable_3': np.random.randint(1, 100, 20),
    'variable_4': np.random.randint(1, 100, 20),
    'variable_5': np.random.randint(1, 100, 20)
}
df = pd.DataFrame(data)
df.head(3)

if (df["variable_1"]>11).any():
    if (df["categoria_1"]== "Y").any():
        print("Paso la segunda ronda")
    elif(df["categoria_1"]== "D").any():
        print("Sos un genio")
    else:
        print("Quedaste a mitad de camino")

else:
    print("No avanzaste a ningun lugar")

# Ejercicio n°2: Eliminamos primera fila, que con cumple con condicion.....................................

data = {'variable_1': [100, 150, 190, 120, 130]} 
df = pd.DataFrame(data)
df
if (df["variable_1"] > 151).any():
    df=df.drop((df["variable_1"] > 151).idxmax())
    print(f"Acabas de reducir el df{df}")
else:
    print("No se puedo efecturiar lo solicitado")


# Ejercicio n°3:  Aplicamos analogia con el ejercicio anterior...............................................
data = {'variable_1': [100, 150, 190, 120, 130]} 
df = pd.DataFrame(data)
df
if (df["variable_1"] > 151).any():
    df=df.drop((df["variable_1"] > 151).idxmin())
    print(f"Acabas de reducir el df{df}")
else:
    print("No se puedo efecturiar lo solicitado")



