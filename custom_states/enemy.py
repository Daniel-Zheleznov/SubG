import pygame
from evergreen import  *

ENEMY_BLUE = (0, 0, 255)
ENEMY_RED = (255, 0, 0)

class Enemy:
    ##inital paramtiztaion for emeny
    def __init__(self, inital_x, inital_y, health, speed, drops):
        self.health       = health
        self.speed        = speed
        self.drops        = drops
        self.damage       = 1

        self.width        = 4
        self.height       = 4

        self.x            = inital_x
        self.y            = inital_y
        
        self.state_color  = ENEMY_RED
        self.alive        = True
    
    ##enemy takes damage
    def take_damage(self, damage):
        self.health -= damage
    
    ##enemy deals damage
    def attacks(self, target):
        target.take_damage(self.damage)
    
    ##starting on drops for enemy but couldnt make much progress without player info
    def createDrop(self, alive):
        if self.health<=0:
            self.alive = False
            self.state_color = ENEMY_BLUE
    ##boundaries for enemy
    
    ##draw enemy and give him boundaries
    def draw(self, canvas):
        if self.alive==True:
            self.enemyMoving() # TODO {Jonathan W.}: Timer on the movement of the enemy 

            pygame.draw.rect(canvas, self.state_color, (self.x, self.y, self.width, self.height))
    
        
    def enemyMoving(self):
        if self.x < 0:
           self.x = 0
        
        if self.x > 160 - self.width:
           self.x = 160 - self.width
        
        if self.y < 0:
            self.y = 0
        
        if self.y > 90 - self.height:
            self.y = 90 - self.height


    