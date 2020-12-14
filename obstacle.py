"""

Program: obstacle.py

Author: Peggy Walsh
        CIS 1415

Description: The moon obstacle properties and attributes. 

"""
import pygame
import random
from pygame.sprite import Sprite
from settings import Settings

#creation of the moon
class Obstacle(Sprite):    

    def __init__(self, cc_game):

        super().__init__()
        self.screen = cc_game.screen
        self.settings = cc_game.settings

        self.image = pygame.image.load('moon.png')
        self.rect = self.image.get_rect()
                             
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.x = float(self.rect.x)

    def inBounds(self):
        #tracking bounds of the screen        
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right or self.rect.left <=0:
            return True
        
    #movement specifications
    def update(self):
        self.x += (self.settings.obstacleSpeed * self.settings.forceDirection)
        self.rect.x = self.x

        

        

    

