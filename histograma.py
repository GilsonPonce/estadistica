import matplotlib.pyplot as plt
import pandas as pd


data = pd.read_excel('base de datos gastos.xlsx')
campo = "entra"
data[campo] = pd.to_numeric(data[campo], errors='coerce')

# Crear el histograma
plt.hist(data[campo], bins=10, color='skyblue', edgecolor='black')
plt.title('Distribución de Gastos')
plt.xlabel('Monto de Gasto')
plt.ylabel('Frecuencia')
plt.show()
