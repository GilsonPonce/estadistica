import pandas as pd
from sklearn.linear_model import LinearRegression
import numpy as np

# Cargar los datos
data = pd.read_excel('base de datos gastos.xlsx')

# Filtrar y limpiar los datos, validando que no haya valores no numéricos o NaN
# Convertir a numéricos y eliminar los NaN
data['entra'] = pd.to_numeric(data['entra'], errors='coerce')
data['sale'] = pd.to_numeric(data['sale'], errors='coerce')

# Eliminar filas con valores NaN en las columnas de interés
data = data.dropna(subset=['entra', 'sale'])

# Separar las variables independiente (entra) y dependiente (sale)
X = data[['entra']]  # Variable independiente
y = data['sale']     # Variable dependiente

# Crear el modelo de regresión lineal
modelo = LinearRegression()

# Ajustar el modelo a los datos
modelo.fit(X, y)

# Mostrar los coeficientes de la regresión
print(f"Coeficiente: {modelo.coef_[0]}")
print(f"Intercepto: {modelo.intercept_}")

# Predicción de valores (opcional)
y_pred = modelo.predict(X)

# Mostrar la puntuación R^2 (indica el ajuste del modelo)
print(f"Puntuación R^2: {modelo.score(X, y)}")
