from random import randint


def input_number(str):
    set = False
    while not set:
        try:
            n = int(input(str))
            set = True
        except:
            print("Что-то пошло не так при вводе числа")
    return n


def guess_number():
    num = randint(0, 1000)
    attempts = 1
    win = False
    while attempts <= 10 and not win:
        attempts += 1
        guess = input_number("Угадайте число от 0 до 1000: ")
        if guess != num:
            if guess > num:
                hint = "меньше"
            else:
                hint = "больше"
            print(f'Не получилось. Число {hint} указанного. Осталось {str(10 - attempts + 1)} попыток.')
        else:
            win = True
    if win:
        print("Вы угадали!")
    else:
        print("Израсходавоны все попытки.")


guess_number()
