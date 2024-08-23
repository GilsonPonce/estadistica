import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_excel('base de datos gastos.xlsx')
campo = "entra"
data[campo] = pd.to_numeric(data[campo], errors='coerce')

data['fecha'] = pd.to_datetime(data['fecha'])
data.sort_values(by='fecha', inplace=True)
plt.plot(data['fecha'], data['sale'], color='green')
plt.title('Tendencia de los Gastos en el Tiempo')
plt.xlabel('Fecha')
plt.ylabel('Gastos')
plt.show()