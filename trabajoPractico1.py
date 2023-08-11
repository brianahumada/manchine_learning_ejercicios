#Ejercicio 1
#Determinar si un numero ingresado por el usuario es PAR
    
num = int(input("Ingresa un numero: "))

if num % 2 == 0:
    print("El numero es par")
elif num % 2 != 0:
    print("El numero es impar")
else:
    print("No deberia entrar nunca")


#Ejercicio 2
#Determinar si un numero ingresado por el usuario esta DENTRO DEL RANGO [1,10] y es par. 
#MUESTRE UN MENSAJE EN CASO CONTRARIO 'NÚMERO FUERA DEL RANGO'


lista= list(range(1,11))
num = int(input("ingrese un numero del 1 al 10: "))
if num in lista and num % 2 == 0:
    print("El número ingresado es par y esta dentro del rango.")
else:
    print("El numero ingresado esta fuera de rango o es impar")


#Ejercicio 3
#Solicitar al usuario que ingrese 10 números. Calcule la suma de todos los números ingresados 
#y cuente cuántos de ellos son par.
num = []
def obtener_numeros():
    contador = 0
    while contador < 10:
        try: 
            numero = int(input("Ingrese un numero: "))
            num.append(numero)
            contador += 1
        except ValueError:
            print("No se puede ingresar una cadena de texto intente de nuevo")
            contador = contador -1

obtener_numeros()

# sumamos
sum = 0
pares = 0 
for numero in num:
    sum += numero
    #pares
    if numero % 2 == 0:
        pares += 1

print(f"La suma de los numeros es: {sum}")
print(f"tenemos una suma de numeros pares de {pares}")

#Ejercicio 4
#Mostrar todos los números presentes en el rango [56,1230]
#Solicitar al usuario que ingrese el rango [a,b] y muestre todos los números pertenecientes a él.

# Mostramos
numeros = range(56,1231,1)
for num in numeros:
    print(num)


a = int(input("ingresa el primer rango: "))
b = int(input("ingresa el segundo rango: "))

for num in range(a,b +1):
    print(num)

#Ejercicio 5
#Solicitar al usuario que ingrese un número, si es negativo o nulo ,
#solicitar reiteradamente hasta que ingrese un numero positivo.

while True:
    try:
        numero = input("Ingrese un numero: ")
        if numero > 0 :
            break
    except ValueError:
        print("El numero debe ser positivo.")

print("Gracias por ingresar un numero positivo")

#Ejercicio 6
#Solicitar al usuario que ingrese un número, si el número es positivo ,
#solicitar reiteradamente hasta que ingrese un numero negativo.
#Luego mostrar dicho número si es par, en caso contrario mostrar un mensaje 'número ingresado impar'.

while True:
    numero = input("ingrese un numero: ")
    if numero < 0:
        if numero % 2 == 0:
            print(f"El numero ingresado es par: {numero}")
            break
        else:
            print(f"El numero ingresado es impar")
            break 
    else:
        print("Ingrese un número negativo")

#Ejercicio 7 
#Solicitar al usuario que ingrese la cantidad de elementos del vector.
#Ingresar cada elemento del vector y calcular su promedio.AYUDA: 
#EL PROMEDIO ES LA SUMA DE TODOS LOS NÚMEROS DIVIDO LA CANTIDAD TOTAL.
#Mostrar el vector.

vector = []
cantidad = int(input("ingrese la cantidad de elementos que tendra el vector: "))

for i in range(cantidad):
    elemento = input(f"ingrese el elemento {i+1} : ")
    vector.append(elemento)

# Suma
total = sum(vector)
promedio = total / len(vector)

print(f"El promedio es: {promedio}")

