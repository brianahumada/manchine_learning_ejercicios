import numpy as np
import math
import time
import matplotlib.pyplot as plt

#hola debes descomentar para ejecutar por parte de todas formas si quieres descomentar todo y ejecutarlo deberia andar.muchas gracias por el tiempo me costo mucho abtraer las ecuaciones me gustaria que hubieran mas ejercicio sobre eso.

#Ejercicio 1
#Dada la siguiente tabla (matriz) de datos, donde cada fila representa la cantidad que se vendio en referencia a un solo producto durante toda la semana; mientras que cada columna representa la venta total en un dia de la semana.Obtener la siguiente información detallada:
# Importe total de la venta por cada dia de la semana
# Importe total de la venta por cada producto en la semana
# Importe total de la venta en toda la semana
def ejercicio1():
    ventas_diarias = np.array(
        #Lun,Mar,Mie,Jue,Vie,Sab,Dom
        [[20, 15, 25, 30, 18, 22, 24],  #Producto A
        [12, 20, 14, 8, 15, 18, 16],    #Producto B
        [35, 28, 32, 30, 26, 24, 30],   #Producto C
        [40, 38, 45, 42, 39, 41, 37]    #Producto D
        ]
    )
    #calculamos la venta de cada dia de la semana 
    def suma_total(ventas_diarias, dia):
        suma=0
        for i in range(4):
            print(ventas_diarias[i,dia])
            suma = suma +ventas_diarias[i,dia]
        valor= ""
        if dia == 0:
            valor = "Lunes"
        elif dia == 1:
            valor = "Martes"
        elif dia == 2:
            valor = "Miercoles"
        elif dia == 3:
            valor = "Jueves"
        elif dia == 4: 
            valor = "Viernes"
        elif dia == 5:
            valor = "Sabado"
        elif dia == 6:
            valor = "Domingo"

        return print(f'La suma total del dia {valor}: {suma}')
    # Descomentar para ejecutar
    #suma_total(ventas_diarias, lunes)
    #suma_total(ventas_diarias, martes)
    #suma_total(ventas_diarias, miercoles)
    #suma_total(ventas_diarias, jueves)
    #suma_total(ventas_diarias, viernes)
    #suma_total(ventas_diarias, sabado)
    #suma_total(ventas_diarias, domingo)

lunes = 0
martes = 1
miercoles = 2
jueves = 3
viernes = 4
sabado = 5
domingo = 6

# descomentar para mostrar 
#ejercicio1()



# calculamos la venta de cada producto por semana y suma total de todos los productos
def venta_producto(ventas_diarias):
    ventas_totales = 0
    for indice, fila in zip(range(len(ventas_diarias)), ventas_diarias):# usamos la zip para convinar la longitud con de la misma matriz para obtener un indice que luego usaremos para reprecentar el producto
        total = sum(fila)
        ventas_totales = ventas_totales + sum(fila)
        if indice == 0:
            producto = "A"
        elif indice == 1:
            producto = "B"
        elif indice == 2:
            producto = "C"
        elif indice == 3:
            producto = "D"

        print(f'Producto {producto}: {fila} es: {total}')
    return print(f'Ventas totales = {ventas_totales}')

#venta_producto(ventas_diarias)

# Ejercicio 2
# Crear un programa donde se le pida al usuario que ingrese la cantidad de elementos de una lista de números reales positivos. Luego Convertir esa lista en un vector de Numpy.

def programa():
    cantidad_elemento = int(input("Ingrese la cantidad de elementos de la lista: "))

    lista = []

    for i in range(cantidad_elemento):
        elemento = int(input(f"Ingrese el elemento N° {i+1}: "))
        lista.append(elemento)

    # convertimos la lista en vector con numpy
    vector = np.array(lista)
    print(f'Vector de Numpy generado con los elementos ingresados:  {vector}')

#programa()

