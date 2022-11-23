from datetime import datetime
import os
import shutil
from typing import List

from distutils.dir_util import copy_tree

from classes.commit import *

def initRepo(folder: str, writer = "Béla") -> bool:
    files = [os.path.join(dirpath,filename) for dirpath, _, filenames in os.walk(folder) for filename in filenames]
    alread_repo = ".dusza" in os.listdir(folder)
    
    if alread_repo:
        print("[Init] Error: .dusza already exists")
        return False

    shutil.copytree(folder, folder + ".dusza/1.commit", dirs_exist_ok=True)
    
    with open(folder+ ".dusza/head.txt", "w") as f:
        f.write("1")
    
    changes: List[CommitChange] = []
        
    for file in files:
        wopath = file.split("/", 1)[1]
        changes.append(CommitChange(CommitChangeType.NEW, wopath, datetime.fromtimestamp(os.path.getmtime(file))))
    
    commit = CommitParameters(folder)
    commit.newCommit(0, writer, "A projekt elso valtozata, mely tartalmazza az alapveto funkciokat.", changes)
    commit.exportCommitDetails()

    # for faster testing
    #shutil.rmtree(folder + ".dusza", ignore_errors=True)
                
    return True