from random import randint


def queen_8(queens: list) -> bool:
    for i in range(len(queens) - 1):
        for j in range(i + 1, len(queens)):
            num1 = abs(queens[i][0] - queens[j][0])
            num2 = abs(queens[i][1] - queens[j][1])
            if num1 == num2 or num1 == 0 or num2 == 0:
                return False
    return True


def generate_queen_8() -> list:
    success = []
    while len(success) != 4:
        queens = []
        while len(queens) != 8:
            pos = (randint(1, 8), randint(1, 8))
            if pos not in queens:
                queens.append(pos)
        if queen_8(queens) and queens not in success:
            success.append(queens)
    return success
