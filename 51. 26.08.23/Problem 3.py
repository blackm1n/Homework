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


def check_prime(N):
    factorization = prime_factorization(N)
    if len(factorization) > 1:
        return "Составное"
    else:
        return "Простое"


def input_number(str):
    set = False
    while not set:
        try:
            N1 = int(input(str))
            if N1 < 0:
                print("Число не может быть отрицательным")
            elif N1 > 99999:
                print("Число не может быть выше 100 тысяч")
            else:
                N = N1
                set = True
        except:
            print("Что-то пошло не так при вводе числа")
    return N


N = input_number("Введите число: ")

print(check_prime(N))
