import os
import time
from . import save_data

def check_valid(string):
    i = 0
    while i < len(string):
        if not string[i].isalnum():
            return False
        i += 1

    return True    

def cmd_help():
    print("e <tile-descriptor> <new-tile-info> - Edit a tile")
    print("s - Save state to file.")
    print("q - Quit the editor without saving.")
    print("\nA <tile-descriptor> is in this fashion xxx,yy")
    print("A <new-tile-info> is ")
    print("                      o - Oil")
    print("                      f - Foreign")
    print("                      x - Flares")
    print("                      e - Enemy spawn point")
    print("                      p - Player spawn point")
    print("                      n - Nothing/Base")

def shell(state_name:str, state_map = None):
    running = True

    if state_map is None:
        state_map = ['n' for i in range(160*90)]

    os.system('cls' if os.name == 'nt' else 'clear')
    print(f"Evergreen level editor shell\n\n{state_name}")
    while running:
        cmd = input("> ").strip()
        cmdline = cmd.strip().split(" ")

        if cmd.lower() == "help":
            cmd_help()

        if cmd.lower().startswith('e'):
            cmdline[1] = cmdline[1].split(",")
            if len(cmdline[1]) <= 1:
                print("Retry. Invalid cmd parameters.")
                continue

            if 0 > int(cmdline[1][0]) or int(cmdline[1][0]) > 159:
                print("Retry. Invalid cmd parameters.")
                continue

            if 0 > int(cmdline[1][1]) or int(cmdline[1][1]) > 89:
                print("Retry. Invalid cmd parameters.")
                continue

            if cmdline[2].lower() not in ["o", "f", "x", "e", "p", "n"]:
                print("Retry. Invalid cmd parameters.")
                continue

            # doing it
            state_map[(int(cmdline[1][1])*160) + int(cmdline[1][0])] = cmdline[2].lower()

        if cmd.lower() == 's':
            save_data.save(state_name, state_map)

        if cmd.lower() == 'd':
            x, y = 0, 0

            while y < 90:
                x = 0
                while x < 90:
                    print(state_map[(y*90) + x], end='')
                    x += 1
                
                print("\n")
                y += 1

        if cmd.lower() == "clear" or cmd.lower() == "cls" or cmd.lower() == "clr":
            os.system('cls' if os.name == 'nt' else 'clear')            

        if cmd.lower() == 'q':
            print("Goodbye my friend.")
            running = False

def create_new():
    os.system('cls' if os.name == 'nt' else 'clear')

    state_name = input("State name: ")

    if check_valid(state_name) == False:
        print("Retry. Invalid state name")
        time.sleep(1)
        create_new()

    if state_name.strip() == "":
        print("Retry. Invalid state name")
        time.sleep(1)
        create_new()

    shell(state_name)
    