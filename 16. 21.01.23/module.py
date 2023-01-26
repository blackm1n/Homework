from Person import Person
from Number import Number
from Address import Address
from DataBase import DataBase
import json
from operator import methodcaller

db: DataBase = DataBase()


def add_person(info):
    global db
    full_name, birth_date, status = info
    person: Person = Person(find_unsigned_id(db.person_table), full_name, birth_date, status)
    db.append_person(person)
    return person


def add_number(info):
    global db
    person_id, phone_number, comment = info
    number: Number = Number(find_unsigned_id(db.number_table), person_id, phone_number, comment)
    db.append_number(number)
    return number


def add_address(info):
    global db
    person_id, address_name, comment = info
    address: Address = Address(find_unsigned_id(db.address_table), person_id, address_name, comment)
    db.append_address(address)
    return address


def delete_person(info):
    global db
    db.remove_person(info)
    return "Удаление завершено"


def delete_number(info):
    global db
    db.remove_number(info)
    return "Удаление завершено"


def delete_address(info):
    global db
    db.remove_address(info)
    return "Удаление завершено"


def rewrite_person(id, info):
    global db
    full_name, birth_date, status = info
    person: Person = Person(id, full_name, birth_date, status)
    db.update_person(person)
    return person


def rewrite_number(id, info):
    global db
    person_id, phone_number, comment = info
    number: Number = Number(id, person_id, phone_number, comment)
    db.update_number(number)
    return number


def rewrite_address(id, info):
    global db
    person_id, address_name, comment = info
    address: Address = Address(id, person_id, address_name, comment)
    db.update_address(address)
    return address


def show_table(table):
    return db.select_table(table)


def find_table_entry(table, criteria, key, mode):
    if table == 1:
        return db.search_person(criteria, key, mode)
    if table == 2:
        return db.search_number(criteria, key, mode)
    if table == 3:
        return db.search_address(criteria, key, mode)


def temp_database(data):
    tempdb: DataBase = DataBase()

    for i in range(3):
        for j in data[i]:
            value = j
            if i == 0:
                tempperson: Person = Person(value[0], value[1], value[2], value[3])
                tempdb.append_person(tempperson)
            if i == 1:
                tempnumber: Number = Number(value[0], value[1], value[2], value[3])
                tempdb.append_number(tempnumber)
            if i == 2:
                tempaddress: Address = Address(value[0], value[1], value[2], value[3])
                tempdb.append_address(tempaddress)
    return tempdb


def import_file(extension, file_path):
    global db
    data = []
    if extension == 1:
        with open(f'{file_path}.json', 'r') as file:
            raw_data = json.loads(file.read())

        data = list(raw_data.values())

        for i in data:
            for j in range(len(i)):
                i[j] = list(i[j].values())

    elif extension == 2:
        with open(f'{file_path}.csv', 'r') as file:
            raw_data = list(map(methodcaller("split", ";"), file.readlines()))

        for i in raw_data:
            i.pop()

        data = [[], [], []]

        for i in range(2, len(raw_data)):
            lst = []
            for j in range(len(raw_data[i])):
                if raw_data[i][j] != "":
                    lst.append(raw_data[i][j])
                if j % 5 == 4:
                    if len(lst) > 0:
                        data[j // 5].append(lst)
                    lst = []

    db = temp_database(data)
    return "Импортирование завершено"


def export_to_file(extension, file_path):
    if extension == 1:
        with open(f'{file_path}.json', 'w') as file:
            file.write(json.dumps(db.export_data()))

    elif extension == 2:
        output = [["", "Люди", "", "", "", "", "Телефоны", "", "", "", "", "Адреса", "", "", ""], []]
        data = db.export_data()

        for i, value in enumerate(list(data.values())):
            output[1] += list(value[0].keys()) + [""]
            for j in range(len(value)):
                if len(output) <= j + 2:
                    temp = []
                    for k in range(i * 5):
                        temp.append("")
                    output.append(temp + list(value[j].values()) + [""])
                else:
                    output[j + 2] += list(value[j].values()) + [""]

        with open(f'{file_path}.csv', 'w') as file:
            for i in output:
                for j in i:
                    file.write(f'{j};')
                file.write("\n")
    return "Экспортирование завершено"


def find_unsigned_id(table):
    id_list = []
    for i in table:
        id_list.append(i.id)
    id = 0
    while id in id_list:
        id += 1
    return id


def end_work():
    return exit()