# Ejercicio 3
# Crear un programa donde el usuario ingrese la cantidad de filas y columnas que tendra una tabla de datos. Luego el programa pedira ingresar los datos de la tabla fila por fila. Todos los datos serán numéricos.
# Mostrar la tabla ingresada en formato LISTA de Python, y mostrar la misma tabla en formato array de Numpy.
# Solicitar al usuario que ingrese las posiciones de dos filas y realice la suma de las mismas. Mostrar este vector resultado.

def programa2():
    fila = int(input("ingrese la cantidad de fila: "))
    colum = int(input("ingrese la cantidad de columnas: "))
    lista = []
    for i in range(fila):
        fila = []
        for j in range(colum):
            valor = int(input(f'Ingrese el valor de la posicion {i+1}, {j+1}: '))
            fila.append(valor)
        lista.append(fila)

    print(f'Lista en formato py: {lista}')

    # convertimos a numpy
    vector = np.array(lista)
    print(f'Mostramos la misma matriz en Numpy: {vector} ')

    #Sumamos las filas.
    #No intente romperlo las filas que debe seleccionar es de la matriz que creo que se encuentra en vector
    fila1 = int(input("ingrese una fila: "))
    fila2 = int(input("ingrese otra fila: "))
    filas_seleccionadas=[fila1,fila2]
    
    nueva_matriz = vector[filas_seleccionadas]
    
    print("la fila no coincide")

    #suma pero muestra el resultado dos veces sigo con el procimo ejercicio
    suma2= [elemento + elemento for elemento in nueva_matriz]
    suma = nueva_matriz + nueva_matriz
    #falta que muestre solo los resultados
    print(f'La suma es es: {suma.tolist()}')
    print(f'La suma es es: {suma2}')
    
# descomentar para mostrar 
#programa2()


# Ejercicio 4
#A continuación se muestran los valores de  los siguientes productos:
#['arroz', 'harina','fideo','yerba','azucar']=[145.6 , 100 , 89.90 , 700 , 95]

#Los valores de estos productos son aproximados de hace dos meses, debido a la inflación y alza de los precios, se vieron afectados de la siguiente manera:
#*   Producto arroz , harina, azucar duplicaron su precio
#*   Productos restantes incrementaron en un 75% su precio

#Mostrar los datos en forma de vector y actualizar sus precios, de manera que se pueda comparar ambos vectores.

def ejercicio4():
    productos = np.array(['arroz', 'harina','fideo','yerba','azucar'])
    precio = np.array([145.6 , 100 , 89.90 , 700 , 95])
    ordenado= np.column_stack([productos, precio]) # ordenamos
    print("MATRIZ ACTUAL")
    print(ordenado)
    precio[0] = precio[0]*2
    precio[1] = precio[1]*2
    precio[4] = precio[4]*2
    precio[2] = (0.75 * precio[2])+ precio[2]
    precio[3] = (0.75 * precio[3])+ precio[3]
    ordenado= np.column_stack([productos, precio]) # ordenamos
    print("MATRIZ MODIFICADA")
    print(ordenado)

# descomentar para mostrar 
#ejercicio4()

"""
EJERCICIO 5

Completar la siguiente tabla de comandos y funciones que se utilizarán sobre vectores definidos a través de Numpy

Comando	                                operación y funcionalidad	                      resultado	    ejemplo
1	np.array([lista])	                crea un vector o table con Numpy	              matriz	    np.array([1.6, 2, 0, 6.75])
2	np.sqrt(vector)	                    para calcular la raiz cuadrada de un vector	      raiz  	    np.sqrt(vector_np)
3	np.random.rand(n)	                para generar un vector de N°,aleatoreo rango[0,1] matriz	    np.random.rand(5)
4	np.ones((n))	                    crea un array con el rango especifico             array	        np.ones((3))
5	np.zeros((n))	                    crear array de  0	                              array	        np.zeros((3))
6	np.min(array)	                    saca el valor minumo de un array	              valor mínimo	np.min(vector_np)
7	np.max(array)		                saca el valor maximo de un array                  valor máximo	np.max(vector_np)
8	np.where(CONDICIÓN SOBRE EL VECTOR)	encontrar el indice segun la conficion	          indices 	    np.where(vector_np>1)
9	np.random.shuffle(MATRIZ)	        mezcla areatoriamente la matriz	                  matriz        np.random.shuffle(matrix)
10	array.shape[n], n=0,1	            obtener la forma del array	                      vector 	    array.shape[n] n = 0 fila 1 columnas 
11	np.sum(array, axis=n), n=0,1	    calcular la suma de un vector	                  vector        np.array(matriz, axis=n) n = 0 fila, 1 columna 
12	np.arange(a, b, p)	                crea un array especifico	                      vector 	    np.arange(0, 10, 0.1) a =inicio b =fin c=incremento

"""

