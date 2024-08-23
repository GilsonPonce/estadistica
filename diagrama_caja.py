import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_excel('base de datos gastos.xlsx')
campo = "entra"
data[campo] = pd.to_numeric(data[campo], errors='coerce')

plt.boxplot(data[campo])
plt.title('Diagrama de Caja de los Gastos')
plt.ylabel('Monto de Gasto')
plt.show()
