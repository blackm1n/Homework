# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

string = list(map(str, input("Введите строку: ").split()))

print(*[x for x in string if "абв" not in x])