import pygame
class ghostblocks():
    def __init__(self, colour, gridXPos, gridYPos):
        self.colour = colour
        self.gridXPos = int(gridXPos)
        self.gridYPos = int(gridYPos)
        self.blockSize = 25

    def draw(self, screen):
            pygame.draw.rect(screen, self.colour, [self.gridXPos * self.blockSize + 1, self.gridYPos * self.blockSize + 1, self.blockSize - 2, self.blockSize - 2], 1)

