import pandas as pd
import numpy as np

data = {
    'Columna_1': [1, 2, np.nan, 4,5,5,5,1,3,4,2,7,3,1],
    'Columna_2': [5, np.nan, 7, 8,5,5,5,5,3,2,1,1,5,5],
    'Columna_3': [9, 10, 11, np.nan,5,5,5,7,6,5,6,7,8,1],
    'Columna_4': [np.nan, 14, 15, 16,5,5,5,1,2,1,1,1,1,2]
}
df = pd.DataFrame(data)

(df["Columna_1"].isnull()).any() # Para encontrar, al menos un valor nulo
(df["Columna_4"].isnull()).idxmax() # Para encontrar, al primera valor nulo partiendo desde index =0
int(df.at[1, "Columna_1"])  # Buscamos un valor dentro de variable, usando indice.

correlation_matrix = df.corr()
print(correlation_matrix)
type(correlation_matrix)

valor_mas_grande = df.max().max()
correlation_matrix .max()