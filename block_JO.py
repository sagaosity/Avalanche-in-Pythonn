import pygame
class block():
    def __init__(self, colour, gridXPos, gridYPos): # Constructor of the block objects
        self.colour = colour
        self.gridXPos = int(gridXPos)
        self.gridYPos = int(gridYPos)
        self.blockSize = 25

    def draw(self, screen): # Draws the block objects on the screen
         pygame.draw.rect(screen, self.colour, [self.gridXPos * self.blockSize+1, self.gridYPos * self.blockSize+1, self.blockSize-2, self.blockSize-2], 0)



