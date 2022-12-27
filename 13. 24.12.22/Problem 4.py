# Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.

import random


def RandPolynomial(k):
    result = ''
    for i in range(-k, 1):
        i = -i
        coefficient = random.randint(0, 100)
        if i > 1:
            if coefficient > 2:
                result += f'{coefficient}x^{i}'
            elif coefficient == 1:
                result += f'x^{i}'
        elif i == 1:
            if coefficient > 1:
                result += f'{coefficient}x'
            elif coefficient == 1:
                result += f'x'
        else:
            if coefficient >= 1:
                result += f'{coefficient}'
            else:
                result = result[:-1]
        if coefficient >= 1 and i >= 1:
            result += '+'
    return result


k1 = int(input("Введите k1: "))
k2 = int(input("Введите k2: "))

with open('file1.txt', 'w') as file:
    poly = RandPolynomial(k1)
    file.write(poly)
    print(poly)

with open('file2.txt', 'w') as file:
    poly = RandPolynomial(k2)
    file.write(poly)
    print(poly)
