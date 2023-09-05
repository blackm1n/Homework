# Достаточно громозко из-за множества различных частей, но работает

import fractions

def prime_factorization(N):
    i = 2
    factor = []
    while N >= i * 2:
        if N % i == 0:
            result = prime_factorization(N // i)
            result.append(i)
            factor += result
            return sorted(factor)
        i += 1
    if len(factor) == 0:
        factor.append(N)
    return sorted(factor)


def nod(a, b):
    prime_a = prime_factorization(a)
    prime_b = prime_factorization(b)

    j = 0
    result = 1
    if len(prime_a) > len(prime_b):
        for i in range(len(prime_a)):
            if j != len(prime_b):
                if prime_a[i] == prime_b[j]:
                    result *= prime_a[i]
                    j += 1
    else:
        for i in range(len(prime_b)):
            if j != len(prime_a):
                if prime_b[i] == prime_a[j]:
                    result *= prime_b[i]
                    j += 1

    return result

def input_fraction(str):
    set = False
    while not set:
        try:
            frac = input(str)
            if "/" in frac:
                lst = frac.split("/")
                nums = [int(num) for num in lst]
                set = True
            else:
                print("Введена не дробь")
        except:
            print("Что-то пошло не так при вводе дроби")
    return nums

def sum_fractions(frac1, frac2):
    frac = [(frac1[0] * frac2[1]) + (frac2[0] * frac1[1]), frac1[1] * frac2[1]]
    div = nod(*frac)
    return [frac[0] // div, frac[1] // div]

def mult_fractions(frac1, frac2):
    frac = [frac1[0] * frac2[0], frac1[1] * frac2[1]]
    div = nod(*frac)
    return [frac[0] // div, frac[1] // div]

def frac_to_string(frac):
    return f'{frac[0]}/{frac[1]}'

frac1 = input_fraction("Введите первую дробь: ")
frac2 = input_fraction("Введите вторую дробь: ")

print(f'Сумма: {frac_to_string(sum_fractions(frac1, frac2))}')
print(f'Произведение: {frac_to_string(mult_fractions(frac1, frac2))}')
print(f'Проверенная сумма: {fractions.Fraction(*frac1) + fractions.Fraction(*frac2)}')
print(f'Проверенное произведение: {fractions.Fraction(*frac1) * fractions.Fraction(*frac2)}')