import os
import argparse
import logging


def recurse_walk(path: str) -> list:
    file_names = []
    for file in os.listdir(path):
        file_dict = {'name': file, 'parent_dir': path.split(os.path.sep)[-1]}
        dir_result = []
        size = 0
        if os.path.isdir(os.path.join(path, file)):
            file_dict['isdir'] = True
            dir_result = recurse_walk(os.path.join(path, file))
            for res in dir_result:
                if res['parent_dir'] == file:
                    size += res['size']
        else:
            size += os.stat(os.path.join(path, file)).st_size
            file_dict['isdir'] = False
        file_dict['size'] = size
        file_names.append(file_dict)
        file_names += dir_result
    return file_names


def save_result(path: str) -> None:
    result = recurse_walk(path)
    FORMAT = '{levelname:<8} - {asctime}. Результат выполнения функции {funcName}("{msg[0]}") равен:\n{msg[1]}'
    logging.basicConfig(filename='log_result.log1', filemode='w',  # .gitignore игнорит .log, поэтому .log1
                        encoding='UTF-8', format=FORMAT, style='{', level=logging.DEBUG)
    logger = logging.getLogger(__name__)
    logger.debug([path, result])


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="os.walk but different")
    parser.add_argument('path', metavar='P', type=str, help="Path to a directory", default=".")
    args = parser.parse_args()
    if os.path.isdir(args.path):
        save_result(args.path)
    else:
        print("Не является папкой")
