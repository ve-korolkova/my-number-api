import matplotlib.pyplot as plt

# Данные
data1 = [5, 6, 7, 8, 9]  # для статистики
data2 = [2, 3, 4]         # для визуализации

# Визуализация: боксплот двух рядов
plt.boxplot([data1, data2], labels=['Ряд 1', 'Ряд 2'])
plt.title('Сравнение двух рядов данных')
plt.ylabel('Значения')
plt.grid(True, alpha=0.3)
plt.show()
