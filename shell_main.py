import os
import time
import shell_functions

count = 1
GREEN = "\033[92m"
RESET = "\033[0m"
PURPLE = '\033[95m'
BOLD = '\033[1m'
SOFT = "\033[2;37m"


os.system("cls")
while True:
  #  name = f"{PURPLE}{BOLD}charlie_is_here_{GREEN}(•‿•){RESET} "
  
    name = os.getcwd() 
    command = input( f"{PURPLE} {name} ~ {RESET}").strip()

    #EXIT 
    if command.lower() in ("end", "exit", "quit"):
        print("👋 Byee Sir..")
        break

    #OPEN FILE
    if command.startswith("openf "):
        shell_functions.open_file(command)
        continue
    
    #OPEN
    if command.startswith("open "):
        shell_functions.open_folder(command)
        continue 
    
    #SHOW
    if command.startswith("show"):
        for file in os.listdir(os.getcwd()):
            print(file)
        continue

    #MAKE
    if command.startswith("mkfl "):
        shell_functions.make_file(command)
        continue

    #MAKE
    if command.startswith("dldir"):
        shell_functions.delete_file(command)
        continue
    #MAKE
    if command.startswith("mkdr"):
        shell_functions.make_folder(command)
        continue
    #BACK
    if command.startswith("back"):
        shell_functions.back_folder()
        continue

    #DELETE
    if command.startswith("delete"):
        path = command[7:].strip()
        if os.path.isdir(path):
            if not os.listdir(path):
                shell_functions.delete_folder(command)
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
