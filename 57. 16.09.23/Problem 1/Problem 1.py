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


def sort_files(dir_path: str) -> None:
    if os.path.isdir(dir_path):
        text = os.path.join(dir_path, "Текст")
        video = os.path.join(dir_path, "Видео")
        audio = os.path.join(dir_path, "Аудио")
        image = os.path.join(dir_path, "Изображение")
        archive = os.path.join(dir_path, "Архив")
        for dir in [text, video, audio, image, archive]:
            if not os.path.exists(dir):
                os.makedirs(dir)
        for file in os.listdir(dir_path):
            file_path = os.path.join(dir_path, file)
            if os.path.isfile(file_path):
                extension = file.split(".")[-1]
                if extension in ["txt", "pdf", "docx"]:
                    os.rename(file_path, os.path.join(text, file))
                elif extension in ["mp4", "mov", "avi", "mkv"]:
                    os.rename(file_path, os.path.join(video, file))
                elif extension in ["mp3", "wav", "flac", "m4a"]:
                    os.rename(file_path, os.path.join(audio, file))
                elif extension in ["png", "jpeg", "jpg", "gif"]:
                    os.rename(file_path, os.path.join(image, file))
                elif extension in ["zip", "tar", "7z", "rar"]:
                    os.rename(file_path, os.path.join(archive, file))


# random_extensions(
#     ["txt", "pdf", "docx", "mp4", "mov", "avi", "mkv", "mp3", "wav", "flac", "m4a", "png", "jpeg", "jpg", "gif", "zip",
#      "tar", "7z", "rar", "py", "dll", "xlsx", "xml", "json", "csv"], 100, file_path="Files")

sort_files("Files")
