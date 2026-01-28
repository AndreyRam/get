import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression

# Данные для графика
x = [0.133, 0.167, 0.255, 0.317, 0.397, 0]
y = [0.0687, 0.0879, 0.1322, 0.1635, 0.2069, 0]

# Убираем точку (0,0) для расчета наклона (если она не должна участвовать в линейной зависимости)
x_for_fit = [0.133, 0.167, 0.255, 0.317, 0.397]
y_for_fit = [0.0687, 0.0879, 0.1322, 0.1635, 0.2069]

# Расчет коэффициента наклона
x_array = np.array(x_for_fit).reshape(-1, 1)
y_array = np.array(y_for_fit)

model = LinearRegression()
model.fit(x_array, y_array)

slope = model.coef_[0]
intercept = model.intercept_

print(f"Коэффициент наклона (угловой коэффициент): {slope:.4f}")
print(f"Свободный член: {intercept:.4f}")
print(f"Уравнение прямой: y = {slope:.4f}x + {intercept:.4f}")

# Создание графика
plt.figure(figsize=(10, 6))

# Основные данные
plt.plot(x, y, marker='o', linestyle='-', color='blue', linewidth=2, 
         markersize=8, label='Экспериментальные данные')

# Линия регрессии
x_fit = np.linspace(min(x), max(x), 100)
y_fit = slope * x_fit + intercept
plt.plot(x_fit, y_fit, 'r--', linewidth=1.5, 
         label=f'Линейная аппроксимация (k = {slope:.4f})')

# Настройки графика
plt.title('Зависимость Y от X', fontsize=14)
plt.xlabel('Ось X', fontsize=12)
plt.ylabel('Ось Y', fontsize=12)

# Плотная сетка
plt.grid(True, alpha=0.3, which='both')
plt.minorticks_on()
plt.grid(True, alpha=0.1, which='minor')

# Легенда
plt.legend(fontsize=11, loc='upper left')

# Настройка осей
plt.xticks(fontsize=10)
plt.yticks(fontsize=10)

# Добавляем текстовое поле с информацией о наклоне
textstr = f'k = {slope:.4f}\nR² = {model.score(x_array, y_array):.4f}'
props = dict(boxstyle='round', facecolor='wheat', alpha=0.8)
plt.text(0.05, 0.95, textstr, transform=plt.gca().transAxes, fontsize=10,
         verticalalignment='top', bbox=props)

plt.tight_layout()
plt.show()

# Дополнительная информация
print(f"\nДополнительная информация:")
print(f"Коэффициент детерминации R²: {model.score(x_array, y_array):.4f}")
