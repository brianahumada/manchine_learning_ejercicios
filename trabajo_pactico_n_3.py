import numpy as np
import matplotlib.pyplot as plt

# Trabajo practico Numero 3
"""
En esta celda, se utiliza la función np.random.rand() de NumPy para crear un array de 
números aleatorios con una forma específica. Luego, se imprime el array.
"""
#ramdon_array = np.random.randint(0,10,(4,3))
#print("Array aleatorio: ", ramdon_array)


"""
MEDIA
En esta celda, se crea un array 'array' y se utiliza la función np.mean() de NumPy 
para calcular la media del array. Luego, se imprime el resultado.
"""
#array = np.array([1, 2, 3, 4, 5])
#media = np.mean(array)
#print("Media:", media)

"""
DESVIACIÓN ESTÁNDAR
En esta celda, se crea un array 'array' y se utiliza la función np.std() de NumPy 
para calcular la desviación estándar del array. Luego, se imprime el resultado.
"""

#array = np.array([1, 2, 3, 4, 5])
#desviacion_estandar = np.std(array)
#print("Desviación estándar:", desviacion_estandar)

"""
VARIANZA
La función np.var() se utiliza para calcular la varianza de un array. Ejemplo de uso:
"""
#array = np.array([1, 2, 3, 4, 5])
#varianza = np.var(array)
#print("Varianza:", varianza)

"""
VALOR MINIMO
En esta celda, se crea un array 'array' y se utiliza la función np.min() de NumPy 
para encontrar el valor mínimo del array. Luego, se imprime el resultado.
"""
#array = np.array([1, 2, 3, 4, 5])
#matriz=np.random.randint(-3,3,(5,5))
#minimo = np.min(array)
#minimo = np.min(matriz, axis=0)
#print("Valor mínimo:", minimo)
#print( matriz)

"""
VALOR MÁXIMO
En esta celda, se crea un array 'array' y se utiliza la función np.max() de NumPy 
para encontrar el valor máximo del array. Luego, se imprime el resultado.
"""
#array = np.array([1, 2, 3, 4, 5])
#maximo = np.max(array)
#print("Valor máximo:", maximo)

"""
GRÁFICO DE DISPERCION
En esta celda, se crea un array 'x' con valores aleatorios y un array 'y' con valores aleatorios.
Luego, se utiliza la biblioteca Matplotlib para trazar un gráfico de dispersión con 'x' en el eje x y 'y' en el eje y. También se agrega etiquetas y un título al gráfico.
"""

#x = np.random.rand(100)
#y = np.random.rand(100)

#plt.scatter(x, y)
#plt.xlabel('x')
#plt.ylabel('y')
#plt.title('Gráfico de dispersión')
#plt.show()

"""
En esta celda, se crea un array 'data' con valores aleatorios siguiendo una distribución normal. 
Luego, se utiliza la biblioteca Matplotlib para trazar un histograma de 'data'. También se agrega etiquetas y un título al gráfico.
"""
#data = np.random.normal(0, 1, 1000)

#plt.hist(data, bins=30)
#plt.xlabel('Valor')
#plt.ylabel('Frecuencia')
#plt.title('Histograma')
#plt.show()

"""
MEDIANA
La función np.median() se utiliza para calcular la mediana de un array. Ejemplo de uso:
"""
#array = np.array([1, 2, 3, 4, 5])
#mediana = np.median(array)
#print("Mediana:", mediana)

"""
PORCENTILES
La función np.percentile() 
se utiliza para calcular los percentiles de un array. Ejemplo de uso:
"""
#array = np.array([1, 2, 3, 4, 5])
#percentil_50 = np.percentile(array, 50)
#print("Percentil 50:", percentil_50)

