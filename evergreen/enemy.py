import pygame
pygame.init()
class Enemy:
    ##inital paramtiztaion for emeny
    def __init__(self, health, speed, drops):
        self.attribute1 = health
        self.attribute2= speed
        self.attribute4= drops
    damage=1
    enemy_width = 10
    enemy_height = 10
    enemy_x = 100
    enemy_y = 100
    RED = (255, 0, 0)
##enemy takes damage
    def take_damage(self, damage):
        self.health -= damage
##enemy deals damage
    def attacks(self, target):
        target.take_damage(self.damage)
    
##starting on drops for enemy but couldnt make much progress without player info
    def createDrop(self):
        if self.health<=0:
            self.drops==True
    ##boundaries for enemy
    if enemy_x < 0:
        enemy_x = 0
    if enemy_x > 160 - enemy_width:
        enemy_x = 160 - enemy_width
    if enemy_y < 0:
        enemy_y = 0
    if enemy_y > 90 - enemy_height:
        enemy_y = 90 - enemy_height
    ##
    def enemyMoving(self):
        pass
    #if (enemy_x>playerx):
        #enemy_x-=self.speed
    #if (enemy_x<playerx):
        #enemy_x-=self.speed
    #if (enemy_x=playerx):
        #enemy_x-=0
     #if (enemy_y>player_y):
        #enemy_y-=self.speed
    #if (enemy_y<player_y):
        #enemy_y-=self.speed
    #if (enemy_y=playery):
        #enemy_x-=0
    
    