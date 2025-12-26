import os
import time
import sys
import shutil
from click import command 

GREEN = "\033[92m"
RESET = "\033[0m"
SOFT = "\033[2;37m"

import os
#MAKE FOLDER
def make_folder(command):
    path = command[4:].strip()

    if len(path) == 0:
        print(f"{SOFT}Please provide a folder name{RESET}")
        return

    try:
        os.mkdir(path)
        #print(f"✅ Folder '{path}' created")

    except FileExistsError:
        print(f"{SOFT}Folder '{path}' already exists{RESET}")
        
        
#BACK FOLDER
def back_folder():
    os.chdir("..")

#OPEN FOLDER
def open_folder(command):
    path = command[5:].strip()
    name = os.getcwd();
    name = name + path
    try:
        os.chdir(path)
        # print(f"📂 Entered: {os.getcwd()}")
    except FileNotFoundError:
        print(f"{SOFT}Folder not found{RESET}")
    except NotADirectoryError:
        print(f"{SOFT}Not a folder{RESET}")
        
#DELETE FOLDER
def delete_folder(command):
    path = command[6:].strip()
    try:
        if os.path.isdir(path):
            shutil.rmtree(path)   
            # print(f"🗑️ Folder '{path}' deleted")
        else:
            print(f"{SOFT}Folder does not exist{RESET}")
    except Exception as e:
        print(f"{SOFT}Error: {RESET}", e)

#OPEN FILE
def open_file(command):
    name = command[6:].strip()

    if not name:
        print(f"{SOFT}Please provide a file name{RESET}")
        return

    if not os.path.exists(name):
        print(f"{SOFT}File not found{RESET}")
        return

    os.startfile(name)
    
#MAKE FILE
def make_file(command):
    name = command[5:].strip()

    if not name:
        print(f"{SOFT}Please provide a file name{RESET}")
        return

    try:
        with open(name, "x"):
            print(f"{SOFT}File '{name}' created{RESET}")

    except FileExistsError:
        print(f"{SOFT}File already exists{RESET}")

    except FileNotFoundError:
        print(f"{SOFT}Invalid file name{RESET}")

#DELETE FILE
def delete_file(name):
    name = name[6:].strip()
    try:
        os.remove(name)
        print(f"{SOFT}File '{name}' deleted{RESET}")
    except FileNotFoundError:
        print(f"{SOFT} File not found {RESET}")

#DELETE FOLDER IF FOLDER IS NOT EMPTY 
def del_nt_mt_fol(command):
    path = command[6:].strip()
    vote = input(f"{SOFT}Want to Delete Folder?{RESET}").strip().lower()
    vote = input(f"{SOFT}Want to Really Folder?{RESET}").strip().lower()
    if vote in ("y", "yes"):
        shutil.rmtree(path)
        print(f"{SOFT}Folder '{path}' deleted{RESET}")
 
#ANIMATION
def slide_in(text, delay=0.05, color=""):
    for i in range(len(text) + 1):
        sys.stdout.write("\r" + color + text[:i] + RESET)
        sys.stdout.flush()
        time.sleep(delay)
    print() 