"""
APLICACIÓN DE PROBABILIDAD

Se Realiza el lanzamiento de un dado EQUILIBRADO JUSTO, de manera reiterada con las mismas 
condiciones, y se anotan sus resultados= CARA O CRUZ.

Se le pide al usuario que defina la cantidad N de lanzamientos y se calcula su 
frecuencia relativa= 'PROBABILIDAD' de obtener cara o cruz. Se obtiene los siguientes resultados:
"""
"""
n=int(input('ingrese la cantidad de simulación o lanzamientos: '))

#========= FORMA 1 DE SIMULAR LANZAMIENTO DE UN DADO============
dado=[]
cara=0
cruz=0
for i in range(n):
  dado.append(np.random.rand(1))
  dado1=np.array(dado)
  if dado1[i]<0.5:
    print('salio cara')
    print(dado[i])
    cara +=1
  else:
    print('salio cruz')
    print(dado[i])
    cruz +=1

#  mostrar la probailidad frecuencista de el lanzamiento de un dado
prom_cara=cara/n
prom_cruz=cruz/n
print('la probabilidad aproximada en '+str(n)+' lanzamientos de sacar CARA es:', prom_cara)
print('la probabilidad aproximada en '+str(n)+' lanzamientos de sacar CRUZ es:', prom_cruz)
"""
"""
#========== FORMA COMPACTA DE SIMULAR USANDO NUMPY===========
m=int(input('ingrese la cantidad de simulación o lanzamientos:'))
lanzamientos = np.random.randint(0, 2, m)

# Calcular las probabilidades

probabilidad_cara = np.sum(lanzamientos ==0 ) / len(lanzamientos)
probabilidad_sello = np.sum(lanzamientos== 1) / len(lanzamientos)

print(f"Probabilidad de cara: {probabilidad_cara:.2f}") #.2f es un formateo despues del punto mostrar solo dos fijitos
print(f"Probabilidad de sello: {probabilidad_sello:.2f}")

x=np.array(range(2))
y=np.array([probabilidad_cara, probabilidad_sello])

plt.bar(x,y)
plt.xlabel('Opción')
plt.ylabel('Frecuencia relativa')
plt.title('Histograma del lanzamiento de una moneda equilibrada')
plt.show()
"""

# EJERCICIO 1
"""
Simular el lanzamiento de un dado eqilibrado de 6 caras.

Mostrar la probabilida aproximada de obtener el número 2, 3 y 5
Graficar el histograma de las probabilidades
"""
def ejercicio1():
    # Simular lanzamientos de un dado
    m = int(input('Ingrese la cantidad de simulaciones o lanzamientos: '))
    lanzamientos = np.random.randint(1, 7, m)

    # Calcular las probabilidades aproximadas
    probabilidad_2 = np.sum(lanzamientos == 2) / len(lanzamientos)
    probabilidad_3 = np.sum(lanzamientos == 3) / len(lanzamientos)
    probabilidad_5 = np.sum(lanzamientos == 5) / len(lanzamientos)

    print(f"Probabilidad de obtener el número 2: {probabilidad_2:.2f}")
    print(f"Probabilidad de obtener el número 3: {probabilidad_3:.2f}")
    print(f"Probabilidad de obtener el número 5: {probabilidad_5:.2f}")

    # Crear un histograma de las probabilidades
    numeros = [2, 3, 5]
    probabilidades = [probabilidad_2, probabilidad_3, probabilidad_5]

    plt.bar(numeros, probabilidades)
    plt.xlabel('Número')
    plt.ylabel('Probabilidad')
    plt.title('Histograma de Probabilidades')
    plt.xticks(numeros)
    plt.ylim(0, 1)
    plt.show()

#ejercicio1()
"""
Simular el lanzamiento de un dado NO eqilibrado o cargado de 6 caras, 
de manera que las chances o probabilidades de salir 1 o 2 sean el doble de obtener otro resultado (3,4,5 o 6)

Mostrar la probabilida aproximada de obtener el número 2, 3 y 5
Graficar el histograma de las probabilidades
"""

def ejercicio2():
    lanzamientos = np.random.randint(1, 7, 200)

    m = int(input("Ingrese la cantidad de lanzamiento: "))
    
    probabilidad = [0.3, 0.3, 0.1, 0.1, 0.1, 0.1] 
    
    resultados = np.random.choice([1,2,3,4,5,6], size = m, replace=True,p= probabilidad)# p = el resultado debe ser 1 la sumatoria de todas la probabilidades

    # Calcular las probabilidades aproximadas
    probabilidad_2 = np.sum(resultados == 2) / len(resultados)
    probabilidad_3 = np.sum(resultados == 3) / len(resultados)
    probabilidad_5 = np.sum(resultados == 5) / len(resultados)

    print(f"Probabilidad de obtener el número 2: {probabilidad_2:.2f}")
    print(f"Probabilidad de obtener el número 3: {probabilidad_3:.2f}")
    print(f"Probabilidad de obtener el número 5: {probabilidad_5:.2f}")

    # Crear un histograma de las probabilidades
    numeros = [2, 3, 5]
    probabilidades = [probabilidad_2, probabilidad_3, probabilidad_5]

    plt.bar(numeros, probabilidades)
    plt.xlabel('Número')
    plt.ylabel('Probabilidad')
    plt.title('Histograma de Probabilidades')
    plt.xticks(numeros)
    plt.ylim(0, 1)
    plt.show()

