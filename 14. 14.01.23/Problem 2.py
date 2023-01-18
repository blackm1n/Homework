# Создайте программу для игры с конфетами человек против человека.

import random


def MoveHuman(move):
    count = 0
    while (count <= 0 or count > 28):
        count = int(input(f'Ход {move} игрока: '))
        if (count <= 0 or count > 28):
            print("Неправильное число конфет")
    return count


def MoveEasy(move):
    count = random.randint(1, 28)
    print(f'Ход {move} игрока: {count}')
    return count


def MoveHard(candy, move):
    if candy % 29 == 0:
        count = random.randint(1, 28)
    else:
        count = candy % 29
        if count == 0:
            count = 1
    print(f'Ход {move} игрока: {count}')
    return count


def Game(candy, difficulty):
    move = random.randint(0, 1)
    while (candy > 0):
        print(f'Конфет - {candy}')
        move = move % 2 + 1
        if move == 1:
            candy -= MoveHuman(move)
        else:
            if difficulty == 1:
                candy -= MoveHuman(move)
            elif difficulty == 2:
                candy -= MoveEasy(move)
            elif difficulty == 3:
                candy -= MoveHard(candy, move)
        if (candy <= 0):
            print(f'Победил {move} игрок')


candy = int(input("Введите количество конфет. Стандарт: 2021\n"))
difficulty = int(input("Введите сложность: \n1. Против игрока.\n2. Против легкого бота.\n3. Против сложного бота.\n"))

Game(candy, difficulty)
