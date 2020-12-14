"""

Program: movemoons.py

Author: Peggy Walsh
        CIS 1415

Description: Moon class that has random movement. 

"""
import sys, pygame
from random import *

class Obstacle(pygame.sprite.Sprite):
    def __init__(self, imageFile, location, speed):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(imageFile)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location
        self.speed = speed 

    #method for moving the moon
    def move(self):
        self.rect = self.rect.move(self.speed)
        if self.rect.left < 0 or self.rect.right > width:
            self.speed[0] = -self.speed[1]

        if self.rect.top < 0 or self.rect.bottom > height:
            self.speed[1] = -self.speed[1]

#Main window and screen
size = width, height = 800, 600
screen = pygame.display.set_mode(size)
screen.fill([0, 0, 0])

imgFile = "moon.png"
moons = []#tracking list of moons

for row in range (0, 4):
    for column in range (0, 4):
        location = [column + 150 + 10, row * 150 + 10]
        speed = [choice([-1, 1]), choice([-1, 1])]#random generated speeds
        moon = Obstacle(imgFile, location, speed)
        moons.append(moon)
        
#redraw the screen 
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
    pygame.time.delay(20)
    screen.fill([0, 0, 0])
    for moon in moons:
        moon.move()
        screen.blit(moon.image, moon.rect)
    pygame.display.flip()