#ejercicio2()
"""
Realizar la simulación del juego {piedra,papel , tijera} donde el resultado de esta simulación deberá ser lo que mi oponente elije. 
No debe considerarse la simulación de mi elección.

Calcular la probailidad aproximada que mi oponente elija, 'piedra', 'papel', o 'tijera', en N jugadas.
Realizar un grafico de barra mostrando estas probabilidad. 
Concluir algo sobre las probabilidades de estos resultados, cuando el número de jugadas se incrementa bastante.
"""

def ejercicio3():
    # Definir las opciones del juego
    opciones = ['piedra', 'papel', 'tijera']

    # Solicitar el número de jugadas
    n = int(input('Ingrese el número de jugadas: '))

    # Simular las elecciones del oponente
    elecciones_oponente = np.random.choice(opciones, size=n)

    # Calcular las probabilidades de las elecciones del oponente
    probabilidad_piedra = np.sum(elecciones_oponente == 'piedra') / n
    probabilidad_papel = np.sum(elecciones_oponente == 'papel') / n
    probabilidad_tijera = np.sum(elecciones_oponente == 'tijera') / n

    print(f"Probabilidad de que el oponente elija 'piedra': {probabilidad_piedra:.2f}")
    print(f"Probabilidad de que el oponente elija 'papel': {probabilidad_papel:.2f}")
    print(f"Probabilidad de que el oponente elija 'tijera': {probabilidad_tijera:.2f}")

    # Crear un gráfico de barras de las probabilidades
    probabilidades = [probabilidad_piedra, probabilidad_papel, probabilidad_tijera]

    plt.bar(opciones, probabilidades)
    plt.xlabel('Elección del Oponente')
    plt.ylabel('Probabilidad')
    plt.title('Probabilidad de Elecciones del Oponente en el Juego de Piedra, Papel o Tijera')
    plt.ylim(0, 1)
    plt.show()

#ejercicio3()

"""
Dada la base de datos de ventas diarias durante una semana, de un negocio con 4 productos.
- VER EJERCICIO PARTE 2 PRACTICO N 
2- Realizar el siguiente análisis de datos para poder obtener información y 
planificar una estrategia de ventas.

Calcular la media en la ventas por cada producto y la mediana. Plotear estos nuevos 
datos en un gráfico de barra.
Calcular la media en la ventas por DÍA y la mediana. Plotear estos nuevos datos en 
un gráfico de TRAZO DE LINEAS.
Realizar una conclusión en función las graficas y sugerir al menos 5 estrategias de 
venta o inversión de manera de potenciar este negocio.
Calcular el desvio estandar de los datos por cada producto y concluir para cada 
producto como es su rango de variabilidad en las ventas de los mismos.Plotear los datos 
de ventas de la semana de los productos con mayor y menor desvio estandar y evidenciar la 
variabilidad indicada en el parametro 'DESVIO ESTANDAR'
"""

