# Из домашнего задания на 17.12.22 - Задача 3
# Задайте список из n чисел последовательности (1+1/n)**n и выведите на экран их сумму.

# Старое решение

# n = int(input("Введите число: "))
#
# sequence = []
# for i in range(1, n + 1):
#     sequence.append((1 + (1 / i)) ** i)
#
# print(sequence)
# print(sum(sequence))

# Новое решение

print(sum([(1 + (1 / i)) ** i for i in range(1, int(input("Введите число: ")) + 1)]))
