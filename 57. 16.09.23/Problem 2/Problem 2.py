import os
import random
import string


def random_files(extension: str, min_len: int = 6, max_len: int = 30, min_byte: int = 256, max_byte: int = 4096,
                 count: int = 42, *, file_path: str = None):
    letters = string.ascii_letters
    for _ in range(count):
        name = "".join([random.choice(letters) for _ in range(random.randint(min_len, max_len))])
        if file_path:
            if not os.path.isdir(file_path):
                os.makedirs(file_path)
            path = os.path.join(file_path, name)
        else:
            path = name
        with open(f'{path}.{extension}', 'ab') as file:
            file.write(random.randbytes(random.randint(min_byte, max_byte)))


def random_extensions(extensions: list, count: int, *, file_path: str = None):
    total_files = 0
    while total_files != count:
        random_files(random.choice(extensions), count=1, file_path=file_path)
        total_files += 1


def rename_files(dir_path: str, end_name: str, num_length: int, extension: str, end_extension: str, save_name: tuple[
                 int, int]) -> None:
    count = 0
    if os.path.isdir(dir_path):
        for file in os.listdir(dir_path):
            file_path = os.path.join(dir_path, file)
            if os.path.isfile(file_path):
                ext = file.split(".")[-1]
                if ext == extension:
                    count += 1
                    file_name = ".".join(file.split(".")[:-1])
                    name = ""
                    lower_bound = save_name[0] - 1
                    upper_bound = save_name[1]
                    if len(file_name) < upper_bound:
                        upper_bound = len(file_name)
                    elif len(file_name) < lower_bound:
                        lower_bound = upper_bound = 0
                    for i in range(lower_bound, upper_bound):
                        name += file_name[i]
                    name += f'{end_name}_{str.zfill(str(count), num_length)}.{end_extension}'
                    os.rename(file_path, os.path.join(dir_path, name))


# random_extensions(["txt", "mp4", "mp3", "png", "json"], 100, file_path="Files")

rename_files("Files", "file", 3, "mp4", "txt", (1, 1))
