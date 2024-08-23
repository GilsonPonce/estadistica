import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_excel('base de datos gastos.xlsx')
campo = "entra"
data[campo] = pd.to_numeric(data[campo], errors='coerce')


plt.scatter(data['entra'], data['sale'], color='blue')
plt.title('Relación entre Ingresos y Gastos')
plt.xlabel('Ingresos')
plt.ylabel('Gastos')
plt.show()