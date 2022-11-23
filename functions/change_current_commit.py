import os
import shutil


def current_commit_version(folder) -> int:
    path = f"{folder}/.dusza/head.txt"
    if not os.path.exists(path):
        return print("[Error] The chosen folder is not initialized.")
    with open(path, 'r', encoding="utf-8") as f:
        return int(f.readlines()[0].strip())


def change_current_commit_version(folder, new_version):
    current_version = current_commit_version(folder)
    path = f"{folder}/.dusza/{new_version}.commit"
    if current_version == new_version:
        return "The chosen version mustn't be equal with the new version."
    if not os.path.exists(path):
        return "The chosen version is not valid."

    for i in os.listdir(folder):
        if i == ".dusza":
            continue
        # os.remove(f"{folder}/{i}")
    for file_name in os.listdir(f"{folder}/.dusza/{new_version}.commit"):
        source = f"{folder}/.dusza/{new_version}.commit"
        destination = folder
        shutil.copytree(source, destination, ignore=shutil.ignore_patterns("commit.details"), dirs_exist_ok=True)
        print('copied', file_name)

    return
