import pandas as pd

# Supongamos que df1 y df2 son tus DataFrames originales
# con al menos una columna con el mismo nombre

# Crear ejemplos de DataFrames
df1 = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6], 'C': [7, 8, 9], 'D': [10, 11, 12]})
df2 = pd.DataFrame({'A': [13, 14, 15]})

# Concatenar DataFrames a lo largo de las filas (axis=0)
result = pd.concat([df1, df2], axis=0)

# Imprimir el resultado
print(result)
zimport pandas as pd

# Supongamos que df1 y df2 son tus DataFrames originales
# con al menos una columna con el mismo nombre

# Crear ejemplos de DataFrames
df1 = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6], 'C': [7, 8, 9], 'D': [10, 11, 12]})
df2 = pd.DataFrame({'A': [13, 14, 15]})

# Concatenar DataFrames a lo largo de las filas (axis=0)
result = pd.concat([df1, df2], axis=0)

# Imprimir el resultado
print(result)
