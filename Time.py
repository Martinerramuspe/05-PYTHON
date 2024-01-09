from datetime import datetime

# Fecha proporcionada
fecha_str = "Monday, September 04, 2023"

# Formato de la fecha
formato = "%A, %B %d, %Y"

# Parsear la fecha
fecha_objeto = datetime.strptime(fecha_str, formato)

# Imprimir la fecha en un formato diferente, si es necesario
print("Fecha parseada:", fecha_objeto)
