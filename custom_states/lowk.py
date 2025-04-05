from evergreen import *
from json import loads

class lowk(State):
	def __init__(self, game: Game, canvas_size: list[int], player):
		super().__init__(game, canvas_size)
		self.player = player

		self.data = []
		with open('evergreen/custom_states/lowk.json', 'r') as map_file:
			self.data = loads(map_file.readlines())
			map_file.close()


	def update(self, deltatime: int):
		pass

	def draw(self, canvas: pygame.Surface):
		pass
