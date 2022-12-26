# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

def PrimeFactorization(N):
    i = 2
    factor = []
    while N >= i * 2:
        if N % i == 0:
            result = PrimeFactorization(N // i)
            result.append(i)
            factor += result
            return sorted(factor)
        i += 1
    if len(factor) == 0:
        factor.append(N)
    return sorted(factor)


N = int(input("Введите число: "))

print(PrimeFactorization(N))
