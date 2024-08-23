import pandas as pd
import numpy as np
from scipy import stats

# Cargar los datos
data = pd.read_excel('base de datos gastos.xlsx')

# Filtrar los datos de la categoría que quieres (ejemplo: ALIMENTACION)
gastos_alimentacion = data['sale'][data['categoria'] == 'GASTO']

# Convertir la columna a valores numéricos y eliminar los NaN
gastos_alimentacion = pd.to_numeric(gastos_alimentacion, errors='coerce').dropna()

# Verificar el tamaño de la muestra después de limpiar
print(f'Tamaño de la muestra: {len(gastos_alimentacion)}')

# Cálculo del intervalo de confianza al 95%
media = np.mean(gastos_alimentacion)
desviacion_estandar = np.std(gastos_alimentacion, ddof=1)  # ddof=1 para muestra
n = len(gastos_alimentacion)
intervalo_confianza = stats.t.interval(0.95, df=n-1, loc=media, scale=desviacion_estandar/np.sqrt(n))

# Mostrar el resultado
print(f"Intervalo de Confianza al 95%: {intervalo_confianza}")
