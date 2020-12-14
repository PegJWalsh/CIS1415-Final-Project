"""

Program: button.py

Author: Peggy Walsh
        CIS 1415

Description: GUI input box with name prompt and game button. 

"""

from breezypythongui import EasyFrame
import pygame
from collision import CelestialCollision


class EntryGame(EasyFrame):
    """Displays a greeting in a window."""

    def __init__(self):
        self.collision = CelestialCollision()
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
                               command = self.__init__)
                       
                                                   
       

def main():
    """Instantiates and pops up the window."""
    EntryGame().mainloop()

if __name__ == "__main__":
    main()
