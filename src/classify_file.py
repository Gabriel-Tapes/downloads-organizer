from json import load
from subprocess import check_output

HOME = check_output(["xdg-user-dir"])[:-1].decode("utf-8")


def classify_file(file: str):
    file_extension = file.split(".")[-1]
    with open(
        f"{HOME}/.config/downloads-organizer/config.json", "r", encoding="utf-8"
    ) as config_file:
        config = load(config_file)
        for folder in config:
            if file_extension in config[folder]:
                return folder
        return check_output(["xdg-user-dir", "DESKTOP"])[0:-1].decode("utf-8")
