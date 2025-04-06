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
        self.Ifnearoil=False
        self.Ifnearenemy=False
        self.Ifnearforeign=False
        self.Game = game  # store game reference
        self.angle = 270  # Facing "up" by default
        self.position = pygame.Vector2(100, 100)  # Starting positio

    def Movment(self,left,right,up,down):
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
    def playerdraw(self,surface):
        oval_color = (255, 255, 0)  # Yellow 
        oval_x = 100
        oval_y = 100
        oval_width = 25
        oval_height = 75
        
    def interaction(self):
        #random drop with either fuel or speed but significantly less value 
        if(self.Game.actions["INTERACT"]):
            True
        if (self.Ifnearenemy):   #update value
            self.fuel += 0.01
        elif (self.Ifnearoil):
        #update value
               self.speed += 0.01
        elif (self.Ifnearforeign):
        #update value
           if random.choice([True, False]):
            self.fuel += 0.1
        else:
            self.speed += 0.1
    def aim(self,surface):
     #draw line infront of player
    # Dotted line parameters
        direction = pygame.Vector2(1, 0).rotate(-self.angle)  # Rotate clockwise
        dot_spacing = 10
        dot_length = 5
        num_dots = 15
        for i in range(num_dots):
            start = self.position + direction * i * (dot_length + dot_spacing)
        end = start + direction * dot_length
        pygame.draw.line(surface, (255, 255, 255), start, end, 2)

   