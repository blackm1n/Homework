from random import randint


class Matrix:

    def __init__(self, data=None, *, width=randint(2, 10), height=randint(2, 10)):
        if data:
            self.data = data
            self.height = len(data)
            self.width = len(data[0])
        else:
            self.data = [[randint(0, 9) for _ in range(width)] for _ in range(height)]
            self.width = width
            self.height = height

    def transpose(self):
        self.data = list(map(list, zip(*self.data)))

    def __str__(self):
        res = ''
        for i in range(len(self.data)):
            for j in range(len(self.data[i])):
                res += f'{self.data[i][j]} '
            res += '\n'
        return res


ma = Matrix()
print(ma)
ma.transpose()
print(ma)
