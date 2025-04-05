import pygame

pygame.init()

class Game:
    def __init__(self):
        self.__window =  pygame.display.set_mode((1280, 720))
        self.__timer = pygame.time.Clock()

        pygame.display.set_caption("An Evergreen window")

        self.__states = []
        self.__current_state = 0

        self.actions = {
            "UP": False,
            "DOWN": False,
            "LEFT": False,
            "RIGHT": False,
            "INTERACT": False
        }

        self.data = {}

    def run(self, fps: int = 60):
        running = True

        while running:
            self.__window.fill("midnightblue")

            self.__timer.tick(fps)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        running = False

                    if event.key == pygame.K_w:
                        self.actions["UP"] = True
                    
                    if event.key == pygame.K_s:
                        self.actions["DOWN"] = True

                    if event.key == pygame.K_a:
                        self.actions["LEFT"] = True

                    if event.key == pygame.K_d:
                        self.actions["RIGHT"] = True

                    if event.key == pygame.K_e:
                        self.actions["INTERACT"] = True

                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_w:
                        self.actions["UP"] = False
                    
                    if event.key == pygame.K_s:
                        self.actions["DOWN"] = False

                    if event.key == pygame.K_a:
                        self.actions["LEFT"] = False

                    if event.key == pygame.K_d:
                        self.actions["RIGHT"] = False
                    
                    if event.key == pygame.K_e:
                        self.actions["INTERACT"] = True

        pygame.quit()


class State:
    def __init__(self, game: Game, canvas_size: list[int]):
        self.game = game

    def add_state(self):
        self.game.__states.append(self)

    def remove_state(self):
        self.game.__states.pop()

    def update(self, deltatime: int):
        pass

    def draw(self, canvas: pygame.Surface):
        pass