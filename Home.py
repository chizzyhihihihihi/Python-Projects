from pathlib import Path
import subprocess
import os
import time

basedir = Path(__file__).resolve().parent
projects_dir = basedir / "projects"

projects = {
    "1": "passgenerator.py",
    "2": "qrgenerator.py",
}
def main():
    print("============================================================================================================================================================================================")
    print(r""" 
    __________          __  .__                             .____                               .__                  
    \______   \___.__._/  |_|  |__   ____   ____            |    |   _____   __ __  ____   ____ |  |__   ___________ 
     |     ___<   |  |\   __\  |  \ /  _ \ /    \           |    |   \__  \ |  |  \/    \_/ ___\|  |  \_/ __ \_  __ \
     |    |    \___  | |  | |   Y  (  <_> )   |  \          |    |___ / __ \|  |  /   |  \  \___|   Y  \  ___/|  | \/
     |____|    / ____| |__| |___|  /\____/|___|  /          |_______ (____  /____/|___|  /\___  >___|  /\___  >__|   
               \/                \/            \/                   \/    \/           \/     \/     \/     \/       
    """)
    print("============================================================================================================================================================================================")
main()

def choice_and_run(projects):
    print("Welcome to the Py Launcher Choose a program to run")
    print("1. Password Generator")
    print("2. QR Code Generator")

    choice = input("Enter your choice: ")
    
    if choice in projects:
        os.system('cls' if os.name == 'nt' else 'clear')
        project_path = projects_dir / projects[choice]
        subprocess.run(["python3", str(project_path)])
    else:
        print("Invalid choice. Please select a valid option.")
        time.sleep(1)
        os.system('cls' if os.name == 'nt' else 'clear')
        main()
        choice_and_run(projects)

def run():
    choice_and_run(projects)

run()