"""
Funciones matemáticas sobre vectores
En esta sección, se aplican funciones matemáticas a un vector utilizando Python puro y NumPy.
Luego, se imprime el resultado de cada función.

ACLARACIÓN: Estas funciones utilizan funciones y operaciones elementales matemáticas,
sobre cada una de las posiciones del vector. Pero en general, se pueden definir funciones matemáticas que relacionan diferentes posiciones de un vector.
"""

def ejemplo():
    vector_py = [1, 2, 3, 4, 5]
    vector_np = np.array([1, 2, 3, 4, 5])
    raiz_cuadrada_py = [math.sqrt(x) for x in vector_py]
    vector_cuad=[(x**2) for x in vector_np]
    vector_log=[math.log(x) for x in vector_np]
    raiz_cuadrada_np = np.sqrt(vector_np)
    vector_npLog=np.log(vector_np)
    print("Raíz cuadrada en Python puro:", raiz_cuadrada_py)
    print("Raíz cuadrada en NumPy:", raiz_cuadrada_np)
    print('Vector al cuadrado en Python: ',vector_cuad)
    print('logaritmo de un Vector en Python: ',vector_log)
    print('logaritmo de un Vector en Numpy: ',vector_npLog)

# descomentar para mostrar 
#ejemplo()

"""
Rendimiento
En esta celda, se mide el rendimiento de operaciones en un vector utilizando Python puro y NumPy. 
Se imprime el tiempo de ejecución de cada operación.
"""
def ejemplo1():
    vector_py = [i for i in range(1000000)]
    vector_np = np.arange(1000000)

    start_time = time.time()
    [x * 2 for x in vector_py]
    end_time = time.time()
    print("Tiempo en Python puro:", end_time - start_time, "segundos")

    start_time = time.time()
    end_time = time.time()
    print("Tiempo en NumPy:", end_time - start_time, "segundos")

# descomentar para mostrar grafico
#ejemplo1()

"""
Redimensionamiento 1
En esta celda, se crea un NumPy 'array' y se utiliza la función reshape() 
de NumPy para redimensionarlo a una forma diferente. Luego, se imprime el nuevo array. 
"""
def rendimiento2():
    array = np.array([1, 2, 3, 4, 5, 6])
    nuevo_array = array.reshape((2, 3))
    print("Nuevo array redimensionado:", nuevo_array)

# descomentar para mostrar grafico
#rendimiento2()

"""
Redimensionamiento 2
En esta celda, se crea un NumPy 'array' y se utiliza la función np.resize() de NumPy 
para redimensionarlo a una forma diferente. Luego, se imprime el nuevo array.
"""

def rendimiento2():
    array = np.array([1, 2, 3, 4, 5, 6])
    nuevo_array = np.resize(array, (3, 3))
    print("Nuevo array redimensionado:", nuevo_array)

# descomentar para mostrar grafico
#rendimiento2()


"""
EJERCICIO PARTE 2
Ejercicio 1:

Dado una matriz de datos, dividir el 70% de filas en un array_entrenamiento y el otro 30% en otro array_testeo. 
Esta distribución de filas de la matriz inicial, debe ser aleatoria. Mostrar las matrices al ser modificadas 
por el comando np.random.shuffle('matriz'). Finalmente mostrar los array_entrenamiento y array_testeo.
"""

