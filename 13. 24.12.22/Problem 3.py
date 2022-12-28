# Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.

table = list(map(int, input("Введите числа: ").split(", ")))

popped = 0
for i in range(len(table)):
    if table.count(table[i - popped]) > 1:
        table.pop(i - popped)
        popped += 1

print(table)