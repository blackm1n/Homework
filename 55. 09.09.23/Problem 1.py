def prime_numbers(count: int) -> int:
    n = 2
    for _ in range(count):
        check = False
        while not check:
            check = True
            for i in range(2, n // 2 + 1):
                if n % i == 0:
                    check = False
                    break
            if check:
                yield n
            n += 1


print(*prime_numbers(10))