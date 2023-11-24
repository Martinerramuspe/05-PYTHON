# HERRAMIENTAS PRACTICAS PRINT,SALIDA DE DATOS------------------------
nombre= "Martin"
edad= 23
nombre="verde"
print(f"hola {nombre}, tenes {edad}") 
print(f"como estas {nombre}?, tanto tiempo!")

# VOLEANOS Y CONJUNTO------------------------------------------------
a=3
b=13
c=-5
d=3.4
print(a>b and c>d) # hay un orden de prioridad en cuanto a como llega al resultado.

# ENTRADA Y TRANSFORMACION DE DATOS---------------------------------------------------
nombre= input("digite su nombre: ")
type(nombre)
print(f"hola, como andas {nombre}?")

a= float(input("Pasame un numero: "))
b=4
c=a+b
print(f"El resultado es {c}, te parece?")

# FUNCIONE INTEGRADAS------------------------------------------------
a="3"
b= int(a)
type(b)

c= 1
d= str(c)
type(d)

n= round(4.6)
print(n)

r= len("caslaspro ")# cuenta los espacios tambien
print(r)

# EJERCICIOS--------------------------------------------------------
a= int(input("dame a:"))
b= int(input("dame b:"))
c= int(input("dame c:"))

resultado = ((a**3)+b)/(c+c*3)
print(resultado)
print(round(resultado))

# ELIMINAR ASIGNACION DE VARIABLE-----------------------------------
del variable