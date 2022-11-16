from classes.commit import *
from functions.initrepo import *

szerzo = "Anyad"

def main():
    createRepo = initRepo("testing/")
    
    print("[Init] repo status:", "success" if createRepo else "failed")
            
main()