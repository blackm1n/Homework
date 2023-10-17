import unittest


class TestUserBase(unittest.TestCase):
    def setUp(self) -> None:
        self.db = {}
        add_user(User("addedUser", 1, 1), self.db)
        self.names = ("testUser1", "test", "12389", "тест", "user", 123)
        self.ids = (78, "num", 8.23, 0, 8, -12567, 1)
        self.levels = (6, 2.37, 17, -12, "number", 3)

    def test_User_1(self):
        self.assertEqual(User(self.names[1], self.ids[0], self.levels[0]).name, self.names[1])
        self.assertEqual(User(self.names[4], self.ids[4], self.levels[5]).the_id, self.ids[4])
        self.assertEqual(User(self.names[3], self.ids[6], self.levels[0]).level, self.levels[0])

    def test_User_2(self):
        self.assertRaisesRegex(ValueError, "Имя должно быть текстового вида",
                               User, self.names[0], self.ids[2], self.levels[3])
        self.assertRaisesRegex(ValueError, "Имя должно быть текстового вида",
                               User, self.names[2], self.ids[4], self.levels[1])

    def test_User_3(self):  # Специально проваливается что-бы указать на недочет в коде написанном на семинаре
        self.assertRaisesRegex(ValueError, "Имя должно быть текстового вида",
                               User, self.names[5], self.ids[0], self.levels[0])

    def test_User_4(self):
        self.assertRaisesRegex(ValueError, "Личный идентификатор должен быть целым числом",
                               User, self.names[1], self.ids[2], self.levels[3])
        self.assertRaisesRegex(ValueError, "Личный идентификатор должен быть целым числом",
                               User, self.names[3], self.ids[5], self.levels[1])
        self.assertRaisesRegex(ValueError, "Личный идентификатор должен быть целым числом",
                               User, self.names[1], self.ids[1], self.levels[3])
        self.assertRaisesRegex(ValueError, "Личный идентификатор должен быть целым числом",
                               User, self.names[4], self.ids[3], self.levels[1])

    def test_User_5(self):
        self.assertRaisesRegex(ValueError, "Уровень доступа должен быть целым числом от 1 до 7",
                               User, self.names[4], self.ids[0], self.levels[2])
        self.assertRaisesRegex(ValueError, "Уровень доступа должен быть целым числом от 1 до 7",
                               User, self.names[3], self.ids[4], self.levels[1])
        self.assertRaisesRegex(ValueError, "Уровень доступа должен быть целым числом от 1 до 7",
                               User, self.names[1], self.ids[4], self.levels[4])
        self.assertRaisesRegex(ValueError, "Уровень доступа должен быть целым числом от 1 до 7",
                               User, self.names[3], self.ids[0], self.levels[3])

    def test_db_1(self):
        self.assertIsNone(add_user(User(self.names[1], self.ids[0], self.levels[0]), self.db))
        self.assertIsNone(add_user(User(self.names[4], self.ids[4], self.levels[5]), self.db))

    def test_db_2(self):
        self.assertRaisesRegex(Exception, "Пользователь с этим ID уже записан в базу",
                               add_user, User(self.names[3], self.ids[6], self.levels[0]), self.db)


class User:
    def __init__(self, name: str, the_id: int, level: int):
        if not isinstance(the_id, str) and not name.isalpha():
            raise ValueError('Имя должно быть текстового вида')
        self.name = name
        if not isinstance(the_id, int) or the_id <= 0:
            raise ValueError('Личный идентификатор должен быть целым числом')
        self.the_id = the_id
        if not isinstance(level, int) or level not in range(1, 8):
            raise ValueError('Уровень доступа должен быть целым числом от 1 до 7')
        self.level = level

    def __str__(self):
        return f'{self.name = }, {self.the_id = }, {self.level = }'


def worker():
    while True:
        try:
            name = input('Введите имя: ')
            the_id = int(input('Введите личный идентификатор: '))
            level = int(input('Введите уровень доступа: '))
            return User(name, the_id, level)
        except ValueError as e:
            print(e)


def add_user(user, db):
    if user.the_id in db:
        raise Exception('Пользователь с этим ID уже записан в базу')
    else:
        db[user.the_id] = (user.name, user.level)


if __name__ == '__main__':
    unittest.main(verbosity=2)