def ejercicio4():
    ventas_diarias = np.array(
        #Lun,Mar,Mie,Jue,Vie,Sab,Dom
        [[20, 15, 25, 30, 18, 22, 24],  #Producto A
        [12, 20, 14, 8, 15, 18, 16],    #Producto B
        [35, 28, 32, 30, 26, 24, 30],   #Producto C
        [40, 38, 45, 42, 39, 41, 37]    #Producto D
        ]
    )


    print("Matriz de ventas diarias:",ventas_diarias)


    #Nuevos Ajustes

    # PUNTO 1- Media y Mediana por producto
    media_por_producto = np.mean(ventas_diarias, axis=1)
    mediana_por_producto = np.median(ventas_diarias, axis=1)

    # PUNTO 2-
    productos = ['Producto A', 'Producto B', 'Producto C', 'Producto D']
    plt.bar(productos, media_por_producto,color = 'r', label='Media')
    plt.bar(productos, mediana_por_producto,color = 'blue', label='Mediana', alpha=0.5)
    plt.xlabel('Producto')
    plt.ylabel('Ventas')
    plt.title('Media y Mediana de Ventas por Producto')
    plt.legend()
    plt.show()

    #  media y mediana de ventas por día
    media_por_dia = np.mean(ventas_diarias, axis=0)
    mediana_por_dia = np.median(ventas_diarias, axis=0)

    # Plotear
    dias = ['Lun', 'Mar', 'Mie', 'Jue', 'Vie', 'Sab', 'Dom']
    plt.plot(dias, media_por_dia,color = 'r', label='Media')
    plt.plot(dias, mediana_por_dia,color = 'blue', label='Mediana')
    plt.xlabel('Día')
    plt.ylabel('Ventas')
    plt.title('Media y Mediana de Ventas por Día')
    plt.legend()
    plt.show()

    # desvío estándar por cada producto
    desvio_estandar_por_producto = np.std(ventas_diarias, axis=1)

    #  productos con mayor y menor desvío estándar
    producto_mayor_desvio = productos[np.argmax(desvio_estandar_por_producto)]
    producto_menor_desvio = productos[np.argmin(desvio_estandar_por_producto)]

    # ventas de la semana para los productos con mayor y menor desvío estándar
    plt.plot(dias, ventas_diarias[np.argmax(desvio_estandar_por_producto)],color = 'r', label=producto_mayor_desvio)
    plt.plot(dias, ventas_diarias[np.argmin(desvio_estandar_por_producto)],color = 'blue', label=producto_menor_desvio)
    plt.xlabel('Día')
    plt.ylabel('Ventas')
    plt.title(f'Variabilidad en Ventas - {producto_mayor_desvio} vs {producto_menor_desvio}')
    plt.legend()
    plt.show()

    # Todos los productos graficamos
    for i, producto in enumerate(productos):
        plt.plot(dias, ventas_diarias[i], label=producto)

    plt.xlabel('Día')
    plt.ylabel('Ventas')
    plt.title('Variabilidad en Ventas - Todos los Productos')
    plt.legend()
    plt.show()

    # Conclusiones DEBO HACERLO YO SOLO.

    # Mediana y Media de productos:
    # A) No muestran diferencias significativas entre ambas variables para cada producto, no pudiendo identificar individualmente con esta información mayor
    #    perspectiva sobre cada producto.
    # B) Visiblemente los productos A y B, sobre todo el segundo representan una media y mediana considerablemente baja respecto a los otros productos.
    # C) Visiblmente en el gráfico 2 y 3 se visualizan la variación de ventas de en todos los productos en general y sobre todo en la tercera imagen los
    #    productos con mayor dispersión.
    #        1) Analizar la reposición de los productos en los dístintos días a fin de identificar si el problema es operativo.
    #        2) Realizar un histograma de ventas por unidad de los mismos días de la semana en la historia, igualando las semanas (mismo numero de semana),
    #           a fin de identificar la estacionalidad, eventualidad y comportamiento de cada producto o línea especifica.
    # D) Identifiación por producto.
    #     Producto D: Tiene un incremento significativo sobre el inicio de la semana y una caida constante hacia el fin de semana.
    #     Producto B: A priori el problema es operativo sobre la reposición ya tiene una caida profunda y luego su repunte, lo cual significa
    #                 que el producto tiene aceptación para los clientes.
    #                 Luego de solucionar en modo constante por varias semanas y ver que las gráficas son mas estables, se debe realizar un análisis de costos, precios
    #                 Exhibición del mismo para poder generar un incremento de las ventas.
    #     Producto A: Tener las mismas consideraciones mencionadas en el producto B.
    #     Producto C: A priori parece ser un producto de estacionalidad de la venta semanal, sin embargo hay que estudiar su histograma como se menciona anteriormente.

    # Conclusiones:
    #             Debido a la trasabilidad y comportamiento de cada producto, se detectan comportamientos dispares de cada uno, faltando información pertinente
    #             a fin de poder discrepar y direccionar las distintas acciones de revisión de las mismas.
    #             Si los productos mencionados no tienen historial de ventas, se puede inducir los comportamientos con los histogramas de cada categoría en la que pertenencen.



#ejercicio4()

