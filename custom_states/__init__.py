from evergreen import *
from json import loads

class fantasia(State):
	def __init__(self, game: Game, player):
		super().__init__(game)
		self.player = player

		self.data = []
		with open('custom_states/fantasia.json', 'r') as map_file:
			self.data = loads(''.join(map_file.readlines()))
			map_file.close()

		self.tiles = [pygame.Surface((1, 1)) for i in range(160*90)]

	def update(self, deltatime: int):
		pass

	def draw(self, canvas: pygame.Surface):
		x, y = 0, 0
		tile_count: int = 0
		while tile_count < len(self.tiles):
			color = (0, 0, 0)
			match self.tiles[tile_count]:
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

			print(color)

			self.tiles[tile_count].fill(color)
			canvas.blit(self.tiles[tile_count], (x, y))

			x += 1
			if tile_count%160 == 0 and tile_count != 0:
				y += 1
				x = 0

			tile_count += 1
