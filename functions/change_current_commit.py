import os
import shutil


def current_commit_version(folder) -> int:
    path = f"{folder}/.dusza/head.txt"
    if not os.path.exists(path):
        print("[Error] The chosen folder is not initialized.")
        return
    with open(path, 'r', encoding="utf-8") as f:
        return int(f.readlines()[0].strip())


def change_current_commit_version(folder, new_version):
    current_version = current_commit_version(folder)
    path = f"{folder}/.dusza/{new_version}.commit"
    if current_version == new_version:
        print("The chosen version mustn't be equal with the new version.")
        return
    if not os.path.exists(path):
        print("The chosen version is not valid.")
        return

    for i in os.listdir(folder):
        if i == ".dusza":
            continue
        pp = f"{folder}/{i}"
        if os.path.isdir(pp):
            shutil.rmtree(pp)
        else:
            os.remove(pp)

    shutil.copytree(path, folder, ignore=shutil.ignore_patterns("commit.details"), dirs_exist_ok=True)

    with open(folder+ ".dusza/head.txt", "w") as f:
        f.write(str(new_version))

    return