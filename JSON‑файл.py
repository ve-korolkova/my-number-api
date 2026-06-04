python
import json

# Генерируем список из 1 400 чисел (от 1 до 1 400)
numbers = list(range(1, 1401))

# Сохраняем в файл
with open('numbers.json', 'w') as f:
    json.dump(numbers, f)