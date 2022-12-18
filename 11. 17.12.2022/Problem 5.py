import random


def randlist(table):
    if type(table) != list:
        return print('Not a list')
    if len(table) == 1:
        return table
    for i in range(len(table) * 4):
        check = True
        while check:
            a = random.randint(0, len(table) - 1)
            b = random.randint(0, len(table) - 1)
            if a != b:
                check = False
        temp = table[a]
        table[a] = table[b]
        table[b] = temp


table = list(map(str, input("Введите массив: ").split(", ")))

print(f'До: {table}')

randlist(table)

print(f'После: {table}')