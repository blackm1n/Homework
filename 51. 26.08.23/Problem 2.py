def input_triangle():
    a = input_number("Введите первую сторону треугольника: ")
    b = input_number("Введите вторую сторону треугольника: ")
    c = input_number("Введите третью сторону треугольника: ")
    triangle = [a, b, c]
    return triangle


def input_number(str):
    set = False
    while not set:
        try:
            n = int(input(str))
            set = True
        except:
            print("Что-то пошло не так при вводе числа")
    return n


def check_triangle(triangle):
    if max(triangle) < min(triangle) + sum(triangle) - max(triangle) - min(triangle):
        return True
    else:
        return False


def iden_triangle(triangle):
    triangle_type = 1

    for i in range(2, -1, -1):
        if triangle[i] == triangle[i - 1]:
            triangle_type += 1

    match triangle_type:
        case 1:
            return "разносторонним"
        case 2:
            return "равнобедренным"
        case 4:
            return "равносторонним"


triangle = input_triangle()

if check_triangle(triangle):
    print(f'Является {iden_triangle(triangle)} треугольником')
else:
    print("Не является треугольником")
