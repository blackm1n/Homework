for i in range(10):
    for j in range(10):
        if i == 0 and j == 0:
            print(" " * 3, end=" ")
        elif i == 0:
            print(f'{j + 1:3}', end=" ")
        elif j == 0:
            print(f'{i + 1:3}', end=" ")
        else:
            print(f'{(i + 1) * (j + 1):3}', end=" ")
    print()