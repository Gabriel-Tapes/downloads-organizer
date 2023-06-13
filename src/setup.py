import json
import os
from subprocess import check_output

USER_DIRS = [
    check_output(["xdg-user-dir", "DOCUMENTS"])[:-1].decode("utf-8"),
    check_output(["xdg-user-dir", "PICTURES"])[:-1].decode("utf-8"),
    check_output(["xdg-user-dir", "MUSIC"])[:-1].decode("utf-8"),
    check_output(["xdg-user-dir", "VIDEOS"])[:-1].decode("utf-8"),
]

FILE_EXTENSIONS = [
    ["pdf", "odt", "doc", "docx", "csv", "ods", "xls", "xlsx"],
    ["png", "jpeg", "jpg", "gif", "webp", "svg"],
    ["mp3", "wav", "ogg"],
    ["mp4", "avi", "wmv", "mov", "flv", "mkv", "webm"],
]


def setup():
    HOME = check_output(["xdg-user-dir"])[:-1].decode("utf-8")
    CONFIG_PATH = f"{HOME}/.config/downloads-organizer"

    default_json = dict(zip(USER_DIRS, FILE_EXTENSIONS))

    config_json = json.dumps(default_json, indent=2)

    if not os.path.exists(CONFIG_PATH):
        os.mkdir(CONFIG_PATH)

    if not os.path.isfile(f"{CONFIG_PATH}/config.json"):
        with open(f"{CONFIG_PATH}/config.json", "w", encoding="utf-8") as config_file:
            config_file.write(config_json)
