import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_excel('base de datos gastos.xlsx')
campo = "entra"
data[campo] = pd.to_numeric(data[campo], errors='coerce')


data.groupby('categoria')['sale'].sum().plot(kind='pie', autopct='%1.1f%%')
plt.title('Distribución de los Gastos por Categoría')
plt.ylabel('')
plt.show()