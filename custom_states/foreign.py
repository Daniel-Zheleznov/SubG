import pygame

FOREIGN_SUB_TYPE      = 0
FOREIGN_OUTPOST_TYPE  = 2

class Foreign:
    def __init__(self, x, y, type_):
        self.x = x
        self.y = y
        self.type = type_

        self.width = self.height = 5

        self.outpost_img = pygame.image.load("custom_states\\assets\\outpost.png")

    def render(self, canvas: pygame.Surface):
        canvas.blit(self.outpost_img, (self.x, self.y))

    def update(self, dt):
        pass