# CONDICIONALES
# Ejercicio n°1................................................................................
numero= 3
if numero>0:
    print("el numero es positivo hdp") 
elif numero==0:
    print("el numero es neutral, ni positivo ni negativo")
else:
    print("El numero es negativo deforme")


# Ejercicio n°2...............................................................................
puntaje = float(input("Ingrese el puntaje del estudiante: "))

if puntaje >= 90:
    clasificacion = "Excelente"
elif puntaje >= 80:
    clasificacion = "Sobresaliente"
elif puntaje >= 70:
    clasificacion = "Bueno"
elif puntaje >= 60:
    clasificacion = "Aprobado"
else:
    clasificacion = "Reprobado"

print(f"El estudiante obtuvo un puntaje de {puntaje}, lo que le clasifica como: {clasificacion}")


#Ejercicio n°3................................................................................
usuarios = {"juan": {"edad":44, "rol": "ingenierio"},
            "martin": {"edad":34, "rol": "data_ciences"},
            "agustin": {"edad":14, "rol": "tecnico"}}

"juan" in usuarios
usuarios["martin"]

inyeccion = input("ingrese el nombre del interesado, para extraer informacion: ")
inyeccion_2 = usuarios[inyeccion]
if inyeccion in usuarios:
    print(f"El empleado {inyeccion} existe y su informacion es la siguiente: {inyeccion_2}")
else:
    print(f"Lamento comunicarles que ese empleado no se encuentra en la base de datos")

# Ejercicio n°4...............................................................................
# Fijate de transformar el diccionario en df  y  hacer lo de imput, para ver si te devuelve de la misma forma
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
# Creamos consulta a base de datos, para ver si exite  un indice (index) en el dataframe llamando asi.
inyeccion= input("ingrese nombre: ")
if inyeccion  in df.index:
    print("Extiste le usuario en la base de datos")
else:
    print("NO existe ese perro")
                 
df

#Ejercicio n°5...............................................................................

# Base de datos de usuarios (simulada)
usuarios = {
    'mario_3': {'contraseña': 'clave123', 'rol': 'admin'},
    'jose_el': {'contraseña': 'secreto456', 'rol': 'usuario_normal'},
    'trujillo': {'contraseña': 'password789', 'rol': 'usuario_normal'}
}

# Solicitar al usuario que ingrese sus credenciales
nombre_usuario = input("Ingrese su nombre de usuario: ")
contraseña = input("Ingrese su contraseña: ")

# Verificar la autenticación del usuario
if nombre_usuario in usuarios and contraseña == usuarios[nombre_usuario]['contraseña']:
    # Usuario autenticado correctamente
    rol_usuario = usuarios[nombre_usuario]['rol']

    # Determinar acciones según el rol del usuario
    if rol_usuario == 'admin':
        print("Bienvenido administrador. Puedes realizar todas las acciones.")
    elif rol_usuario == 'usuario_normal':
        print("Bienvenido usuario normal. Tienes permisos limitados.")
    else:
        print("Rol desconocido.")
else:
    # Usuario no autenticado
    print("Autenticación fallida. Verifica tus credenciales.")
