from datetime import datetime
import os
import shutil
from typing import List

from classes.commit import *

def initRepo(folder: str, writer = "Béla") -> bool:
    files = os.listdir(folder)
    
    if ".dusza" in files:
        print("[Init] Error: .dusza already exists")
        return False
    
    os.mkdir(folder + ".dusza")
    os.mkdir(folder + ".dusza/1.commit")
    
    with open(folder + ".dusza/head.txt", "w") as f:
        f.write("1")
    
    changes: List[CommitChange] = []
        
    for file in files:
        with open(folder + file, "rb") as f:
            data = f.read()
            with open(folder + ".dusza/1.commit/" + file, "wb") as nfile:
                nfile.write(data)
                
        changes.append(CommitChange(CommitChangeType.NEW, file, datetime.fromtimestamp(os.path.getmtime(folder + file))))
    
    commit = CommitParameters(folder)
    commit.createNew("-", writer, "A projekt elso valtozata, mely tartalmazza az alapveto funkciokat.", changes)
    commit.exportCommit()

    ## for faster testing
    # shutil.rmtree(folder + ".dusza", ignore_errors=True)
                
    return True

def createCommitDetails():
    pass