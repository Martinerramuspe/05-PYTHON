import re

# Supongamos que tienes una lista de strings en una columna
columna_str = ["cadena1", "cadena2", "cadena3"]

# Definir el patrón de expresión regular
patron = re.compile(r'$')

# Agregar ",2023" a cada elemento de la columna utilizando re.sub
columna_actualizada = [re.sub(patron, ',2023', s) for s in columna_str]

# Imprimir la columna actualizada
print(columna_actualizada)