# Ejercicio 8
#Solicitar a 10 usuario que ingresen los siguientes datos en el formato lista.
#['NOMBRE','APELLIDO', 'DNI','GASTOS MENSUALES DE HOGAR']
#Ingresar el final de la lista los siguientes usuarios:
#['ESTEBAN','LOPEZ', '45675400','190800.80']
#['NOELIA','ALEJA', '46906875','85900.50']
#Mostrar el vector. Eliminar el primer usuario de la lista.

datos = {}
for i in range(10):
    apellido = input("ingrese su apellido: ")
    nombre = input("ingrese su nombre: ")
    dni = input("ingrese su numero de documento: ")
    gastos = input("ingrese sus gastos mensuales: ")

    datos[f'persona N° {i+1}'] = apellido,nombre,dni,gastos

print(datos)
#eliminamos la primera entrada
key = "persona N° 1"
datos.pop(key)
print(datos)    

# Ejercicio 9
#Buscar en la web los datos pablacionales de todas las provicias de Argentina ,
#generando una lista con los siguiente información.
# ['PROVINCIA','CANTIDAD DE HABITANTES', 'CONSUMO ELECTRICO PER CAPITA','SUPERFICIE EN M^2']
# Mostrar TODOS LOS DATOS DEL LISTADO.

datos_provincias = [
    [1,'Buenos Aires',17569053, 307571],
    [2,'Catamarca', 429556, 102602],
    [3,'Chaco', 1142963,99633],
    [4,'Chubut',603120, 224686],
    [5,'Córdoba',3978984,165321],
    [6,'Corrientes',1197553, 88199],
    [7,'Entre Ríos', 1426426, 78781],
    [8,'Formosa',606041,72066],
    [9,'Jujuy',797955,53219],
    [10, 'La Pampa',366022,143440],
    [11, 'La Rioja',384607,89680],
    [12, 'Mendoza',2014533,148827],
    [13, 'Misiones',1280960,29801],
    [14, 'Neuquén',726590,94078 ],
    [15, 'Río Negro',762067, 203013],
    [16, 'Salta',1440672,155488],
    [17, 'San Juan',818234,89651],
    [18, 'San Luis',540905,76748],
    [19, 'Santa Cruz',333473,243943],
    [20, 'Santa Fe',3556522,133007],
    [21, 'Santiago del Estero',1054028,136351],
    [22, 'Tierra del Fuego, Antártida e Islas del Atlántico Sur',190641,987168],
    [23, 'Tucumán',1703186,22524]
]
print(datos_provincias)

#Ejercicio 10
#Crear una lista con información de estudianes de un colegio donde incluya los siguientes items:
# curso y división del aula del alumno
# nombre y apellidos
# DNI
# cantidad de notas en el primer trimestre
# INGRESAR CADA UNA DE ESAS NOTAS, POR EL USUARIO
# promedio del trimestre
# Mostrar todos los nombres y apellidos de los alumnos Mostrar los alumnos con promedio mayor o igual a 6

def info(num_notas, num_alumnos):
  list_alumnos = []
  for j in range(1,num_alumnos+1):
    nombre = input("Ingrese su nombre: ")
    apellido = input("Ingrese su apellido: ")
    dni = int(input("Ingrese su DNI: "))
    curso = input("Ingrese el curso: ")
    division = input("Ingrese la comision: ")
    
    list_notas = []

    for i in range (1,num_notas+1):
      notas = float(input("Ingrese la nota: "))
      list_notas.append(notas)
    promedio = round(sum(list_notas)/num_notas,2)
    alumno = [nombre,apellido, dni,curso,division,promedio]
    list_alumnos.append(alumno)
    return list_alumnos

data = info(3,25)
list_aprobados = []
for indice, valor in enumerate(data):
    if valor[5] >=6:
        list_aprobados.append(valor)
        print(f"Nombre: {valor[0]}; Apellido: {valor[1]} APROBADO")
    else:
        print(f"Nombre:{valor[0]}; Apellido: {valor[1]} DESAPROBADO")

print("ALUMNOS APROBADOS")
print(list_aprobados)