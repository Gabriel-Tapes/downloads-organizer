import json
import os


def setup():
    HOME = os.environ.get("HOME")
    CONFIG_PATH = f"{HOME}/.config/downloads-organizer"

    default_json = {
        "Documentos": ["pdf", "odt", "doc", "docx", "csv", "ods", "xls", "xlsx"],
        "Imagens": ["png", "jpeg", "jpg", "gif", "webp", "svg"],
        "Músicas": ["mp3", "wav", "ogg"],
        "Vídeos": ["mp4", "avi", "wmv", "mov", "flv", "mkv", "webm"],
    }

    config_json = json.dumps(default_json, indent=2)

    if not os.path.exists(CONFIG_PATH):
        os.mkdir(CONFIG_PATH)

    if not os.path.isfile(f"{CONFIG_PATH}/config.json"):
        with open(f"{CONFIG_PATH}/config.json", "w", encoding="utf-8") as config_file:
            config_file.write(config_json)
