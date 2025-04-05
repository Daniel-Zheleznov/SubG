import pygame
import random
from evergreen import *

class Player:
    def __init__(self, fuel, speed, ammo, guided, health,game: Game):
        self.fuel = fuel
        self.speed = speed
        self.ammo = ammo
        self.guided = guided
        self.health = health
    def Movment(self,left,right):
        interaction=False
        movment
        if self.tpye==pygame.QUIT:  
            interaction=False
        if self.key==pygame.K_LEFT:
            movment=Game.__current_state*self.speed*1/2 #trying to curve the moment rather than going straight left,which is why I have a -value,and value represents the x axis of this canvas 
        if self.key==pygame.K_RIGHT:
            movment=Game.__current_state*self.speed*1/2
            return movment,interaction
    def QTE(self, state: State):
        TIMER_EVENT_1 = pygame.USEREVENT + 1 # adjust after
        TIMER_EVENT_2 = pygame.USEREVENT + 2 # adjust after
        delay1 = random.randint(2000, 5000)  # adjust after
        delay2 = random.randint(2000, 5000)
        pygame.time.set_timer(TIMER_EVENT_1, delay1)
        pygame.time.set_timer(TIMER_EVENT_2, delay2)
        self.timer1_active = True
        self.timer2_active = True
        
        if self.type == pygame.KEYDOWN:
            if self.key == pygame.K_ESCAPE:
                print("Nothing bad happened")
    def playerdraw(self):
        oval_color = (255, 255, 0)  # Yellow 
        oval_x = 100
        oval_y = 100
        oval_width = 25
        oval_height = 75
    def interaction(self):

        if(self.Game.actions["Interact"]):
            print("my nits on your chin")
            