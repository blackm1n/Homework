# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
def fullFibonacci(n):
    fibonacci = [0]
    if n == 0:
        return fibonacci
    elif n == 1:
        fibonacci.append(1)
    elif n > 1:
        fibonacci = fullFibonacci(n - 1)
        fibonacci.append(fullFibonacci(n - 1)[-1] + fullFibonacci(n - 2)[-1])
    fibonacci.insert(0, fibonacci[-1] * ((-1) ** (n + 1)))
    return fibonacci


n = int(input("Введите число: "))

print(fullFibonacci(n))
