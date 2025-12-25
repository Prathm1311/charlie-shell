import os
import time
import shell_functions

count = 1
GREEN = "\033[92m"
RESET = "\033[0m"
PURPLE = '\033[95m'
BOLD = '\033[1m'

os.system("cls")

while True:
    name = f"{PURPLE}{BOLD}charlie_is_here_{GREEN}(•‿•){RESET} "
    command = input(name + os.getcwd() + "~ ").strip()

    #EXIT 
    if command.lower() in ("end", "exit", "quit"):
        print("👋 Byee Sir..")
        break

    #OPEN
    if command.startswith("open"):
        shell_functions.open(command)
        continue 

    #SHOW
    if command.startswith("show"):
        for file in os.listdir(os.getcwd()):
            print(file)
        continue

    #MAKE
    if command.startswith("make"):
        shell_functions.make(command)
        continue

    #DELETE
    if command.startswith("delete"):
        path = command[6:].strip()
        if os.path.isdir(path):
            if not os.listdir(path):
                shell_functions.delete(command)
            else:
                shell_functions.del_nt_mt_fol(command)
        else:
            print("❌ Folder not found")
        continue

    #SLEEP (LOCK)
    if command.startswith("sleep"):
        print("💤 Locking system...")
        time.sleep(1)
        os.system("rundll32.exe user32.dll,LockWorkStation")
        continue

    #CLEAR
    if command == "clear":
        os.system("cls")
        continue

    #DEFAULT SYSTEM COMMAND
    os.system(command)
