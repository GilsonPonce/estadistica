import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_excel('base de datos gastos.xlsx')
campo = "entra"
data[campo] = pd.to_numeric(data[campo], errors='coerce')

media_por_categoria = data.groupby('categoria')[campo].mean()
media_por_categoria.plot(kind='bar', color='lightblue')
plt.title('Media de Gastos por Categoría')
plt.xlabel('Categoría')
plt.ylabel('Monto Promedio de Gasto')
plt.xticks(rotation=45)
plt.show()
