"""

Program: final_pwalsh.py

Author: Peggy Walsh
        CIS 1415

Description: GUI input box with name prompt and game button. 

"""

from breezypythongui import EasyFrame
import pygame
#from player import Player

class EntryGame(EasyFrame):
    """Displays a greeting in a window."""

    def __init__(self):
        """Sets up the window and the label."""
        EasyFrame.__init__(self, width = 300, height = 200, title = "Celestial Collision")
        self.addLabel(text = "You have entered Celestial Collision!", row = 0,
                      column = 0, sticky = "NSEW", columnspan = 2)
        self.addLabel(text = "Enter your name:", row = 2, column = 0,
                      sticky = "NSEW", columnspan = 2)
        self.inputField = self.addTextField(text = "", row = 3, column = 0,
                      sticky = "NSEW")
        self["background"] = "blue"

        self.addButton(text = "Press to Begin", row = 4, column = 0,
                                                   command = self.begin)

    def begin(self):
        pygame.init()
        h = 600
        w = 800

        screen = pygame.display.set_mode((w,h))# create graphical window

        pygame.display.set_caption("Celestial Collision")

        play = True

        background_image = pygame.image.load("background.png")#load background image
        player_image = pygame.image.load("spaceship.png")
        moon = pygame.image.load("moon.png")
        
        while(play == True):
                for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                                play = False
                                
                                
                screen.blit(background_image, [0, 0])
                screen.blit(player_image, [350, 300])
                screen.blit(moon, [500, 200])
                pygame.display.flip()

                pygame.display.update()
    
                       
def main():
    """Instantiates and pops up the window."""
    EntryGame().mainloop()

if __name__ == "__main__":
    main()







