from evergreen import *
from json import loads
from . import enemy
from . import foreign
import random

def generate_enemies(count: int, spawn_data: list[list[str, str]]):
	enemies = []

	for i in range(count):
		index = random.randint(0, len(spawn_data)-1)
		spawn = spawn_data[index]
		enemies.append(enemy.Enemy(spawn[0], spawn[1], 100, 3, None))

	return enemies

def generate_objects(count: int, spawn_data: list[list[str, str]]):
	objects = []

	for i in range(count):
		index = random.randint(0, len(spawn_data)-1)
		spawn = spawn_data[index]
		objects.append(foreign.Foreign(spawn[0], spawn[1], random.choice([foreign.FOREIGN_SUB_TYPE, foreign.FOREIGN_OIL_TYPE, foreign.FOREIGN_OUTPOST_TYPE])))

	return objects

class TestState(State):
	def __init__(self, game: Game, player):
		self.ENEMY_COUNT = 2
		self.FOREIGN_COUNT = 2

		super().__init__(game)
		self.player = player

		self.data = []
		with open('custom_states/TestState.json', 'r') as map_file:
			self.data = loads(''.join(map_file.readlines()))
			map_file.close()

		enemy_spawn_data = self.data['enemy_spawn_data']
		self.enemy_data = generate_enemies(self.ENEMY_COUNT, enemy_spawn_data)

		foreign_spawn_data = self.data['foreign_spawn_data']
		self.foreign_data = generate_objects(self.FOREIGN_COUNT, foreign_spawn_data)

		self.data = self.data['map']

		self.tiles = [pygame.Surface((1, 1)) for i in range(len(self.data))]

	def update(self, deltatime: int):
		pass

	def draw(self, canvas: pygame.Surface):
		x, y = 0, 0
		tile_count: int = 0
		while tile_count < len(self.tiles):
			color = (0, 0, 0)
			match self.data[tile_count]:
				case 'o':
					color = (48,  42,  34)  # Oil
				case 'f':
					color = (26,  86,  126) # Foreign
				case 'x':
					color = (197, 44,  34)  # Flare
				case 'e':
					color = (48,  42,  34)  # Enemy spawn point
				case 'p':
					color = (253, 253, 253) # Player spawn point
				case 'n':
					color = (20,  22,  30)  # Nothing

			self.tiles[tile_count].fill(color)
			canvas.blit(self.tiles[tile_count], (x, y))

			x += 1
			if tile_count%160 == 0 and tile_count != 0:
				y += 1
				x = 0

			tile_count += 1

		enemy_entity: enemy.Enemy
		for enemy_entity in self.enemy_data:
			enemy_entity.draw(canvas)

		foreign_entity: foreign.Foreign
		for foreign_entity in self.foreign_data:
			foreign_entity.render(canvas)

