
# Ciclo for sobre lista.
frutas = ["manzana","platano","uva"]
for x in frutas:
    print(x)

# Ciclo for sobre diccionario, aplicado sobre "clave"
mi_diccionario = {"a": 1, "b": 2, "c": 3}
for y in mi_diccionario:
    print(y)

# Ciclo for sobre diccionario, aplicado sobre "valor"
mi_diccionario = {"a": 1, "b": 2, "c": 3}
for valor in mi_diccionario.values():
    print(valor)

# Idea_01
numeros = [2,1,45,1]
for numero in numeros:
    a= numero + numero
    print(a)

# Idea_02
numeros =[2,3,1,5,5,3]
for x in numeros:
    a =x*numeros[4]
    print(a)

# 
import pandas as pd
data = {'Nombre': ['Alice', 'Bob', 'Charlie'],
        'Edad': [25, 30, 35],
        'Ciudad': ['NY', 'SF', 'LA']}

df = pd.DataFrame(data)

# Iterar sobre las columnas
for columna in df.columns:
    print(f'Columna: {columna}')
    print(df[columna])

