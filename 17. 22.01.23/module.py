from Position import Position
from Worker import Worker
from DataBase import DataBase
import json
from operator import methodcaller

db: DataBase = DataBase()


def add_worker(info):
    global db
    full_name, age, salary, pos_id = info
    worker: Worker = Worker(find_unsigned_id(db.worker_table), full_name, age, salary, pos_id)
    db.append_worker(worker)
    return worker


def add_position(info):
    global db
    title = info
    pos: Position = Position(find_unsigned_id(db.pos_table), title)
    db.append_position(pos)
    return pos


def delete_worker(info):
    global db
    db.remove_worker(info)
    return "Удаление завершено"


def delete_position(info):
    global db
    db.remove_position(info)
    return "Удаление завершено"


def rewrite_worker(id, info):
    global db
    full_name, age, salary, pos_id = info
    worker: Worker = Worker(id, full_name, age, salary, pos_id)
    db.update_worker(worker)
    return worker


def rewrite_position(id, info):
    global db
    title = info
    pos: Position = Position(id, title)
    db.update_position(pos)
    return pos


def show_table(table):
    return db.select_table(table)


def find_table_entry(table, criteria, key, mode):
    if table == 1:
        return db.search_worker(criteria, key, mode)
    if table == 2:
        return db.search_position(criteria, key, mode)


def temp_database(data):
    tempdb: DataBase = DataBase()

    for i in range(2):
        for j in data[i]:
            value = j
            if i == 0:
                tempworker: Worker = Worker(value[0], value[1], value[2], value[3], value[4])
                tempdb.append_worker(tempworker)
            elif i == 1:
                temppos: Position = Position(value[0], value[1])
                tempdb.append_position(temppos)
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

        data = [[], []]

        for i in range(2, len(raw_data)):
            lst = []
            for j in range(len(raw_data[i])):
                if raw_data[i][j].isdigit():
                    raw_data[i][j] = int(raw_data[i][j])
                if raw_data[i][j] != "":
                    lst.append(raw_data[i][j])
                if j % 3 == 2 and j > 3:
                    if len(lst) > 0:
                        data[j // 3 - 1].append(lst)
                    lst = []

    db = temp_database(data)
    return "Импортирование завершено"


def export_to_file(extension, file_path):
    if extension == 1:
        with open(f'{file_path}.json', 'w') as file:
            file.write(json.dumps(db.export_data()))

    elif extension == 2:
        output = [["", "Работники", "", "", "", "", "", "Должности", ""], []]
        data = db.export_data()

        for i, value in enumerate(list(data.values())):
            output[1] += list(value[0].keys()) + [""]
            for j in range(len(value)):
                if len(output) <= j + 2:
                    temp = []
                    for k in range(i * 6):
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
