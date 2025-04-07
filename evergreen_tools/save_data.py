from json import dump

def save(state_name, state_map, enemy_spawns, enemy_count):
    with open(f"custom_states/{state_name}.json", "w+") as json_file:
        print(f"Saving to custom_states/{state_name}.json")
        dump({"enemy_spawn_data": enemy_spawns, "map": state_map}, json_file)
        print(f"Saved to custom_states/{state_name}.json")

    with open(f"custom_states/__init__.py", "a+") as file:
        print(f"Saving to custom_states/__init__.py@{state_name}")

        file.write(f"\nclass {state_name}(State):\n")
        file.write("\tdef __init__(self, game: Game, player):\n")
        file.write(f"\t\tself.ENEMY_COUNT = {enemy_count}\n\n")
        file.write("\t\tsuper().__init__(game)\n\t\tself.player = player\n\n")
        file.write(f"\t\tself.data = []\n")
        file.write(f"\t\twith open('custom_states/{state_name}.json', 'r') as map_file:\n")
        file.write(f"\t\t\tself.data = loads(''.join(map_file.readlines()))\n")
        file.write(f"\t\t\tmap_file.close()\n")
        file.write(f"\t\tenemy_spawn_data = self.data['enemy_spawn_data']\n")
        file.write(f"\t\tself.enemy_data = generate_enemies(self.ENEMY_COUNT, enemy_spawn_data)\n\n")
        file.write(f"\t\tself.data = self.data['map']\n\n")
        file.write(f"\t\tself.tiles = [pygame.Surface((1, 1)) for i in range(len(self.data))]\n\n")

        file.write(f"\tdef update(self, deltatime: int):\n")
        file.write(f"\t\tpass\n\n")
        
        file.write(f"\tdef draw(self, canvas: pygame.Surface):\n")
        file.write(f"\t\tx, y = 0, 0\n")
        file.write(f"\t\ttile_count: int = 0\n")
        file.write(f"\t\twhile tile_count < len(self.tiles):\n\t\t\tcolor = (0, 0, 0)\n")
        file.write(f"\t\t\tmatch self.data[tile_count]:\n")
        file.write(f"\t\t\t\tcase 'o':\n\t\t\t\t\tcolor = (48,  42,  34)  # Oil\n")
        file.write(f"\t\t\t\tcase 'f':\n\t\t\t\t\tcolor = (26,  86,  126) # Foreign\n")
        file.write(f"\t\t\t\tcase 'x':\n\t\t\t\t\tcolor = (197, 44,  34)  # Flare\n")
        file.write(f"\t\t\t\tcase 'e':\n\t\t\t\t\tcolor = (48,  42,  34)  # Enemy spawn point\n")
        file.write(f"\t\t\t\tcase 'p':\n\t\t\t\t\tcolor = (253, 253, 253) # Player spawn point\n")
        file.write(f"\t\t\t\tcase 'n':\n\t\t\t\t\tcolor = (20,  22,  30)  # Nothing\n\n")
        file.write(f"\t\t\tself.tiles[tile_count].fill(color)\n")
        file.write(f"\t\t\tcanvas.blit(self.tiles[tile_count], (x, y))\n\n")
        file.write(f"\t\t\tx += 1\n")
        file.write(f"\t\t\tif tile_count%160 == 0 and tile_count != 0:\n")
        file.write(f"\t\t\t\ty += 1\n")
        file.write(f"\t\t\t\tx = 0\n\n")
        file.write(f"\t\t\ttile_count += 1\n")

        file.write(f"\t\tenemy_entity: enemy.Enemy\n")
        file.write(f"\t\tfor enemy_entity in self.enemy_data:")
        file.write(f"\t\t\tenemy_entity.draw(canvas)\n")

        # TODO {DANIEL ZHELEZNOV}: MAKE A WAY FOR THE PLAYER TO SEE IF THEY ARE OVER OIL/NEAR FOREIGN

        print(f"Saved to custom_states/__init__.py@{state_name}")