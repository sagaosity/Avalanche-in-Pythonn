import pygame
from gameboard_JO import gbWidth, gbHeight, gbActive
from ghostblocks_JO import ghostblocks
BLUE = (0, 94, 245)
TURQUOISE = (66, 239, 245)
GREEN = (87, 245, 66)
RED = (224, 38, 38)
YELLOW = (224, 227, 68)
ORANGE = (224, 144, 38)
PURPLE = (177, 68, 227)
ZSHAPE =[[(gbWidth/2)-1,0],[(gbWidth/2)-2,0],[(gbWidth/2)-1,1],[(gbWidth/2),1]]
SSHAPE = [[(gbWidth/2)-1,0], [(gbWidth/2), 0], [(gbWidth/2)-1,1], [(gbWidth/2)-2,1]]
LSHAPE = [[(gbWidth/2)-1,1], [(gbWidth/2)-1,0], [(gbWidth/2)-1,2], [(gbWidth/2), 2]]
JSHAPE = [[(gbWidth/2), 1], [(gbWidth/2), 0], [(gbWidth/2), 2], [(gbWidth/2)-1,2]]
ISHAPE = [[(gbWidth/2)-1,1], [(gbWidth/2)-1,0], [(gbWidth/2)-1,2], [(gbWidth/2)-1,3]]
TSHAPE = [[(gbWidth/2)-1,1], [(gbWidth/2)-1,0], [(gbWidth/2)-2,1], [(gbWidth/2),1]]#
SQSHAPE = [[(gbWidth/2)-1, 0], [(gbWidth/2)-1,1], [(gbWidth/2), 0], [(gbWidth/2), 1]]
ALLSHAPES = [JSHAPE, ISHAPE, SSHAPE, ZSHAPE, SQSHAPE,LSHAPE, TSHAPE]
ALLCOLOURS = [ BLUE, TURQUOISE, GREEN, RED, YELLOW, ORANGE, PURPLE]
class ghostshapes():
    def __init__(self, shapenum):
        self.numblocks = 4
        self.active = True
        self.colour = ALLCOLOURS[shapenum]
        self.shape = ALLSHAPES[shapenum]
        self.ghostblockList = []
        for i in range(self.numblocks):
            self.ghostblockList.append(ghostblocks(self.colour, self.shape[i][0], self.shape[i][1]))
        self.rockBottom = False

    def drawghostshapes(self, screen):
        for i in range(self.numblocks):
            self.ghostblockList[i].draw(screen)

    def update(self, shape):
        for i in range(self.numblocks):
            self.ghostblockList[i].gridXPos = shape.blockList[i].gridXPos
            self.ghostblockList[i].gridYPos = shape.blockList[i].gridYPos
        while self.rockBottom == False:
            for i in range(self.numblocks):
                if self.ghostblockList[i].gridYPos >= gbHeight - 1 or gbActive[self.ghostblockList[i].gridXPos][self.ghostblockList[i].gridYPos + 1] == True:
                    self.rockBottom = True
            for i in range(self.numblocks):
                if self.rockBottom == False:
                     self.ghostblockList[i].gridYPos += 1

        self.rockBottom = False
