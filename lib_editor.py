import os
import time
import json

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
            state_map[(int(cmdline[1][1])*90) + int(cmdline[1][0])] = cmdline[2].lower()

        if cmd.lower() == 's':
            with open(f"custom_states/{state_name}.json", "w+") as json_file:
                print(f"Saving to custom_states/{state_name}.json")
                json.dump({"map": state_map}, json_file)
                print(f"Saved to custom_states/{state_name}.json")

            with open(f"custom_states/{state_name}.py", "w+") as file:
                print(f"Saving to custom_states/{state_name}.py")

                file.write("from evergreen import *\nfrom json import loads\n\n")
                file.write(f"class {state_name}(State):\n")
                file.write("\tdef __init__(self, game: Game, canvas_size: list[int], player):\n")
                file.write("\t\tsuper().__init__(game, canvas_size)\n\t\tself.player = player\n\n")
                file.write(f"\t\tself.data = []\n")
                file.write(f"\t\twith open('custom_states/{state_name}.json', 'r') as map_file:\n")
                file.write(f"\t\t\tself.data = loads(map_file.readlines())\n")
                file.write(f"\t\t\tmap_file.close()\n\n")
                
                file.write(f"\tdef update(self, deltatime: int):\n")
                file.write(f"\t\tpass\n\n")
                
                file.write(f"\tdef draw(self, canvas: pygame.Surface):\n")
                file.write(f"\t\tx, y: int = 0, 0\n")
                file.write(f"\t\ttile_count: int = 0\n")
                file.write(f"\t\twhile tile_count < (160*90):\n")
                file.write(f"\t\t\tpass\n")

                # TODO {DANIEL ZHELEZNOV}: MAKE A WAY FOR THE PLAYER TO SEE IF THEY ARE OVER OIL/NEAR FOREIGN

                print(f"Saved to custom_states/{state_name}.py")

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
    