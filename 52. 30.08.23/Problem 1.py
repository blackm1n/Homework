# Я пытал рандомные вещи и в конце концов получилось.

def input_number(str):
    set = False
    while not set:
        try:
            n = int(input(str))
            set = True
        except:
            print("Что-то пошло не так при вводе числа")
    return n

def to_hex(num):
    hex_letters = ["A", "B", "C", "D", "E", "F"]
    power = 1
    while 16 ** power <= num:
        power += 1
    string = ""
    while power != 0:
        digit = (num % (16 ** power)) // (16 ** (power - 1))
        string += f'{digit if (digit < 10) else hex_letters[digit - 10]}'
        num -= digit * 16 ** (power - 1) if digit > 0 else 16 ** (power - 1)
        power -= 1
    return string


num = input_number("Введите число: ")
hex_num = to_hex(num)
print(f'Шестьнадцатеричное число: {hex_num}')
print(hex(num))