def ejercicio4_otro():

  ventas_diarias = np.array(
      #Lun,Mar,Mie,Jue,Vie,Sab,Dom
      [
      [20, 15, 25, 30, 18, 22, 24],   #Producto A
      [12, 20, 14, 8, 15, 18, 16],    #Producto B
      [35, 28, 32, 30, 26, 24, 30],   #Producto C
      [40, 38, 45, 42, 39, 41, 37]    #Producto D
      ]
  )

  ventas_por_dia = np.sum(ventas_diarias, axis=0)
  print("Total de ventas por día:",ventas_por_dia)

  ventas_por_producto = np.sum(ventas_diarias, axis=1)
  print("Total de ventas por producto:",ventas_por_producto)

  ventas_total_semana = np.sum(ventas_por_producto)
  print("ventas total en toda la semana: ", ventas_total_semana)

  media_por_producto = np.mean(ventas_diarias, axis=1)
  print('Media por ventas semanales de un producto: \n',media_por_producto)

  mediana_por_producto = np.median(ventas_diarias, axis=1)
  print('Mediana por ventas semanales de un producto: \n',mediana_por_producto)

  productos = ['Producto A', 'Producto B', 'Producto C', 'Producto D']
  plt.bar(productos, media_por_producto, label='Media')
  plt.bar(productos, mediana_por_producto, label='Mediana', alpha=0.5, color='red')
  plt.xlabel('Productos')
  plt.ylabel('Ventas')
  plt.title('Media y Mediana de Ventas por Producto')
  plt.legend()
  plt.show()

  media_por_dia = np.mean(ventas_diarias, axis=0)
  print('Media de ventas por día: \n',media_por_dia)

  mediana_por_dia = np.median(ventas_diarias, axis=0)
  print('Mediana de ventas por día: \n',mediana_por_dia)

  dias = ['Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sábado', 'Domingo']
  plt.plot(dias, media_por_dia, marker='o', label='Media')
  plt.plot(dias, mediana_por_dia, marker='x', label='Mediana')
  plt.xlabel('Días de la semana')
  plt.ylabel('Ventas')
  plt.title('Media y Mediana de Ventas por Día')
  plt.legend()
  plt.xticks(rotation=45)
  plt.grid(True)
  plt.show()

  desvio_estandar_por_producto = np.std(ventas_diarias, axis=1)
  producto_mayor_desvio = np.argmax(desvio_estandar_por_producto)
  producto_menor_desvio = np.argmin(desvio_estandar_por_producto)

  plt.bar(range(len(desvio_estandar_por_producto)), ventas_por_producto,
          tick_label=['Producto A', 'Producto B', 'Producto C', 'Producto D'],
          color='blue', label='Ventas')
  plt.errorbar(producto_mayor_desvio, ventas_por_producto[producto_mayor_desvio],
              yerr=desvio_estandar_por_producto[producto_mayor_desvio],
              fmt='o', color='red', label='Mayor Desvío Estándar')
  plt.errorbar(producto_menor_desvio, ventas_por_producto[producto_menor_desvio],
              yerr=desvio_estandar_por_producto[producto_menor_desvio],
              fmt='o', color='green', label='Menor Desvío Estándar')
  plt.xlabel('Producto')
  plt.ylabel('Ventas')
  plt.title('Ventas por Producto con Desvío Estándar')
  plt.legend()
  plt.xticks(rotation=45)
  plt.grid(True)
  plt.show()

#ejercicio4_otro()

