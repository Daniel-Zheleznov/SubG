import pygame

FOREIGN_OUTPOST_BROKEN      = 0
FOREIGN_OUTPOST_TYPE  = 2

class Foreign:
    def __init__(self, x, y, type_):
        self.x = x
        self.y = y
        self.type = type_

        self.width = self.height = 5

        if self.type == FOREIGN_OUTPOST_TYPE:
            self.image = pygame.image.load("custom_states\\assets\\outpost.png")
        else:
            self.image = pygame.image.load("custom_states\\assets\\outpost-broken.png")

    def render(self, canvas: pygame.Surface):
        canvas.blit(self.image, (self.x, self.y))

    def update(self, dt):
        pass