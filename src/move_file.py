import os

HOME = os.environ.get("HOME")


def move(file, folder):
    new_file_name = file
    i = 1
    while os.path.exists(f"{HOME}/{folder}/{new_file_name}"):
        new_file_name = f"{file}[{i}]"
        i += 1
    os.rename(f"{HOME}/Downloads/{file}", f"{HOME}/{folder}/{new_file_name}")
