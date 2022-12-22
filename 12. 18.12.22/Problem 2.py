# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.

table = list(map(int, input("Введите числа: ").split(", ")))

result = []
for i in range(len(table) // 2 + 1):
    result.append(table[i] * table[-i - 1])

print(result)
