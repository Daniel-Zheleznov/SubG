from evergreen import *
from json import loads
from . import enemy
import random

def generate_enemies(count: int, spawn_data: list[list[str, str]]):
	enemies = []

	for i in range(count):
		index = random.randint(0, len(spawn_data)-1)
		spawn = spawn_data[index]
		enemies.append(enemy.Enemy(spawn[0], spawn[1], 100, 3, None))

	return enemies
