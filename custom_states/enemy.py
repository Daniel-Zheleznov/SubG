import pygame
from evergreen import  *

ENEMY_STATE_ACTIVE = 0
ENEMY_STATE_DEAD   = 1

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
        
        self.state        = ENEMY_STATE_ACTIVE
        self.alive        = True

        self.enemy_img    = pygame.image.load("custom_states\\assets\\enemy.png")
    
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
            self.state = ENEMY_STATE_DEAD
    ##boundaries for enemy
    
    ##draw enemy and give him boundaries
    def draw(self, canvas: pygame.Surface):
        if self.alive==True:
            self.enemyMoving() # TODO {Jonathan W.}: Timer on the movement of the enemy 

            if self.state == ENEMY_STATE_ACTIVE:
                canvas.blit(self.enemy_img, (self.x, self.y))
            # pygame.draw.rect(canvas, self.state_color, (self.x, self.y, self.width, self.height))
    
        
    def enemyMoving(self):
        if self.x < 0:
           self.x = 0
        
        if self.x > 160 - self.width:
           self.x = 160 - self.width
        
        if self.y < 0:
            self.y = 0
        
        if self.y > 90 - self.height:
            self.y = 90 - self.height


    