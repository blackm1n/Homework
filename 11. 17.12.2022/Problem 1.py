# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

num = str(float(input("Введите число: "))).replace(".", "")

result = 0
for i in num:
    result += int(i)

print(result)