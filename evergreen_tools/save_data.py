from json import dump

def save(state_name, state_map):
    with open(f"custom_states/{state_name}.json", "w+") as json_file:
        print(f"Saving to custom_states/{state_name}.json")
        dump({"map": state_map}, json_file)
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
        file.write(f"\t\tx, y = 0, 0\n")
        file.write(f"\t\ttile_count: int = 0\n")
        file.write(f"\t\twhile tile_count < (160*90):\n")
        file.write(f"\t\t\tpass\n")

        # TODO {DANIEL ZHELEZNOV}: MAKE A WAY FOR THE PLAYER TO SEE IF THEY ARE OVER OIL/NEAR FOREIGN

        print(f"Saved to custom_states/{state_name}.py")