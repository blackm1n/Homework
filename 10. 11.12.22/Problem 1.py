# Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.

day = int(input("Введите номер дня недели: "))

if day in range(6, 8):
    print("Данный день является выходным")
elif day in range(1, 6):
    print("Данный день является будним")
else:
    print("Данное число не является номером дня недели")