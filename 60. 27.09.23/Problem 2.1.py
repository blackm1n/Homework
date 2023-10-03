class Triangle:

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
        if not self._check_triangle():
            raise ImpossibleTriangle('Треугольник с такими сторонами существовать не может')

    def sides(self):
        return [self.a, self.b, self.c]

    def _check_triangle(self):
        if max(self.sides()) < min(self.sides()) + sum(self.sides()) - max(self.sides()) - min(self.sides()):
            return True
        else:
            return False

    def type(self):
        triangle_type = 1

        for i in range(2, -1, -1):
            if self.sides()[i] == self.sides()[i - 1]:
                triangle_type += 1

        match triangle_type:
            case 1:
                return "Разносторонний"
            case 2:
                return "Равнобедренный"
            case 4:
                return "Равносторонний"


class ImpossibleTriangle(Exception):
    pass


tri = Triangle(3, 4, 5)
print(tri.type())
