# Данные
data1 = [5, 6, 7, 8, 9]  # для статистики
data2 = [2, 3, 4]         # для визуализации

# Сортируем оба ряда
sorted_data1 = sorted(data1)
sorted_data2 = sorted(data2)

# Находим тройку наибольших и наименьших значений для первого ряда (если возможно)
largest_3 = sorted_data1[-3:] if len(sorted_data1) >= 3 else sorted_data1
smallest_3 = sorted_data1[:3] if len(sorted_data1) >= 3 else sorted_data1

# Для второго ряда — аналогично
largest_3_2 = sorted_data2[-3:] if len(sorted_data2) >= 3 else sorted_data2
smallest_3_2 = sorted_data2[:3] if len(sorted_data2) >= 3 else sorted_data2

# Выводим результаты
print("Ряд 1 (5, 6, 7, 8, 9):")
print(f"Три наибольших: {largest_3}")
print(f"Три наименьших: {smallest_3}")

print("\nРяд 2 (2, 3, 4):")
print(f"Три наибольших: {largest_3_2}")
print(f"Три наименьших: {smallest_3_2}")
