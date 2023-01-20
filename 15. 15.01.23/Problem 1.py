# Из домашнего задания на 18.12.22 - Задача 3
# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.

# Старое решение

# table = list(map(float, input("Введите вещественные числа: ").split(", ")))
#
# count = 0
# for i in range(len(table)):
#     if table[i - count] % 1 == 0:
#         table.pop(i - count)
#         count += 1
#     else:
#         table[i - count] = round(table[i - count] % 1, 5)
#
# print(max(table) - min(table))

# Новое решение

table = list(map(lambda x : round(x % 1, 5), filter(lambda x : x % 1 != 0, list(map(float, input("Введите вещественные числа: ").split())))))

print(max(table) - min(table))