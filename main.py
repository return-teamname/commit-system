import msvcrt
import sys
import os
from classes.commit import *
from functions.commit_from_file import readCommitFromDetails
from functions.initrepo import *
from functions.change_current_commit import *
from functions.make_new_commit import createCommit



def main():
    #createRepo = initRepo("testing/")
    #print("[Init] repo status:", "success" if createRepo else "failed")
    
    #lastcommit = readCommitFromDetails("testing/", 1)
    creation = createCommit("testing/", current_commit_version("testing/") + 1)
    #current_commit = current_commit_version("testing/")
    #change_current_commit_version("testing_3/", 2)

    name = "Anyad" #input("Adja meg a nevét ")
    # os.system("cls")
    # while True:
    #     print("Kérjük válasszon az alábbi menűpontok közül")
    #     print("1. Commit létrehozása")
    #     print("2. Az aktív commit megváltoztatása")
    #     print("3. Verziók listázása")
    #     print("ESC: Kilépés")

    #     inp = msvcrt.getch()

    #     if inp == chr(27).encode():
    #         sys.exit()
    #     if inp == "1".encode():
    #         print("menu 1")
    #     if inp == "2".encode():
    #         print("menu 2")
    #     if inp == "3".encode():
    #         print("menu 3")

    #     os.system("cls")

if __name__ == "__main__":
    main()