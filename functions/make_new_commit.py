from datetime import datetime
import os
import shutil
from typing import List

from distutils.dir_util import copy_tree

from classes.commit import *
from functions.change_current_commit import current_commit_version
from functions.commit_from_file import readCommitFromDetails

def createCommit(folder: str, commit_id: int, writer = "Béla", desc = "A commit leirasa") -> bool:
    files = [os.path.join(dirpath,filename) for dirpath, _, filenames in os.walk(folder) for filename in filenames]
    alread_repo = ".dusza" in os.listdir(folder)
    
    if not alread_repo:
        print("[Init] Error: the chosen directory was not a repo (.dusza not exists)")
        return False
    
    current_changes: List[CommitChange] = []
    
    ccv = current_commit_version(folder)
    latest_files = [os.path.join(dirpath.split("/", 3)[3], filename) for dirpath, _, filenames in os.walk(folder + f".dusza/{ccv}.commit/") for filename in filenames]
    
    # check if file was deleted
    for file in latest_files:
        if file == "commit.details":
            continue
        
        print("checking file", file)
        
        if not os.path.exists(folder + file):
            latest_date = datetime.fromtimestamp(os.path.getmtime(folder + f".dusza/{ccv}.commit/{file}"))
            current_changes.append(CommitChange(CommitChangeType.DELETED, file, latest_date))
    
    # check if file was new or modified
    for file in files:
        wopath = file.split("/", 1)[1]
        if wopath.startswith(".dusza"):
            continue
        
        date_modified = datetime.fromtimestamp(os.path.getmtime(file))
        changetype = None
        
        # modified
        if wopath in latest_files:
            latest_date_modified = datetime.fromtimestamp(os.path.getmtime(folder + f".dusza/{ccv}.commit/{wopath}"))
            
            if date_modified != latest_date_modified:
                print("modified", file, date_modified)
                changetype = CommitChangeType.MODIFIED
        # new
        else:
            changetype = CommitChangeType.NEW
        
        if changetype:
            print("adding to changes")
            current_changes.append(CommitChange(changetype, wopath, datetime.fromtimestamp(os.path.getmtime(file))))
    
    commit = CommitParameters(folder)
    commit.newCommit(commit_id, writer, desc, current_changes)
    
    if len(current_changes) == 0:
        print("[Error] Nothing changed since last commit")
        return
    
    shutil.copytree(folder, folder + f".dusza/{commit_id}.commit", ignore=shutil.ignore_patterns(".dusza"), dirs_exist_ok=True)
    
    with open(folder+ ".dusza/head.txt", "w") as f:
        f.write(str(commit_id))
    
    commit.exportCommitDetails()

    # for faster testing
    #shutil.rmtree(folder + ".dusza", ignore_errors=True)
                
    return True