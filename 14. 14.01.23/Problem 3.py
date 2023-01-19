# Создайте программу для игры в ""Крестики-нолики"".
# Достаточно громоздко, но самое главное работает.

import random


def WinCombination(board):
    combinations = [[(board[(i * 3) + j], (i * 3) + 1 + j) for i in range(3)] for j in range(3)]
    combinations += [[(board[i + (j * 3)], (i + 1) + (j * 3)) for i in range(3)] for j in range(3)]
    combinations += [[(board[0], 1), (board[4], 5), (board[8], 9)], [(board[2], 3), (board[4], 5), (board[6], 7)]]
    return combinations


def CheckWin(board, move):
    win = 0
    combinations = WinCombination(board)
    for i in combinations:
        count = [0, 0, 0]
        for j in range(len(i)):
            count[i[j][0]] += 1
        count.pop(0)
        if 3 in count:
            win = move
            break
    if 0 not in board:
        win = 3
    return win


def CheckNearWin(board, player2):
    combinations = WinCombination(board)
    totalcount = []
    for i in combinations:
        count = [0, 0, 0]
        for j in range(len(i)):
            count[i[j][0]] += 1
        count.pop(0)
        totalcount.append(count)
    for i in range(len(totalcount) * 2):
        if i < 8:
            if 2 in totalcount[i] and sum(totalcount[i]) != 3:
                for j in range(len(combinations[i])):
                    if combinations[i][j][0] == 0 and totalcount[i][player2 - 1] == 2:
                        return combinations[i][j][1]
        else:
            i = i % 8
            if 2 in totalcount[i] and sum(totalcount[i]) != 3:
                for j in range(len(combinations[i])):
                    if combinations[i][j][0] == 0:
                        return combinations[i][j][1]
    return 0


def BoardShow(board):
    split = "──┼───┼──\n"
    text = ""
    for i in range(9):
        if board[i] == 0:
            text += str(i + 1)
        elif board[i] == 1:
            text += "X"
        else:
            text += "O"
    print(f'{text[0]} | {text[1]} | {text[2]}\n{split}{text[3]} | {text[4]} | {text[5]}\n{split}{text[6]} | {text[7]} | {text[8]}')


def MoveLegality(board, square):
    if board[square - 1] == 0:
        return False
    else:
        return True


def MoveHuman(board, move):
    square = 0
    while (square <= 0 or square > 9 or MoveLegality(board, square)):
        square = int(input(f'Ход {move} игрока: '))
        if (square <= 0 or square > 9):
            print("Неправильное ход")
        elif MoveLegality(board, square):
            print("Это занятая клетка")
    return square


def MoveEasy(board, move):
    square = 0
    while square == 0 or MoveLegality(board, square):
        square = random.randint(1, 9)
    print(f'Ход {move} игрока: {square}')
    return square


def MoveHard(board, move, player2):
    square = CheckNearWin(board, player2)
    if square == 0:
        return MoveEasy(board, move)
    else:
        print(f'Ход {move} игрока: {square}')
        return square


def Game(difficulty, player):
    board = [0 for i in range(9)]
    player1 = player
    player2 = player % 2 + 1
    move = player - 1
    while not CheckWin(board, move):
        BoardShow(board)
        move = move % 2 + 1
        if move == 1:
            board[MoveHuman(board, move) - 1] = player1
        else:
            if difficulty == 1:
                board[MoveHuman(board, move) - 1] = player2
            elif difficulty == 2:
                board[MoveEasy(board, move) - 1] = player2
            elif difficulty == 3:
                board[MoveHard(board, move, player2) - 1] = player2
    BoardShow(board)
    if CheckWin(board, move) == 3:
        print("Ничья")
    else:
        print(f'Победил {move} игрок')


difficulty = int(input("Введите сложность: \n1. Против игрока.\n2. Против легкого бота.\n3. Против сложного бота.\n"))

player = int(input("Кем будете играть: \n1. X\n2. O\n3. Рандом\n"))

if player == 3:
    player = random.randint(1, 2)

Game(difficulty, player)
