# Вычислить число c заданной точностью d

# Я не знал, какое именно число подразумевается, поэтому взял из примера число pi

from math import pi

d = len(str(float(input("Введите число от 10^-10 до 10^-1: "))))-2

print(round(pi, d))