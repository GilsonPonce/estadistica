import pandas as pd
from scipy import stats

# Cargar los datos
data = pd.read_excel('base de datos gastos.xlsx')

# Filtrar los datos de la categoría ALIMENTACION
gastos_alimentacion = data['sale'][data['categoria'] == 'GASTO']

gastos_alimentacion = gastos_alimentacion.dropna()

print(len(gastos_alimentacion))

gastos_alimentacion = pd.to_numeric(gastos_alimentacion, errors='coerce')


# Definir la media hipotética (100 en este caso)
mu_hipotetico = 100

# Realizar la prueba t para una muestra
t_stat, p_value = stats.ttest_1samp(gastos_alimentacion, mu_hipotetico)

# Mostrar los resultados
print(f'Estadístico t: {t_stat}')
print(f'Valor p: {p_value}')

# Decisión
alpha = 0.05
if p_value < alpha:
    print("Rechazamos la hipótesis nula")
else:
    print("No podemos rechazar la hipótesis nula")
