"""

Program: button2.py

Author: Peggy Walsh
        CIS 1415

Description: Pygame button to initiate play.  

"""
import sys
import pygame.font

class Button(object):

    def __init__(self, cc_game, msg):
        #button attributes
        self.screen = cc_game.screen
        self.screen_rect = self.screen.get_rect()

        #button properties
        self.width, self.height = 250, 75
        self.buttonColor = (0, 0, 255)
        self.textColor = (0, 0, 0)
        self.font = pygame.font.SysFont(None, 50)

        #button rectangular object and position
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center

        #message call
        self.callMsg(msg)

    def callMsg(self, msg):
        #display message
        self.msgImage = self.font.render(msg, True, self.textColor,
                                          self.buttonColor)
        
        self.msgImage_rect = self.msgImage.get_rect()

        self.msgImage_rect = self.rect.center

    def drawButton(self):
        #draw button
        self.screen.fill(self.buttonColor, self.rect)
        self.screen.blit(self.msgImage, self.msgImage_rect)
        
        




   
        
    
