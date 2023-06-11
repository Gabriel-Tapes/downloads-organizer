import os

from classify_file import classify_file
from move_file import move
from setup import setup

print("Start oganizing Downloads files")

HOME = os.environ.get("HOME")

setup()

files = [
    f
    for f in os.listdir(f"{HOME}/Downloads")
    if os.path.isfile(f"{HOME}/Downloads/{f}")
]

for file in files:
    folder = classify_file(file)
    if not os.path.exists(f"{HOME}/{folder}"):
        os.mkdir(f"{HOME}/{folder}")
    move(file, folder)

print("Done oganizing Downloads files")
