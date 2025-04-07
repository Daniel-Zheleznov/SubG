import pygame

pygame.init()

class Game:
    def __init__(self):
        self.__window =  pygame.display.set_mode((1280, 720))
        self.__timer = pygame.time.Clock()

        pygame.display.set_caption("An Evergreen window")

        self.states = []

        self.actions = {
            "UP": False,
            "DOWN": False,
            "LEFT": False,
            "RIGHT": False,
            "INTERACT": False
        }

        self.data = {}

    def add_state(self, state):
        self.states.append(state)

    def run(self, fps: int = 60):
        running = True

        dt = 0
        while running:
            self.__window.fill("midnightblue")

            if self.states != []:
                self.states[-1].update(dt)

                canvas = pygame.Surface((160, 90))
                self.states[-1].draw(canvas)

                canvas = pygame.transform.scale(canvas, self.__window.get_size())
                self.__window.blit(canvas, (0, 0))

            dt = self.__timer.tick(fps)
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
    def __init__(self, game: Game):
        self.game = game

    def update(self, deltatime: int):
        pass

    def draw(self, canvas: pygame.Surface):
        pass