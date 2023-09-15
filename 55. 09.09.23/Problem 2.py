import os


def path_to_tuple(path: str) -> tuple:
    lst = path.split(os.sep)
    file = lst[len(lst) - 1].split(".")
    return os.sep.join(lst[:-1]), file[0], file[1]


print(path_to_tuple("C:\\Users\\modny\\AppData\\Local\\Programs\\Python\\Python3113\\python.exe"))