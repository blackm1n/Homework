from math import sqrt
from random import randint
from typing import Callable
import csv
import json
import os


def csv_solve(file_path: str) -> Callable:
    def deco(func: Callable) -> Callable:
        result = dict()

        def wrapper() -> dict:
            with open(file_path, 'r', encoding="UTF-8") as file:
                csv_file = csv.reader(file)
                for line in csv_file:
                    result[str(line)] = func(*map(int, line))
            return result

        return wrapper

    return deco


def save_json(path: str = os.getcwd(), file_name: str = 'json_result') -> Callable:
    def deco(func: Callable) -> Callable:
        def wrapper(*args) -> list:
            result = func(*args)
            print(result)
            if not os.path.isdir(path):
                os.makedirs(path)
            with open(f'{os.path.join(path, file_name)}.json', 'w', encoding='UTF-8') as file:
                json.dump(result, file, indent=2)
            return result

        return wrapper

    return deco


@save_json()
@csv_solve('csv_result.csv')
def solve_x(a: int, b: int, c: int) -> tuple:
    if [a, b, c].count(0) > 1:
        if a != 0 or b != 0:
            return 0,
        else:
            return tuple()
    elif a == 0:
        return -c / b,
    elif b == 0:
        if -c / a > 0:
            return sqrt(-c / a), -sqrt(-c / a)
        else:
            return tuple()
    elif c == 0:
        return 0, -b / a
    else:
        D = (b ** 2) - (4 * a * c)
        if D > 0:
            return (-b + sqrt(D)) / (2 * a), (-b - sqrt(D)) / (2 * a)
        elif D == 0:
            return (-b + sqrt(D)) / (2 * a),
        else:
            return tuple()


def random_csv(path: str = os.getcwd(), file_name: str = "csv_result") -> None:
    if not os.path.isdir(path):
        os.makedirs(path)
    with open(f'{os.path.join(path, file_name)}.csv', 'w', encoding='UTF-8', newline='') as file:
        csv_write = csv.writer(file, dialect='excel')
        for i in range(randint(100, 1000)):
            csv_write.writerow([randint(-100, 100) for _ in range(3)])


solve_x()
