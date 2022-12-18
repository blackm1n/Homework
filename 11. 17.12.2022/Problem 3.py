# Задайте список из n чисел последовательности (1+1/n)**n и выведите на экран их сумму.

n = int(input("Введите число: "))

sequence = []
for i in range(1, n + 1):
    sequence.append((1 + (1 / i)) ** i)

print(sequence)
print(sum(sequence))
