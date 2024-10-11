import random
import csv
import pandas as pd
import numpy as np
from scipy.stats import norm
import matplotlib.pyplot as plt

# Definir la cabecera con parámetros
cabecera = ['edad', 'altura', 'peso', 'nota_final', 'genero']

# Definir el rango de valores para cada parámetro
rangos = {
    'edad': (20, 25),
    'altura': (160, 180),
    'peso': (60, 70),
    'nota_final': (7, 9),
    'genero': ['Masculino', 'Femenino']
}

# Generar datos aleatorios para cada parámetro
datos = {}
for parametro in cabecera:
    if parametro == 'genero':
        datos[parametro] = np.random.choice(rangos[parametro], 1000)
    else:
        datos[parametro] = np.random.normal(rangos[parametro][0], (rangos[parametro][1] - rangos[parametro][0]) /4, 1000)

# Crear un DataFrame con los datos aleatorios
df = pd.DataFrame(datos)

# Ajustar los datos aleatorios para que sean razonables
df['edad'] = df['edad'].apply(lambda x: round(x))
df['altura'] = df['altura'].apply(lambda x: round(x, 2))
df['peso'] = df['peso'].apply(lambda x: round(x, 2))
df['nota_final'] = df['nota_final'].apply(lambda x: round(x, 2))

# Guardar el DataFrame en un CSV
df.to_csv('datos_aleatorios.csv', index=False)

# Función para comparar los datos con una distribución normal perfecta
def comparar_datos(csv_file, parametro):
    datos = pd.read_csv(csv_file)
    x = datos[parametro]
    media = x.mean()
    desviacion = x.std()
    x_normal = np.linspace(media - 3*desviacion, media + 3*desviacion, 100)
    pdf = norm.pdf(x_normal, media, desviacion)
    plt.hist(x, bins=20, density=True, alpha=0.6, color='g')
    plt.plot(x_normal, pdf, color='r')
    plt.title('Distribución Normal y Datos Aleatorios')
    plt.xlabel('Valores')
    plt.ylabel('Probabilidad')
    plt.show()

# Comparar los datos con una distribución normal perfecta
comparar_datos('datos_aleatorios.csv', 'edad')
comparar_datos('datos_aleatorios.csv', 'altura')
comparar_datos('datos_aleatorios.csv', 'peso')
comparar_datos('datos_aleatorios.csv', 'nota_final')