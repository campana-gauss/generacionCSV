import pandas as pd
import numpy as np
from scipy.stats import norm
import matplotlib.pyplot as plt

# Cabecera con la nueva columna 'id'
cabecera = ['id', 'edad', 'altura', 'peso', 'nota_final', 'genero']

# Rangos de los parámetros
rangos = {
    'edad': (20, 25),
    'altura': (160, 180),
    'peso': (60, 70),
    'nota_final': (7, 9),
    'genero': ['Masculino', 'Femenino']
}


# Función para generar los datos
def generar_datos():
    datos = {}
    # Generar ID secuencial
    datos['id'] = np.arange(1, 1001)

    for parametro in cabecera[1:]:  # Comenzamos desde 'edad' en adelante, ya que 'id' ya lo tenemos
        if parametro == 'genero':
            datos[parametro] = np.random.choice(rangos[parametro], 1000)
        else:
            datos[parametro] = np.random.normal(rangos[parametro][0], (rangos[parametro][1] - rangos[parametro][0]) / 4,
                                                1000)

    return pd.DataFrame(datos)


# Función para comparar datos con una distribución normal
def comparar_datos(df, parametro):
    mu, sigma = df[parametro].mean(), df[parametro].std()
    x = np.linspace(mu - 3 * sigma, mu + 3 * sigma, 100)
    fp = norm.pdf(x, mu, sigma)
    plt.plot(x, fp, color='r')
    df[parametro].plot.hist(bins=20, density=True, alpha=0.6, color='g')
    plt.title('Distribución Normal y Datos Aleatorios')
    plt.xlabel('Valores')
    plt.ylabel('Probabilidad')
    plt.show()


# Generar los datos
df = generar_datos()
df[['edad', 'altura', 'peso', 'nota_final']] = df[['edad', 'altura', 'peso', 'nota_final']].round(2)

# Guardar en un archivo CSV
df.to_csv('datos_estudiantes.csv', index=False)

# Comparar las distribuciones
for parametro in cabecera[1:-1]:  # Excluimos 'id' y 'genero' para las comparaciones
    comparar_datos(df, parametro)