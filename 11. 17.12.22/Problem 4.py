# Задайте список из N элементов, заполненных числами из промежутка [-N, N]. Найдите произведение элементов на указанных позициях. Позиции хранятся в отдельном списке
import random

n = int(input("Введите N: "))

lst1 = list(random.randint(-n, n) for i in range(n))
print(lst1)

lst2 = list(map(int, input("Введите позиции чисел: ").split(", ")))

result = 1
for i in lst2:
    result *= lst1[i]

print(result)