def ejercicio2_1():
    dataset = np.array([[25, 1, 7, 100, 1],
                    [30, 2, 5, 120, 0],
                    [22, 1, 6, 80, 1],
                    [28, 1, 6, 90, 0],
                    [35, 2, 4, 130, 1],
                    [32, 2, 6, 110, 1],
                    [26, 1, 8, 95, 1],
                    [24, 1, 5, 85, 0],
                    [29, 2, 7, 115, 1],
                    [31, 2, 6, 105, 0]])

    # Mezclar las filas de la matriz para obtener una distribución aleatoria de los datos
    np.random.shuffle(dataset)
    print("Matriz Aleatoria:")
    print(dataset)

    indice_separacion= int(0.7 * dataset.shape[0]) #fila y  el 70%
    
    #ordenamos y establecemos datos
    array_entrenamiento = dataset[:indice_separacion,:]
    array_testeo = dataset[indice_separacion:,:]

    print("Matriz inicial (mezclada aleatoriamente):")
    print(dataset)

    print("\nArray Entrenamiento:")
    print(array_entrenamiento)

    print("\nArray Testeo:")
    print(array_testeo)

# descomentar para mostrar grafico
#ejercicio2_1()

"""
Ejercicio 2:

Dado la siguiente tabla de datos poblaciones de las Provincias de Argentina (Ejercicio 10 del Práctico 1), 
Realizar el siguiente analisis.

indicar la cantidad de filas y columnas que posee la tabla de datos.
Mostrar toda la información de la provincia con Mayor Cantidad de habitantes. AYUDA: usar la función np.max(array)
Agregar a la tabla de datos una fila al final , indicando los totales de cada columna. Mostrar el resultado 
de la nueva tabla.
"""

def ejercicio2_2():
    poblacionArgentina1=[
    ['PROVINCIA','CANTIDAD DE HABITANTES','CONSUMO EN MWH','SUPERFICIE EN KM^2'],
    ['Buenos Aires','17.569.053',' 16543722',' 305907'],
    ['Córdoba','3.978.984',' 10606601','164708'],
    ['Santa Fe','3.556.522',' 13078203',' 133249'],
    ['Ciudad Autónoma de Buenos Aires','3.120.612','51712507',' 201'],
    ['Mendoza','2.014.533',' 5652519',' 149069'],
    ['Tucumán','1.703.186','3208711','22.524'],
    ['Salta','1.440.672',' 2214796',' 155341'],
    ['Entre Ríos','1.426.426','3906353','78384'],
    ['Misiones','1.280.960','2845762',' 29911'],
    ['Corrientes','1.197.553','2997612',' 89123'],
    ['Chaco','1.142.963','3045380',' 99763'],
    ['Santiago del Estero','1.054.028',' 1811277',' 136934'],
    ['San Juan','818.234',' 2381940',' 88296'],
    ['Jujuy','797.955',' 1136336',' 53244'],
    ['Río Negro','762.067',' 1984782','202169'],
    ['Neuquén','726.590','1834879',' 94422'],
    ['Formosa','606.041',' 1388311','75488'],
    ['Chubut','603.120','1646029',' 224302'],
    ['San Luis','540.905',' 1780881','75347'],
    ['Catamarca','429.556',' 1337032','101486'],
    ['La Rioja','384.607','1572290',' 91494'],
    ['La Pampa','366.022','915781',' 143493'],
    ['Santa Cruz','333.473',' 1025648',' 244458'],
    ['Tierra del Fuego, Antártida e Islas del Atlántico Sur','190.641',' s/d ',' 37131']]

    poblacionArgentina=np.array(poblacionArgentina1)
    print(poblacionArgentina)

    #cantidad de filas y columnas
    forma = poblacionArgentina.shape
    print(forma)
    filas = forma[0]
    columnas = forma[1]
    print(f"filas: {filas}, columnas: {columnas} ")

    
    #mayor cantidad de habitantes
    print("CALCULAR MAYOR CANTIDAD DE HABITANTES")
    clum_habitantes= poblacionArgentina[1:,1] #ignoro el encabezado
    clum_habitantes = np.array([int(i.replace('.', '')) for i in clum_habitantes]) #Cambiamos los puntos por nada y pasamos numeros
    
    print(clum_habitantes)
    valor_maximo = np.max(clum_habitantes)#valor maximo
    print(f'Valor maximo: {valor_maximo}')
    print(clum_habitantes.dtype)

    #Eliminar los puntos y convertir a enteros solo para los valores numéricos
    for i in range(1,poblacionArgentina.shape[0]):#range(1,)-empezamos a recorrer del indice 1
        for j in range(1, poblacionArgentina.shape[1]):
            #verificacion
            if poblacionArgentina[i,j].replace('.', '').isdigit():#isdigt = devuelve true si todos los caracteres de cadena son numericos
                poblacionArgentina[i ,j] = int(poblacionArgentina[i,j].replace('.', ''))

    
    #calcular totales de columnas
    habitantes1 = np.sum(poblacionArgentina[1:,1].astype(int))
    consumo = np.sum(poblacionArgentina[1:,1].astype(int))
    superfici = np.sum(poblacionArgentina[1:,1].astype(int))

    total = ['totales', f'{habitantes1}',f'{consumo}',f'{superfici}']    
    
    #Agregamos a la matriz
    poblacionArgentina = np.vstack([poblacionArgentina, total])
    print(poblacionArgentina)

