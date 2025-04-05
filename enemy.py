import pygame
from evergreen import  *          
pygame.init()
class Enemy:
    ##inital paramtiztaion for emeny
    def __init__(self, health, speed, drops, game: Game):
        self.attribute1 = health
        self.attribute2= speed
        self.attribute4= drops
    damage=1
##enemy takes damage
    def take_damage(self, damage):
        self.health -= damage
##enemy deals damage
    def attacks(self, target):
        target.take_damage(self.damage)
    
##starting on drops for enemy but couldnt make much progress without player info
    def createDrop(self, alive):
        if self.health<=0:
            self.drops==True
            BLUE = (0, 0, 255)
            self.alive=False
            pygame.draw.rect(Game.__window, BLUE, self.x, self.y)
    ##boundaries for enemy
    
    ##draw enemy and give him boundaries
    def draw(self, width, height, x ,y):
        RED = (255, 0, 0)
        self.width = 10
        self.height = 10
        self.x = 100
        self.y = 100
        if self.x < 0:
           self.x = 0
        if self.x > 160 - self.width:
           self.x = 160 - self.width
        if self.y < 0:
            self.y = 0
        if self.y > 90 - self.height:
            self.y = 90 - self.height
        if self.alive==True:
            pygame.draw.rect(Game.__window, RED, self.x, self.y)
    
        
    def enemyMoving(self):
        pass
    #if (self._x>playerx):
        #enemy_x-=self.speed
    #if (self._x<playerx):
        #self._x-=self.speed
    #if (self._x=playerx):
        #self._x-=0
     #if (self._y>player_y):
        #self._y-=self.speed
    #if (self._y<player_y):
        #self._y-=self.speed
    #if (self._y=playery):
        #self._x-=0
    
    