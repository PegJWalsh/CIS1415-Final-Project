"""

Program: alien.py

Author: Peggy Walsh
        CIS 1415

Description: The alien player properties and attributes. 

"""
import pygame

class Alien(object):
    """Class to manage alien player."""

    def __init__(self, cc_game):
        """Initialize alien player and set its staring point."""
        self.screen = cc_game.screen
        self.screen_rect = cc_game.screen.get_rect()

        """Load the alien player and get its rectangle."""
        self.image = pygame.image.load("aliens.png")
        self.rect = self.image.get_rect()
        #initial position of alien
        self.rect.midbottom = self.screen_rect.midbottom

        #movement flag
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False 

    def update(self):
        #update alien position based upon movement flag
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.rect.x += 1
        if self.moving_left and self.rect.left > 0:
            self.rect.x -= 1
        if self.moving_up and self.rect.y > 0:
            self.rect.y -= 1
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:  
            self.rect.y += 1

    def drawAlien(self):
        """Draw the alien player at starting point."""
        self.screen.blit(self.image, self.rect)
