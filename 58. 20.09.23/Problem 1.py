import os
import json
import csv
import pickle


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


def save_result(path: str = os.getcwd()) -> None:
    result = recurse_walk(path)
    with (
            open(os.path.join(path, 'json_result.json'), 'w', encoding='UTF-8') as json_file,
            open(os.path.join(path, 'csv_result.csv'), 'w', encoding='UTF-8', newline='') as csv_file,
            open(os.path.join(path, 'pickle_result.pickle'), 'bw') as pickle_file):
        json.dump(result, json_file, indent=2)
        csv_write = csv.DictWriter(csv_file, fieldnames=result[0].keys(), dialect='excel', quoting=csv.QUOTE_NONNUMERIC)
        csv_write.writeheader()
        for i in range(len(result)):
            csv_write.writerow(result[i])
        pickle.dump(result, pickle_file)


save_result(os.path.join("..", "57. 16.09.23"))