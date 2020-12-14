"""

Program: gametracking.py

Author: Peggy Walsh
        CIS 1415

Description: Tracking scoring. 

"""
import sys
import pygame
import pygame.font

class GameTracking(object):
    #initialize game tracking
    def __init__(self, cc_game):
        self.settings = cc_game.settings

        self.gamePlay = False

        #scoreboard
        self.screen = cc_game.screen
        self.screen_rect = self.screen.get_rect()

        #font settings
        self.textColor = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 50)

        self.scoreBoard()

        #high score
        self.highScore = 0
        self.hScore()

    def hScore(self):
        pass         
        
    #display scoreboard
    def scoreBoard(self):
        scoreString = str("0")
        self.scoreImage = self.font.render(scoreString, True,
                                           self.textColor)
        #score position
        self.score_rect = self.scoreImage.get_rect()
        self.score_rect.left = self.screen_rect.left + 10
        self.score_rect.top = 10
        
    #draw to screen
    def displayScore(self):
        self.screen.blit(self.scoreImage, self.score_rect)
        
        
        
        

   
        
    
