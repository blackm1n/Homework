import datetime as dt


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
    print("1. Люди")
    print("2. Телефоны")
    print("3. Адреса")
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


def input_person() -> tuple:
    print("\n" + "=" * 20)
    full_name: str = input("Фио: ")
    birth_date: dt.date = dt.date(int(input("Д/р\nГод: ")), int(input("Месяц: ")), int(input("День: ")))
    status: str = input("Статус: ")
    return full_name, birth_date, status


def p_criteria_options() -> int:
    print("\n" + "=" * 20)
    print("Выберите критерий поиска: ")
    print("1. ID")
    print("2. ФИО")
    print("3. Д/р")
    print("4. Статус")
    return int(input("Введите номер необходимого действия: "))


def input_number() -> tuple:
    print("\n" + "=" * 20)
    person_id: int = int(input("Чей телефон: "))
    phone_number: int = int(input("Тел: "))
    comment: str = input("Комментарий: ")
    return person_id, phone_number, comment


def n_criteria_options() -> int:
    print("\n" + "=" * 20)
    print("Выберите критерий поиска: ")
    print("1. ID")
    print("2. Чей телефон")
    print("3. Тел")
    print("4. Коммент")
    return int(input("Введите номер необходимого действия: "))


def input_address() -> tuple:
    print("\n" + "=" * 20)
    person_id: int = int(input("Чей адрес: "))
    address_name: str = input("Адрес: ")
    comment: str = input("Комментарий: ")
    return person_id, address_name, comment


def a_criteria_options() -> int:
    print("\n" + "=" * 20)
    print("Выберите критерий поиска: ")
    print("1. ID")
    print("2. Чей адрес")
    print("3. Адрес")
    print("4. Коммент")
    return int(input("Введите номер необходимого действия: "))


def search_p_key(criteria) -> str:
    print("\n" + "=" * 20)
    if criteria == 1:
        return input("Введите ID: ")
    elif criteria == 2:
        return input("Введите ФИО: ")
    elif criteria == 3:
        return input("Введите дату рождения в формате ГГГГ-ММ-ДД: ")
    elif criteria == 4:
        return input("Введите статус: ")


def search_n_key(criteria) -> str:
    print("\n" + "=" * 20)
    if criteria == 1:
        return input("Введите ID: ")
    elif criteria == 2:
        return input("Введите ID человека владеющего телефоном: ")
    elif criteria == 3:
        return input("Введите номер телефона: ")
    elif criteria == 4:
        return input("Введите комментарий: ")


def search_a_key(criteria) -> str:
    print("\n" + "=" * 20)
    if criteria == 1:
        return input("Введите ID: ")
    elif criteria == 2:
        return input("Введите ID человека владеющего адресом: ")
    elif criteria == 3:
        return input("Введите адрес: ")
    elif criteria == 4:
        return input("Введите комментарий: ")


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
