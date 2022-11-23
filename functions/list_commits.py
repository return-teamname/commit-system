import os

def get_all_commits(path):
    folders = [x[0] for x in os.walk(path)]
    commits = [x.replace(path, "").replace(".commit", "") for x in folders][1:]
    commits = sorted(commits, key=lambda x: int(x))

    return commits

def list_commits_into_terminal(path):
    commits = get_all_commits(path)
    print("Commitok: ")
    for commit in commits:
        print(commit)
    
    selected_commit = input("Select a commit id: ")
    if selected_commit in commits:
        with open(path + selected_commit + ".commit/commit.details", encoding="utf-8") as file:
            contents = file.read()
            print(contents)
    else:
        print("[Error] No commit exists with that id")

