# Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).

quadrant = int(input("Введите номер четверти: "))

if quadrant == 1:
    print("X = (0, +Inf); Y = (0, +Inf)")
elif quadrant == 2:
    print("X = (-Inf, 0); Y = (0, +Inf)")
elif quadrant == 3:
    print("X = (-Inf, 0); Y = (-Inf, 0)")
elif quadrant == 4:
    print("X = (0, +Inf); Y = (-Inf, 0)")
else:
    print("Не является номером четверти")