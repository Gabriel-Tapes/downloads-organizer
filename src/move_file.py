import os

HOME = os.environ.get("HOME")


def move(file, folder):
    new_file_name = file
    i = 1
    while os.path.exists(f"{folder}/{new_file_name}"):
        new_file_name = f"[{i}]{file}"
        i += 1
    os.rename(f"{HOME}/Downloads/{file}", f"{folder}/{new_file_name}")
