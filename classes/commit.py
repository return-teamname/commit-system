
from datetime import datetime
from enum import Enum
import os
from typing import List
from uuid import *


class CommitChangeType(Enum):
    NEW = "uj"
    MODIFIED = "valtozott"
    DELETED = "torolt"

class CommitChange:
    def __init__(self, type: CommitChangeType, file_name: str, date=datetime.now()):
        self.type = type
        self.file_name = file_name
        self.date = date

    def exportChanges(self):
        return str(self.type.value) + " " + str(self.file_name) + " " + str(self.date) + "\n"

class CommitParameters:
    def __init__(self, folder: str):
        self.folder = folder
        self.id = uuid4()
        self.date = datetime.now()

    def createNew(self, parent: str, writer: str, desc: str, changes: List[CommitChange]):
        self.parent = parent
        self.writer = writer
        self.desc = desc
        self.changes = changes
        
    def exportCommit(self):
        with open(self.folder + ".dusza/" + ("1" if self.parent == "-" else self.parent) + ".commit/commit.details", "w", encoding="utf-8") as f:
            f.write("Szulo: " + self.parent + "\n")
            f.write("Szerzo: " + self.writer + "\n")
            f.write("Datum: " + str(self.date) + "\n")
            f.write("Commit leiras: " + self.desc + "\n")
            f.write("Valtozott:\n")
            for change in self.changes:
                f.write(change.exportChanges())

    # def parseToJson(self, raw: str):
    #     lines = raw.split("\n")

    #     parsed = {
    #         "changes": []
    #     }

    #     for index, line in enumerate(lines):
    #         if index < 4:
    #             kv = line.split(":", 1)

    #             parsed[kv[0]] = kv[1]
    #         elif index > 4:
    #             values = line.split(" ", 2)

    #             type = CommitChangeType.NEW if values[0] == "uj" else CommitChangeType.MODIFIED if values[
    #                 1] == "valtozott" else CommitChangeType.DELETED

    #             parsed["changes"].append(CommitChange(type, values[1], values[2]))
                
    #     print(parsed)

    # def readFrom(self, raw: str):
    #     self.createNew()

class Commit:
    def __init__(self, parameters: CommitParameters):
        pass
