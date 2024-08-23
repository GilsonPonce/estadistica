import pandas as pd
import matplotlib.pyplot as plt

# Tus datos corregidos (ya cargados en un DataFrame)
data_corrected = pd.read_excel('base de datos gastos.xlsx')

# Generar la tabla de frecuencias para 'categoria'
frecuencia_categoria_corrected = data_corrected['cuenta'].value_counts()

# Crear el gráfico de barras
plt.figure(figsize=(10,6))
frecuencia_categoria_corrected.plot(kind='bar', color='skyblue')
plt.title('Frecuencia de Cuentas de Gasto')
plt.xlabel('Cuentas')
plt.ylabel('Frecuencia')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()

# Guardar el gráfico si es necesario
plt.savefig('frecuencia_cuenta_gasto.png')

# Mostrar el gráfico
plt.show()
