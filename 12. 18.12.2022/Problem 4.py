# Напишите программу, которая будет преобразовывать десятичное число в двоичное.

# Решение в одну строку
# print(str(bin(int(input("Введите число: "))))[2:])

def toBinary(num):
    if num == 0:
        return '0'
    if num == 1:
        return '1'
    else:
        return toBinary(num // 2) + str(num % 2)


num = int(input("Введите число: "))

print(toBinary(num))
