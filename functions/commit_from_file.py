from datetime import datetime
import os
from typing import List

from classes.commit import CommitChange, CommitChangeType, CommitParameters

def getCommitChangeType(val) -> CommitChangeType:
    return CommitChangeType(val)

def readCommitFromDetails(folder: str, commit_id: int) -> CommitParameters:
    filepath = f"{folder}.dusza/{commit_id}.commit/commit.details"
    if not os.path.exists(filepath):
        print("[Error] File not exists while reading commit with id:", commit_id)
        return
    
    with open(filepath, "r", encoding="utf-8") as f:
        lines = [i.strip() for i in f.readlines()]
        
        datum = datetime.strptime(lines[2].split(": ", 1)[1], "%Y.%m.%d %H.%M.%S")
        
        changes: List[CommitChange] = [CommitChange(getCommitChangeType(i[0]), i[1], datetime.strptime(i[2], "%Y.%m.%d %H.%M.%S")) for i in [l.split(" ", 2) for l in lines[5:]]]
        
        parent_id = lines[0].split(": ", 1)[1]
        
        commitparam: CommitParameters = CommitParameters("folder/", datum)
        commitparam.newCommit(
            int(parent_id) if parent_id != "-" else 0,
            lines[1].split(": ", 1)[1],
            lines[3].split(": ", 1)[1],
            changes
        )
        
        return commitparam
        