"""
EJERCICIO 5
Solicitar al usuario que ingrese la cantidad N de datos a cargar. Luego generar de manera 
aleatoria los siguientes datos:

SEXO= 'MASCULINO', 'FEMENINO','NO ESPECIFICA'
EDAD= entre 28 y 60 años
ALTURA= entre un rango de 165.0 mts hasta 210 mts
PESO= entre un rango de 50 y 110 kg
HORAS DE DESCANSO diario= un número decimal
HORAS DE TRABAJO/ ESTUDIO diario= un número decimal
HORAS DE EJERCICIOS diario= un número decimal
REalizar las siguientes indicaciones y extraer concluisiones sobre la información y la 
pooblación muestreada.

Generar un array de dimensión 2 (matriz), con todos los datos ordenados, permitiendo 
visualizarlos como tabla.
Suponiendo que la distribución de probabilidad de los datos muestrados de las N personas, 
se distribuyen en forma NORMAL. Encontrar la media en los datos de altura, peso, y horas de 
descanso, trabajo y ejercicios.
Graficar la muestra o distribución de los datos de pesos , y alturas en graficas separadas. 
Indicar el grado de variabilidad de sus datos
Plotear de manera conjunta y encontrar si presentan correlación los datos de peso vs altura,
Plotear de manera conjunta los datos de horas de descanso, estudio y ejercicio

"""
def ejercicio5():
  # Solicitar al usuario la cantidad de datos a cargar
  N = int(input('Ingrese la cantidad de datos a cargar: '))

  # Generar datos aleatorios
  sexo = np.random.choice(['MASCULINO', 'FEMENINO', 'NO ESPECIFICA'], size=N)
  edad = np.random.randint(28, 61, size=N)
  altura = np.around(np.random.uniform(165.0, 210.0, size=N), decimals=1)
  peso = np.around(np.random.uniform(50.0, 110.0, size=N), decimals=1)
  horas_descanso = np.random.randint(4, 10, size=N)
  horas_trabajo_estudio = np.random.randint(2, 12, size=N)
  horas_ejercicios = np.round(np.random.uniform(5, 3, size=N), decimals=1)
  
  
  # 1. Generar un array de dimensión 2 (matriz) con todos los datos ordenados
  # La transposición se realiza usando .T al final de la matriz creada con np.array. 
  # Esto es útil cuando deseas tener los atributos como columnas y 
  # las observaciones (individuos) como filas en tu matriz de datos.

  datos = np.array([sexo, edad, altura, peso, horas_descanso, horas_trabajo_estudio, horas_ejercicios]).T
  print('Datos ordenados: \n',datos)

  #ORDENAMOS
  print("tabla de datos")
  print("SEXO | EDAD | ALTURA | PESO | DESCANSO | TRABAJO/ESTUDIO | EJERCICIOS")
  for i in range(len(datos)):
    for j in range(len(datos[i])):
      print(f"{datos[i][j] }", end=" | ")
    print()
      

  # 2. Calcular la media en los datos de altura, peso y horas de descanso, trabajo y ejercicios
  media_altura = np.mean(altura)
  media_peso = np.mean(peso)
  media_descanso = np.mean(horas_descanso)
  media_trabajo_estudio = np.mean(horas_trabajo_estudio)
  media_ejercicios = np.mean(horas_ejercicios)

  print("\nMedias:")
  print(f"Altura: {media_altura:.2f} m")
  print(f"Peso: {media_peso:.2f} kg")
  print(f"Horas de Descanso: {media_descanso:.2f} horas")
  print(f"Horas de Trabajo/Estudio: {media_trabajo_estudio:.2f} horas")
  print(f"Horas de Ejercicios: {media_ejercicios:.2f} horas")

  # 3. Graficar la muestra o distribución de los datos de pesos y alturas
  plt.figure(figsize=(12, 6))

  plt.subplot(1, 2, 1)
  plt.hist(peso, bins=20, color='blue', edgecolor='black', alpha=0.7)
  plt.xlabel('Peso (kg)')
  plt.ylabel('Frecuencia')
  plt.title('Distribución de Pesos')
  plt.grid(True)

  plt.subplot(1, 2, 2)
  plt.hist(altura, bins=20, color='green', edgecolor='black', alpha=0.7)
  plt.xlabel('Altura (cm)')
  plt.ylabel('Frecuencia')
  plt.title('Distribución de Alturas')
  plt.grid(True)

  plt.tight_layout()
  plt.show()

  # 4. Plotear de manera conjunta y encontrar si presentan correlación los datos de peso vs altura
  #grafico de dispercion
  plt.figure(figsize=(8, 6))
  plt.scatter(peso, altura, color='purple', alpha=0.7)
  plt.xlabel('Peso (kg)')
  plt.ylabel('Altura (cm)')
  plt.title('Correlación entre Peso y Altura')
  plt.grid(True)
  plt.show()

  # 5. Plotear de manera conjunta los datos de horas de descanso, estudio y ejercicio
  #grafico de dispercion direrentes relaciones
  plt.figure(figsize=(8, 6))#8x6 pulgadas
  plt.scatter(horas_descanso, horas_trabajo_estudio, color='red', label='Descanso vs Trabajo/Estudio')
  plt.scatter(horas_descanso, horas_ejercicios, color='blue', label='Descanso vs Ejercicios')
  plt.scatter(horas_trabajo_estudio, horas_ejercicios, color='green', label='Trabajo/Estudio vs Ejercicios')
  plt.xlabel('Horas de Descanso')
  plt.ylabel('Horas')
  plt.title('Relaciones entre Horas de Descanso, Trabajo/Estudio y Ejercicios')
  plt.legend()
  plt.grid(True)
  plt.show()

ejercicio5()