# descomentar para mostrar 
#ejercicio2_2()

"""
Gráfica de funciones matemáticas elementales
En esta celda, se crea un array 'x' con valores en el rango de 0 a 10 y se utiliza la función np.sin() y np.cos()
de NumPy para calcular el seno y coseno de cada valor en 'x'. Luego, se utiliza la biblioteca Matplotlib 
para trazar un gráfico de línea con 'x' en el eje x y 'y' en el eje y. 
También se agrega etiquetas y un título al gráfico.
"""
#Ejemplo
def grafico0():
    x = np.arange(0, 10, 0.1)
    y = np.cos(x)

    plt.plot(x, y)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Gráfico de línea')
    plt.show()
# descomentar para mostrar grafico
#grafico0():
"""
Realizar las gráficas de als siguientes expresiones matemáticas. 
Determinar el dominio del eje x adecuado para plotear las funciones de manera que se visualice su comportamiento.
"""
def grafico1():
    x1 = np.linspace(-10, 10, 100)
    y1 = 3 * x1 - 2
    plt.plot(x1, y1)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Gráfico de y = 3 * x1 - 2')
    plt.show()

# descomentar para mostrar grafico
#grafico1()

def grafico2():
    x = np.linspace(-10, 10, 100)
    y = 2 * x**2 + 4 * x + 2
    plt.plot(x, y)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Gráfico de y = 2 * x**2 + 4 * x + 2')
    plt.grid(True)
    plt.show()

# descomentar para mostrar grafico
#grafico2()


def grafico3():
    x = np.linspace(-10, 100, 100)

    # Primera forma
    condicion = [x < 0, x >= 0]
    funcion = [-x[condicion[0]], x[condicion[1]]]
    y =  np.piecewise(x, condicion, funcion)
    
    #otra forma
    #y1 = np.abs(x)

    plt.plot(x, y)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Gráfico de y = [x] ')
    plt.grid(True)
    plt.show()

# descomentar para mostrar grafico
#grafico3()

def grafico4():
    #Debemos hacer que x no tome valor 0
    x = np.linspace(-10, 0.1, 200)
    x = np.concatenate([x ,np.linspace(0.1,10,200)])

    y = 1/x

    plt.plot(x, y)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Gráfico de y = [x] ')
    plt.grid(True)
    plt.show()

# descomentar para mostrar grafico
#grafico4()

def grafico5():
    x = np.linspace(0,10,200) #valores positivos

    y = np.sqrt(x)

    
    plt.plot(x, y)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Gráfico de y = [x] ')
    plt.grid(True)
    plt.show()

# descomentar para mostrar grafico
#grafico5()