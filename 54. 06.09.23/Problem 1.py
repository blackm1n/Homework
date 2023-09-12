from random import randint


def transpose(lst: list) -> list:
    return list(map(list, zip(*lst)))


width = randint(2, 10)
height = randint(2, 10)
lst = [[randint(0, 9) for _ in range(width)] for _ in range(height)]

print(*lst, sep="\n")
print()
print(*transpose(lst), sep="\n")
