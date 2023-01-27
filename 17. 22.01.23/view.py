def show_menu() -> int:
    print("\n" + "=" * 20)
    print("Выберите необходимое действие")
    print("1. Добавить запись в датабазу")
    print("2. Удалить запись в датабазе")
    print("3. Обновить запись в датабазе")
    print("4. Показать датабазу")
    print("5. Поиск по датабазе")
    print("6. Импоптировать данные")
    print("7. Экспортирование данных")
    print("8. Закончить работу")
    return int(input("Введите номер необходимого действия: "))


def table_options() -> int:
    print("\n" + "=" * 20)
    print("Выберите необходимую таблицу")
    print("1. Работники")
    print("2. Должности")
    return int(input("Введите номер необходимого действия: "))


def extension_options() -> int:
    print("\n" + "=" * 20)
    print("Выберите необходимое расширение файла")
    print("1. JSON")
    print("2. CSV")
    return int(input("Введите номер необходимого действия: "))


def file_path() -> str:
    print("\n" + "=" * 20)
    return input(r'Введите путь к назначенному файлу (включая его название): ')


def input_worker() -> tuple:
    print("\n" + "=" * 20)
    full_name: str = input("Фио: ")
    age: int = int(input("Возраст: "))
    salary: int = int(input("Зарплата: "))
    pos_id: int = int(input("ID должности"))
    return full_name, age, salary, pos_id


def w_criteria_options() -> int:
    print("\n" + "=" * 20)
    print("Выберите критерий поиска: ")
    print("1. ID")
    print("2. ФИО")
    print("3. Возраст")
    print("4. Зарплата")
    print("5. ID должности")
    return int(input("Введите номер необходимого действия: "))


def input_position() -> str:
    print("\n" + "=" * 20)
    title: str = input("Должность: ")
    return title


def p_criteria_options() -> int:
    print("\n" + "=" * 20)
    print("Выберите критерий поиска: ")
    print("1. ID")
    print("2. Должность")
    return int(input("Введите номер необходимого действия: "))


def search_w_key(criteria) -> str:
    print("\n" + "=" * 20)
    if criteria == 1:
        return input("Введите ID: ")
    elif criteria == 2:
        return input("Введите ФИО: ")
    elif criteria == 3:
        return input("Введите возраст: ")
    elif criteria == 4:
        return input("Введите зарплату: ")
    elif criteria == 5:
        return input("Введите ID должности: ")


def search_p_key(criteria) -> str:
    print("\n" + "=" * 20)
    if criteria == 1:
        return input("Введите ID: ")
    elif criteria == 2:
        return input("Введите должность: ")


def search_mode() -> int:
    print("\n" + "=" * 20)
    print("Выберите режим поиска: ")
    print("1. Больше")
    print("2. Меньше")
    print("3. Равно")
    return int(input("Введите номер необходимого действия: "))


def input_id() -> int:
    print("\n" + "=" * 20)
    return int(input("Введите id, запись которого хотите выбрать: "))


def info(message) -> None:
    print("\n" + "=" * 20)
    print(message)


def import_confirm() -> int:
    print("\n" + "=" * 20)
    print("Вы точно хотите импортировать датабазу? Текущая датабаза будет потеряна.")
    print("1. Да")
    print("2. Нет")
    return int(input("Введите номер необходимого действия: "))


def exit_confirm() -> int:
    print("\n" + "=" * 20)
    print("Вы точно хотите выйти? Все несохраненные данные будут потеряны.")
    print("1. Да")
    print("2. Нет")
    return int(input("Введите номер необходимого действия: "))
