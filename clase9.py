import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA

# el data frame

data={
    'tipo_de_fruta':['manzana','banana','manzana','banana','naranja','manzana','naranja','manzana'],
    'peso':[100, None, 300, 400, 500, 600, 700, 800],
    'diametro':[7.5, 6.8, 7.2, 8.5, 6.3, 6.4, 6.6, 7.5],
    'sabor':[1, 2, 3, 4, 5, 6, 7, 8],
    'precio':[0.5, 0.7, 0.6, 0.3, 0.2, 0.1, 0.2, 0.5]
}

df_frutas=pd.DataFrame(data)

print(df_frutas)
print(df_frutas.info())
print(df_frutas.dtypes)
# en la columna tipo_de_fruta es una variable categorica nominal /no se puede comparar el valor de los datos
# los demas datos de las columnas son variables continuas podemos comparar los valores
# en este conjunto no hay valores nulos
va = df_frutas.isnull().sum()
print(f"valores nulos son: \n {va}")

#eleminamos el none
df_frutas.dropna(inplace=True)
print(df_frutas)


# graficamos la frecuencia
plt.hist(df_frutas['sabor'], bins=5, color="green", alpha=0.7)
plt.xlabel("sabor")
plt.ylabel("Frecuencia")
plt.title("Histograma de la frecuencia")
plt.show()

# graficamos la distribucion
fruta_count=df_frutas["tipo_de_fruta"].value_counts()
plt.pie(fruta_count,labels=fruta_count.index,autopct="%1.1f%%",startangle=140)
plt.axis("equal")
plt.title("distribucion de tipo de fruta")
plt.show()

# graficamos matriz de corrrlacion
correlacion= df_frutas.corr()
print(correlacion)

plt.figure(figsize=(8,6))
plt.imshow(correlacion,cmap="coolwarm",interpolation="nearest")
plt.colorbar()
plt.xticks(range(len(correlacion)),correlacion.columns,rotation=45)
plt.yticks(range(len(correlacion)),correlacion.columns)
plt.title("matriz de correlacion")
plt.show()