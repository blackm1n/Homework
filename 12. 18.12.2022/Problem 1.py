# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.

table = list(map(int, input("Введите числа: ").split(", ")))

result = 0
for i in range(len(table)):
    if (i + 1) % 2 == 1:
        result += table[i]

print(result)