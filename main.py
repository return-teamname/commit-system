import msvcrt
import sys
import os
from classes.commit import *
from functions.initrepo import *



def main():
    createRepo = initRepo("testing/")
    
    print("[Init] repo status:", "success" if createRepo else "failed")

    name = input("Adja meg a nevét ")
    os.system("cls")
    while True:
        print("Kérjük válasszon az alábbi menűpontok közül")
        print("1. Commit létrehozása")
        print("2. Az aktív commit megváltoztatása")
        print("3. Verziók listázása")
        print("ESC: Kilépés")

        inp = msvcrt.getch()

        if inp == chr(27).encode():
            sys.exit()
        if inp == "1".encode():
            print("menu 1")
        if inp == "2".encode():
            print("menu 2")
        if inp == "3".encode():
            print("menu 3")

        os.system("cls")

if __name__ == "__main__":
    main()