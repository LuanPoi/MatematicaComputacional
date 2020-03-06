import os
import sys
import time
from os.path import *

clear = lambda: os.system('cls')
path = "Objects"

def menu():
    folderChoice = None
    fileChoice = None
    while True:
        clear()
        banner()
        folders = getFolders(path)
        print("Choose an option:")
        for counter in range(len(folders)):
            print(str(counter) + " - " + folders[counter])
        print("Q - quit")
        folderChoice = input("Option: ").lower()
        if folderChoice == "q" or folderChoice == "quit":
            clear()
            sys.exit(0)
        if(folderChoice.isnumeric()):
            folderChoice = int(folderChoice)
            if(folderChoice >= 0 and folderChoice < len(folders)):
                while True:
                    clear()
                    currentPath = join(path, folders[folderChoice])
                    files = getFiles(currentPath)
                    banner()
                    print("Choose a script")
                    for counter in range(len(files)):
                        print(str(counter) + " - " + splitext(files[counter])[0])
                    print("B - back to previous page")
                    print("Q - quit")
                    fileChoice = input("Option: ").lower()
                    if fileChoice == "q" or fileChoice == "quit":
                        clear()
                        sys.exit(0)
                    if fileChoice == "b":                        
                        break
                    elif(fileChoice.isnumeric()):
                        fileChoice = int(fileChoice)
                        if(fileChoice >= 0 and fileChoice < len(folders)):
                            runScript(join(currentPath, files[fileChoice]))
                            continue
                    print("Erro: Entrada inválida.")
                    input()

def getFolders(path):
    folders = []
    for item in os.listdir(path):
        if(isdir(join(path, item))):
            folders.append(item)
    return folders

def getFiles(path):
    files = []
    for item in os.listdir(path):
        if(isfile(join(path, item))):
            files.append(item)
    return files

def runScript(path):
    clear()
    data = os.system("python " + path)
    input()
    return data


def banner():
    print(" ___  ___      _                       _   _                            ")
    print(" |  \/  |     | |                     | | (_)                           ")
    print(" | .  . | __ _| |_ ___ _ __ ___   __ _| |_ _  ___ __ _                  ")
    print(" | |\/| |/ _` | __/ _ \ '_ ` _ \ / _` | __| |/ __/ _` |                 ")
    print(" | |  | | (_| | ||  __/ | | | | | (_| | |_| | (_| (_| |                 ")
    print(" \_|  |_/\__,_|\__\___|_| |_| |_|\__,_|\__|_|\___\__,_|                 ")
    print("  _____                             _             _                   _ ")
    print(" /  __ \                           | |           (_)                 | |")
    print(" | /  \/ ___  _ __ ___  _ __  _   _| |_ __ _  ___ _  ___  _ __   __ _| |")
    print(" | |    / _ \| '_ ` _ \| '_ \| | | | __/ _` |/ __| |/ _ \| '_ \ / _` | |")
    print(" | \__/\ (_) | | | | | | |_) | |_| | || (_| | (__| | (_) | | | | (_| | |")
    print("  \____/\___/|_| |_| |_| .__/ \__,_|\__\__,_|\___|_|\___/|_| |_|\__,_|_|")
    print("                       | |                                              ")
    print("                       |_|                                              ")
    print("")
    

if __name__ == "__main__":
    for seconds in range(2):
        clear()
        banner()
        print(" | ")
        time.sleep(.125)
        clear()
        banner()
        print(" / ")
        time.sleep(.125)
        clear()
        banner()
        print(" - ")
        time.sleep(.125)
        clear()
        banner()
        print(" \ ")
        time.sleep(.125)
        clear()
        banner()
        print(" | ")
        time.sleep(.125)
        clear()
        banner()
        print(" / ")
        time.sleep(.125)
        clear()
        banner()
        print(" - ")
        time.sleep(.125)
        clear()
        banner()
        print(" \ ")
        time.sleep(.125)
    
    menu()