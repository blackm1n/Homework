class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        return f'{self.name}, Возраст {self.age} года'


class Fish(Animal):

    def __init__(self, name, age, fin_amount):
        super().__init__(name, age)
        self.fin_amount = fin_amount

    def info(self):
        return f'Рыба {super().info()}. Имеет {self.fin_amount} плавников'


class Bird(Animal):

    def __init__(self, name, age, feather_len):
        super().__init__(name, age)
        self.feather_len = feather_len

    def info(self):
        return f'Птица {super().info()}. Длина перьев: {self.feather_len} мм'


class Cat(Animal):

    def __init__(self, name, age, tail_len):
        super().__init__(name, age)
        self.tail_len = tail_len

    def info(self):
        return f'Кот {super().info()}. Длина хвоста: {self.tail_len} мм'


class Factory:

    def __new__(cls, anim_class, name, age, attribute):
        instance = super().__new__(anim_class)
        instance.name = name
        instance.age = age
        match anim_class.__name__:
            case 'Fish':
                instance.fin_amount = attribute
            case 'Bird':
                instance.feather_len = attribute
            case 'Cat':
                instance.tail_len = attribute
        return instance


bob = Factory(Cat, 'Bob', 3, 30)
print(bob.info())
print(type(bob))