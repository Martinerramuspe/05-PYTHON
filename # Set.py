# SET

# COMPLEJIDAD 1-------------------------------------------------------------------------------------
usuarios_0 ={"juan",1,"mario",2.2,"calaspro","trujillo"}
type(usuarios_0)
# Obersvacion_01: No se puede acceder a los elemento dentro del mismo, mendiante indices, como lo hacemos en el resto de objetos.
# Observacion_01: A diferencia de las listas estas, no importan el orden de los elementos.

# Buscamos los elemento dentros de set, usando if, la unica forma.
entrada= int(input("Ingresar valor:"))
if entrada in usuarios_0:
    print(f"existe el numero {entrada} en tu set primitivo")
else:
    print(f"No existe el valor {entrada} en este set primitivo")