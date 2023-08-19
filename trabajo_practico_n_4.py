import pandas as pd

# Ruta local al archivo CSV descargado
ruta_csv =''

# Cargar el archivo CSV en un DataFrame
df = pd.read_csv(ruta_csv)

# Mostrar las primeras filas del DataFrame
print(df.head())