"""
# **Introducción a Pandas:**

Pandas es una biblioteca de programación en Python que proporciona estructuras de datos
 y herramientas de análisis de datos eficientes y flexibles. Está diseñada para trabajar con datos tabulares 
 y series temporales, facilitando la manipulación, limpieza y análisis de datos. A diferencia de NumPy, 
 que se enfoca en arrays multidimensionales, Pandas se especializa en estructuras de datos más flexibles 
 como DataFrames y Series.

# **Funciones similares a NumPy en Pandas:**

Pandas se construye sobre la base de NumPy y ofrece muchas funciones similares, 
pero con una capa adicional de funcionalidades específicas para el análisis de datos. 
Por ejemplo, puedes realizar operaciones vectorizadas como sumas, multiplicaciones y filtros 
en DataFrames y Series de manera similar a como lo haces en NumPy.

# **Definición de DataFrame:**

Un DataFrame es una estructura de datos bidimensional similar a una tabla de una base de datos 
o una hoja de cálculo de Excel. Consiste en una colección de columnas, donde cada columna puede 
contener datos de diferentes tipos. Los DataFrames son extremadamente útiles para manipular y 
analizar datos tabulares.

# **Composición de un DataFrame:**

Un DataFrame se compone de filas y columnas. Cada columna tiene un nombre único y 
puede contener datos de un solo tipo, como números, cadenas, fechas, etc. Las filas se indexan para acceder y 
manipular los datos. Pandas permite crear DataFrames a partir de varios tipos de datos, 
como listas, diccionarios, archivos CSV, bases de datos, entre otros.

# **Definición de Serie de Datos:**

Una Serie es una estructura de datos unidimensional en Pandas. Se puede considerar similar 
a una columna en una tabla o un array unidimensional en NumPy. Cada Serie tiene un índice 
que etiqueta los elementos individuales en la Serie, lo que permite un acceso rápido y eficiente a los datos.

# **Ploteo con Pandas:**

Pandas también ofrece herramientas de visualización básicas basadas en la biblioteca de trazado de Matplotlib. 
Puedes usar métodos como plot() en DataFrames y Series para crear gráficos simples, como líneas, barras y dispersión. 
Esto te permite visualizar tus datos de manera rápida y sencilla sin tener que escribir mucho código adicional.

En resumen, Pandas es una poderosa biblioteca en Python que facilita la manipulación y el análisis de datos tabulares. 
Puede realizarse operaciones similares a NumPy, pero con funcionalidades adicionales para la manipulación y análisis de datos 
más complejos. Los DataFrames y Series son las estructuras fundamentales de Pandas, y la biblioteca también 
proporciona herramientas básicas de visualización para ayudarte a entender tus datos de manera más efectiva.
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import listedColormap

# cargamos un diccionario con datos simulados
data = {
    'nombre':['alicia','jose','charli','david','emanuel'],
    'edad':[25,30,22,28,35],
    'altura':[165,180,170,175,160]
}

# cargamos un dataframe
df = pd.DataFrame(data)
"""
#mostramos
print("DATAFRAME")
print(df)

#-----------------CALCULOS CON NAMPY Y PANDAS------------------
#----------PROMEDIO EDAD--------------------
promedio_edad = df['edad'].mean() #media
print(f'promedio de edad: {promedio_edad}')

#altura maxima
altura_max = df['altura'].max()
print(f'La altura maxima es: {altura_max}')

#altura minima
altura_min = df['altura'].min()
print(f'La altura minima: {altura_min}')

#-------------EDAD DOBLE-------
edad_doble = df['edad']*2
print(f'Edad doble: \n',edad_doble)


#--------PLOTEO-------------
df.plot(x='nombre', y='altura', kind='bar', title='Alturas de persona')
plt.ylabel('altura (cm)')
plt.show()
"""
url = 'https://gist.githubusercontent.com/netj/8836201/raw/6f9306ad21398ea43cba4f7d537619d0e07d5ae3/iris.csv'
df = pd.read_csv(url)

#manejo de valores nulos
valores = df.isnull().sum()
print(valores)
#eliminar filas con valores nulos
nuevo_df = df.dropna()
print(nuevo_df)

#mostrar manejo de valores atipicos
#obtener estadistica descriptivas
describe = df.describe()
print(describe)

#define las distintas variables presentes en la columna variety

varieties = df['variety'].unique()
print(varieties)

#crea un mapeo de colores con la paleta de colores para el numero de varibales

cmap=plt.get('table',len(varieties))

#asignar un color unico a vada variedad utilizando el mapeo de colores
colors = [cmap(i) for i in range(len(varieties))]
df['color']= df['variety'],df['sepal.width'],c = df['color']

#crear el grafico dispercion usando los colores asignados

plt.scatter(df['sepal.length'],df['sepal.width'],c=df['color'])

#etiquetas para los ejes y muestre de grafico

plt.xlabel('longitud de sepalo')
plt.ylabel('anchura de sepalo')
plt.title('grafico de dispercion de longitud y anchura de sepalo por valor')
plt.show()