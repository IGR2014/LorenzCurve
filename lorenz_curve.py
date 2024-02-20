import matplotlib.pyplot as plt
import numpy as np
from numpy import sqrt, trapz

# Функція, що обчислює значення кривої Лоренца
def lorenz_curve(x):
    return 1 - sqrt(1 - x**3)

# Функція, що обчислює коефіцієнт Джині аналітично
def gini_coefficient(data):
    sorted_data = np.sort(data)
    n = len(data)
    index = np.arange(1, n + 1)
    return (np.sum((2 * index - n - 1) * sorted_data)) / (n * np.sum(sorted_data))

# Функція, що обчислює коефіцієнт Джині за площами кривих з графіка
def gini_coefficient_area(population, lorenz_values):
    # Площа під кривою Лоренца
    area_lorenz = trapz(lorenz_values, population)
    # Коефіцієнт Джині
    return 2 * area_lorenz

# Функція, що обчислює коефіцієнт Робін Гуда
def robin_hood_coefficient(data):
    mean_income = np.mean(data)
    numerator = np.sum(np.abs(data - mean_income))
    denominator = np.sum(data)
    robin_hood = 0.5 * numerator / denominator
    return robin_hood

# Генеруємо дані для населення (х)
population = np.linspace(0, 1, 100)
# Обчислюємо відповідні значення кривої Лоренца (у)
lorenz_values = lorenz_curve(population)

# Побудова графіка кривої Лоренца
plt.plot(population, lorenz_values, label='Крива Лоренца')
plt.plot(population, population, linestyle='--', color='red', label='Лінія рівності')
plt.fill_between(population, population, lorenz_values, color='skyblue', alpha=0.5)
plt.title('Крива Лоренца, y = 1 - sqrt(1 - x^3)')
plt.xlabel('Населення (x)')
plt.ylabel('Питома вага прибутків (y)')
plt.subplots_adjust(bottom=0.25)

# Виведення коефіцієнту Джині
gini = gini_coefficient(population)
plt.figtext(0.01, 0.11, f"Коеф. Джині (аналітично): {gini:.4f}", horizontalalignment='left')
gini_area = gini_coefficient_area(population, lorenz_values)
plt.figtext(0.01, 0.06, f"Коеф. Джині (за графіком): {gini_area:.4f}", horizontalalignment='left')
robin = robin_hood_coefficient(population)
plt.figtext(0.01, 0.01, f"Індекс Робін Гуда: {robin:.4f}", horizontalalignment='left')

# Відображення графіку
plt.legend()
plt.show()

