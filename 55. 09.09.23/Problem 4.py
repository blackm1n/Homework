def fibonacci(n: int) -> int:
    a = 0
    b = c = 1
    for _ in range(n):
        yield c
        c = a + b
        a, b = b, c


print(*fibonacci(10))