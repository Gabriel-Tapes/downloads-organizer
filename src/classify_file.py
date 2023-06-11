import json
from os import environ

HOME = environ.get("HOME")


def classify_file(file: str):
    file_extension = file.split(".")[-1]
    with open(
        f"{HOME}/.config/downloads-organizer/config.json", "r", encoding="utf-8"
    ) as config_file:
        config = json.load(config_file)
        for folder in config:
            if file_extension in config[folder]:
                return folder
        return "Área de trabalho"
