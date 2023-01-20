# Из семинара 18.12.22 - Задача 1

# Старое решение

# import random
#
# n = int(input("Введите количество букв: "))
#
# text = ''
# for i in range(n):
#     if random.randint(0, 2) == 0:
#         text += 'О'
#     else:
#         text += 'Р'
#
# print(text)
#
# maxp = p = 0
# for i in text:
#     if i == 'Р':
#         p += 1
#         if p > maxp:
#             maxp = p
#     else:
#         p = 0
#
# print(maxp)

# Новое решение

import random

text = "".join(["O" if random.randint(0, 1) == 0 else "P" for i in range(int(input("Введите количество букв: ")))])

print(text)

maxp = p = 0
for i in text:
    if i == 'Р':
        p += 1
        if p > maxp:
            maxp = p
    else:
        p = 0

print(maxp)