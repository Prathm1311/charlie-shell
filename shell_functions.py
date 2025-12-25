import os
import time
import sys
import shutil

GREEN = "\033[92m"
RESET = "\033[0m"

# -------------------------
# Utility: Slide-in effect
# -------------------------
def slide_in(text, delay=0.05, color=""):
    for i in range(len(text) + 1):
        sys.stdout.write("\r" + color + text[:i] + RESET)
        sys.stdout.flush()
        time.sleep(delay)
    print()
# -------------------------
# Make folder
# -------------------------
def make(command):
    path = command[4:].strip()
    count = 1

    if not path:
        print("❌ Please provide a folder name")
        return
    try:
        os.mkdir(path)
        print(f"✅ Folder '{path}' created")
    except FileExistsError:
        while True:
            new_name = f"{path}_{count}"
            if not os.path.exists(new_name):
                os.mkdir(new_name)
                print(f"✅ Folder '{new_name}' created")
                break
            count += 1
# -------------------------
# Open / change directory
# -------------------------
def open_dir(command):
    path = command[4:].strip()
    if not path:
        print("❌ Please provide a folder name")
        return
    try:
        os.chdir(path)
    except FileNotFoundError:
        print("❌ Folder not found")
# -------------------------
# Delete empty folder
# -------------------------
def delete(command):
    path = command[6:].strip()
    try:
        os.rmdir(path)
        slide_in(f"✅ Folder '{path}' deleted", color=GREEN)
    except FileNotFoundError:
        print("❌ Folder not found")
    except OSError:
        print("⚠️ Folder is not empty")
# -------------------------
# Delete non-empty folder
# -------------------------
def delete_non_empty(command):
    path = command[6:].strip()
    if not os.path.isdir(path):
        print("❌ Folder not found")
        return
    vote = input("🤔 Want to delete this folder? (y/yes): ").strip().lower()
    if vote in ("y", "yes"):
        shutil.rmtree(path)
        slide_in(f"✅ Folder '{path}' deleted", color=GREEN)
    else:
        print("❌ Delete cancelled")
# -------------------------
# Check if folder is empty
# -------------------------
def is_folder_empty(path):
    return os.path.isdir(path) and not os.listdir(path)
