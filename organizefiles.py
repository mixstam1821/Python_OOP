from os.path import exists
from os import *
from shutil import move

base = {
    "Python": ["py"],
    "C-C++": ["cpp", "c"],
    "Compressed": ["zip", "rar"],
    "Videos": ["mp4", "mkv"],
    "Documents": ["pdf", "docx"]
}

path = "/home/michael/Downloads"

chdir(path)
for file in listdir(path):
    if file.startswith("."):
        continue
    name = file.split(".")[0]
    ext = file.split(".")[len(file.split(".")) - 1]
    for dir, ext_list in base.items():
        if ext in ext_list:
            if not exists(dir):
                mkdir(dir)
            old_path = path + "/" + file
            new_path = path + "/" + dir
            move(old_path, new_path)
