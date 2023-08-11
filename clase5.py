# ejemplo de media
import numpy as np

#creamos un array
data = np.array([2,4,6,8,10,16])
print(data)

#media
media = np.mean(data)
print(f'media: {media}')

#desvio estandar
"""el desvio 
es una medida que te dice a que distancia de la 
media se encuentran la mayoría de tus datos de la muestra"""
desvio = np.std(data)

print(f'Desvio estandar de datos: {desvio} ')

#varianza 
varianza = np.var(data)
print(f'La varianza es: {varianza}')

#valor minimo y maximo
maximo = np.amax(data)
minimo = np.amin(data)
print(f'el maximo es : {maximo}, El minimo es: {minimo}')

