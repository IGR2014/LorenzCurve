def discounted_profit_analytical(P0, C, r, n):
    """
    Функція для обчислення дисконтованого прибутку аналітичним методом (через інтеграл).
    
    Параметри:
    P0 (float): Початкові капіталовкладення.
    C (float): Зростання капіталовкладень щороку.
    r (float): Відсоткова ставка.
    n (int): Кількість років.
    
    Повертає:
    float: Дисконтований прибуток.
    """
    integral_result = 0
    for t in range(1, n + 1):
        # Застосовуємо формулу інтегралу для обчислення дисконтованої суми
        integral_result += (P0 + C * t) / (1 + r) ** t
    return integral_result

def discounted_profit_approximate(P0, C, r, n, intervals=10):
    """
    Функція для обчислення дисконтованого прибутку наближеним методом.
    
    Параметри:
    P0 (float): Початкові капіталовкладення.
    C (float): Зростання капіталовкладень щороку.
    r (float): Відсоткова ставка.
    n (int): Кількість років.
    intervals (int): Кількість інтервалів для апроксимації.
    
    Повертає:
    float: Дисконтований прибуток.
    """
    interval_width = n / intervals
    approximate_result = 0
    for i in range(intervals):
        t = i * interval_width + interval_width / 2
        # Використовуємо апроксимаційний метод для обчислення дисконтованої суми
        approximate_result += (P0 + C * t) / (1 + r) ** t
    approximate_result *= interval_width
    return approximate_result

# Початкові дані
P0 = 11  # Початкові капіталовкладення
C = 1   # Зростання капіталовкладень щороку
r = 0.07  # Відсоткова ставка
n = 3   # Кількість років

# Аналітичний спосіб
analytical_result = discounted_profit_analytical(P0, C, r, n)
print(f"Дисконтований прибуток (аналітичний спосіб): {analytical_result:.2f} млн. гр. од.")

# Наближений спосіб
approximate_result = discounted_profit_approximate(P0, C, r, n, intervals=10)
print(f"Дисконтований прибуток (наближений спосіб): {approximate_result:.2f} млн. гр. од.")
