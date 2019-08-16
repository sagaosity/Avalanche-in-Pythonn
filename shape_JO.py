import pygame
import random
from block_JO import block
from gameboard_JO import gbWidth
from gameboard_JO import gbHeight
from gameboard_JO import gbActiveColours
from gameboard_JO import gbActive
from gameboard_JO import slamsound
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
class shape():
    def __init__ (self): # Constructor for the shape objects
        self.active = True
        randomnumber = random.randrange(0, 7)
        self.numblocks = 4
        self.colour = ALLCOLOURS[randomnumber]
        self.blockList = []
        self.shape = ALLSHAPES[randomnumber]
        self.shapenum = randomnumber
        for i in range(self.numblocks):
            self.blockList.append(block(self.colour, self.shape[i][0], self.shape[i][1]))

    def changeshape(self, number):
        self.numblocks = 4
        self.active = True
        self.colour = ALLCOLOURS[number]
        self.blockList = []
        self.shape = ALLSHAPES[number]
        for i in range(self.numblocks):
            self.blockList.append(block(self.colour, self.shape[i][0], self.shape[i][1]))



    def draw(self, screen): # Draws the shape objects on the screen
        for i in range(self.numblocks):
            self.blockList[i].draw(screen)

    def moveright(self):# Prevents the T*trimino from moving off the right side of the gameboard
        blocked = False
        for i in range(self.numblocks):
            if self.blockList[i].gridXPos == gbWidth - 1 or gbActive[self.blockList[i].gridXPos + 1][self.blockList[i].gridYPos]:
             blocked = True
        if blocked == False:
            for i in range(self.numblocks):
                self.blockList[i].gridXPos += 1

    def moveleft(self): # Prevents the T*trimino from moving off the left side of the gameboard
        blocked = False
        for i in range(self.numblocks):
            if self.blockList[i].gridXPos == 0 or gbActive[self.blockList[i].gridXPos-1][self.blockList[i].gridYPos] == True:
                blocked = True
        if blocked == False:
            for i in range(self.numblocks):
                self.blockList[i].gridXPos -= 1

    def movedown(self): # Prevents the T*trimino from moving off the bottom of the gameboard
        blocked = False
        for i in range(self.numblocks):
            if self.blockList[i].gridYPos == gbHeight - 1 or gbActive[self.blockList[i].gridXPos][self.blockList[i].gridYPos + 1] == True:
                blocked = True
        if blocked == False:
            for i in range(self.numblocks):

                self.blockList[i].gridYPos += 1

    def rotationCW(self): # Rotates the blocks clockwise based on the position of their centre blocks
        newblockX = [ 0, 0, 0, 0]
        newblockY = [0,0,0,0]
        blocked = False
        if self.shape != SQSHAPE:
            for i in range(self.numblocks):
                 newblockX[i] = -(self.blockList[i].gridYPos - self.blockList[0].gridYPos) + self.blockList[0].gridXPos
                 newblockY[i] = (self.blockList[i].gridXPos - self.blockList[0].gridXPos) + self.blockList[0].gridYPos
                 if newblockY[i] > gbHeight - 1 or newblockX[i] > gbWidth - 1 or newblockX[i] < 0 or gbActive[newblockX[i]][newblockY[i]] == True:
                     blocked = True
            if blocked == False:
                for i in range(self.numblocks):
                    self.blockList[i].gridXPos = newblockX[i]
                    self.blockList[i].gridYPos = newblockY[i]

    def rotationCCW(self): # Rotates the blocks counter-clockwise based on the position of their centre blocks
        newblockX = [0, 0, 0, 0]
        newblockY = [0, 0, 0, 0]
        blocked = False
        if self.shape != SQSHAPE:
            for i in range(self.numblocks):
                newblockX[i] = (self.blockList[i].gridYPos - self.blockList[0].gridYPos) + self.blockList[0].gridXPos
                newblockY[i] = -(self.blockList[i].gridXPos - self.blockList[0].gridXPos) + self.blockList[0].gridYPos
                if newblockY[i] > gbHeight - 1 or newblockX[i] > gbWidth - 1 or newblockX[i] < 0 or gbActive[newblockX[i]][newblockY[i]]:
                    blocked = True
            if blocked == False:
                for i in range(self.numblocks):
                    self.blockList[i].gridXPos = newblockX[i]
                    self.blockList[i].gridYPos = newblockY[i]

    def rockbottom(self): # Checks if a shape has hit the bottom of the screen or an active space
      for i in range(self.numblocks):
         gbActive[self.blockList[i].gridXPos][self.blockList[i].gridYPos] = True
         gbActiveColours[self.blockList[i].gridXPos][self.blockList[i].gridYPos] = self.colour
      self.active = False


    def fallingshapes(self): # Makes the shapes fall
        for i in range(self.numblocks):
            if self.blockList[i].gridYPos >= gbHeight -1 or gbActive[self.blockList[i].gridXPos][self.blockList[i].gridYPos + 1] == True:
                self.active = False
                self.rockbottom()
        for i in range(self.numblocks):
            if self.active == True:

                self.blockList[i].gridYPos = self.blockList[i].gridYPos + 1


    def slam(self): # Allows the player to slam the shapes down using a key
        slamsound.play()
        while self.active == True:
            for i in range(4):

                if self.blockList[i].gridYPos == gbHeight - 1: # This if statement must go first/to check if a block is at the bottom
                    self.rockbottom()
                elif gbActive[self.blockList[i].gridXPos][self.blockList[i].gridYPos + 1] == True: # and be followed with this elif statement/to check if the block will hit an active space
                    self.rockbottom()

            for i in range(self.numblocks):
                if self.active:
                    self.blockList[i].gridYPos += 1


    def drawnextshape(self, screen):
        for i in range(self.numblocks):
           pygame.draw.rect(screen,self.blockList[i].colour,[ self.blockList[i].gridXPos  * self.blockList[i].blockSize + 326,
                                                              self.blockList[i].blockSize * self.blockList[i].gridYPos + 151,
                                                              self.blockList[i].blockSize-2, self.blockList[i].blockSize-2], 0)

    def drawnextnextshape(self, screen):
        for i in range(self.numblocks):
            pygame.draw.rect(screen, self.blockList[i].colour, [self.blockList[i].gridXPos * self.blockList[i].blockSize + 326,
                                                                self.blockList[i].blockSize * self.blockList[i].gridYPos + 301,
                                                                self.blockList[i].blockSize - 2, self.blockList[i].blockSize - 2], 0)

    def drawholdshape(self, screen):
        for i in range(self.numblocks):
            pygame.draw.rect(screen, self.blockList[i].colour, [self.shape[i][0] * self.blockList[i].blockSize + 726,
                                                                self.shape[i][1] * self.blockList[i].blockSize + 456,
                                                                self.blockList[i].blockSize - 2, self.blockList[i].blockSize - 2], 0)
