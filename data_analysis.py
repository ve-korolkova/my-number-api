import matplotlib.pyplot as plt

# Данные
data1 = [5, 6, 7, 8, 9]
data2 = [2, 3, 4]

# Расчёт статистических характеристик для первого ряда
mean = sum(data1) / len(data1)
median = sorted(data1)[len(data1) // 2]
spread = max(data1) - min(data1)
variance = sum((x - mean) ** 2 for x in data1) / len(data1)
std_dev = variance ** 0.5

print(f"Среднее: {mean}")
print(f"Медиана: {median}")
print(f"Размах: {spread}")
print(f"Дисперсия: {variance}")
print(f"Стандартное отклонение: {std_dev:.2f}")

# Визуализация
plt.figure(figsize=(8, 4))
plt.boxplot([data1, data2], labels=['Ряд 1 (5-9)', 'Ряд 2 (2-4)'])
plt.title('Боксплот двух рядов данных')
plt.ylabel('Значения')
plt.grid(True, alpha=0.3)
plt.show()
