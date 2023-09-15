# Надеюсь это сойдет как однострочный генератор. Впринципе можно и без функции и тогда точно однострочный генератор
# будет, но тогда надо будет напрямую к переменным обращаться. Я оставил данное решение закомментированным.

names = ["name1", "name2"]
stakes = [5, 10]
prizes = ["6.7%", "12.8%"]


def f(names: list, stakes: list, prizes: list) -> dict:
    for i in range(len(names)):
        yield {names[i]: stakes[i] * float(prizes[i][:-1]) / 100}


print(*f(names, stakes, prizes))

# print(*({names[i]: stakes[i] * float(prizes[i][:-1]) / 100} for i in range(len(names))))
