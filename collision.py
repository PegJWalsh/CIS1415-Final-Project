"""

Program: collision.py

Author: Peggy Walsh
        CIS 1415

Description: The main class and management of game. 

"""
import sys
import pygame
from random import randint

from settings import Settings
from gametracking import GameTracking
from button2 import Button
from alien import Alien
from obstacle import Obstacle


class CelestialCollision(object):
    """Main class to manage game"""
    
    def __init__(self):
        pygame.init()#initiate pygame
        self.settings = Settings()#call Settings class
        
        #set-up background and window
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Celestial Collision!")
        self.background = pygame.image.load("background.png")
        self.scores = GameTracking(self)

        self.alien = Alien(self)#call Alien Class
        self.obstacles = pygame.sprite.Group()                 

        self.createForce()

        self.startButton = Button(self, "Play")
        
   
    def gameLoop(self):        
        """Main loop of game """
        while True:
            self.checkEvents()
            self.alien.update()
            self.updateObstacles()
            self.updateScreen()          
        

    def checkEvents(self):
        """Checks and responds to keypresses and mouse clicks."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self.check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self.check_keyup_events(event)

            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self.checkButton(mouse_pos)

    def check_keydown_events(self, event):
        #keypress response
        if event.key == pygame.K_RIGHT:
            self.alien.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.alien.moving_left = True
        elif event.key == pygame.K_UP:
            self.alien.moving_up = True
        elif event.key == pygame.K_DOWN:
            self.alien.moving_down = True
        elif event.key == pygame.K_q:
            sys.exit()
            

    def check_keyup_events(self, event):
        #key release response
        if event.key == pygame.K_RIGHT:
            self.alien.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.alien.moving_left = False
        elif event.key == pygame.K_UP:
            self.alien.moving_up = False
        elif event.key == pygame.K_DOWN:
            self.alien.moving_down = False

    def checkButton(self, mouse_pos):#mouse click
        if self.startButton.rect.collidepoint(mouse_pos):
            self.scores.gamePlay = True
    
    def updateObstacles(self):
        self.checkBounds()
        self.obstacles.update()
        #alien and moon collisions
        if pygame.sprite.spritecollideany(self.alien, self.obstacles):
            play = False
            print("You hit a moon!")
            
        
    #creates the first row of moons
    def createForce(self):
        
        obstacle = Obstacle(self)
        obstacle_width, obstacle_height = obstacle.rect.size
        available_space_x = self.settings.screen_width - (2 * obstacle_width)
        number_obstacles_x = available_space_x // (2 * obstacle_width)

        alien_height = self.alien.rect.height
        available_space_y = (self.settings.screen_height -
                                 (3 * obstacle_height) - alien_height)
        number_rows = available_space_y // (2 * obstacle_height)

        for row_number in range(number_rows):
            for obstacle_number in range(number_obstacles_x):
                self.createObstacle(obstacle_number, row_number)
            
    #create one obstacle(moon) and settings its location
    def createObstacle(self, obstacle_number, row_number):

        obstacle = Obstacle(self)
        obstacle_width, obstacle_height = obstacle.rect.size
                
        obstacle.x = obstacle_width + 2 * obstacle_width * obstacle_number
        obstacle.rect.x = obstacle.x
        obstacle.rect.y = obstacle.rect.height + 2 * obstacle.rect.height * row_number
        self.obstacles.add(obstacle)

    #checks the boundaries of the window
    def checkBounds(self):
        for obstacle in self.obstacles.sprites():
            if obstacle.inBounds():
                self.changeDirection()
                break
            
    #pushes moons to the left when they hit the right bounds of the screen
    def changeDirection(self):
        for obstacle in self.obstacles.sprites():
            obstacle.rect.y += self.settings.dropSpeed
        self.settings.forceDirection *= -1    
    

    def updateScreen(self):
        """Update screen images and flip to new screen."""

        self.screen.blit(self.background, [0, 0])
        self.alien.drawAlien()
        self.obstacles.draw(self.screen)
        self.scores.displayScore()
        if not self.scores.gamePlay:
            self.startButton.drawButton()
        
        pygame.display.flip()    

    
#Run the game and game instance
if __name__ == "__main__":
    cc = CelestialCollision()
    cc.gameLoop()
