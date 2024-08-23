import pandas as pd

# Cargar los datos
data = pd.read_excel('base de datos gastos.xlsx')
campo = 'entra'

data[campo] = pd.to_numeric(data[campo], errors='coerce')


# Calcular medidas de tendencia central y dispersión para la variable 'sale' (gastos)
media = data[campo].mean()
mediana = data[campo].median()
moda = data[campo].mode()[0]
rango = data[campo].max() - data[campo].min()
varianza = data[campo].var()
desviacion_estandar = data[campo].std()
iqr = data[campo].quantile(0.75) - data[campo].quantile(0.25)

# Mostrar resultados
print(f"Media: {media}")
print(f"Mediana: {mediana}")
print(f"Moda: {moda}")
print(f"Rango: {rango}")
print(f"Varianza: {varianza}")
print(f"Desviación Estándar: {desviacion_estandar}")
print(f"Rango Intercuartílico (IQR): {iqr}")
