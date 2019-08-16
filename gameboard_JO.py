import pygame
import random
gbWidth = 12 # Sets the dimensions of the gameboard, along with its current number of active spaces
gbHeight = 20
gbActive = [[0 for y in range(gbHeight)]for x in range(gbWidth)]
gbActiveColours = [[0 for y in range(gbHeight)]for x in range(gbWidth)]
pygame.init()
lineclear = pygame.mixer.Sound("clear.wav")
slamsound = pygame.mixer.Sound("fall.wav")
gameover = pygame.mixer.Sound("gameover.wav")
gotem = pygame.mixer.Sound("gotthem.wav")
TURQUOISE = (66, 239, 245)
MAGENTA = (252, 3, 127)
INDIGO = (112, 54, 247)
LIME = (81, 255, 0)
BEIGE = (235, 107, 52)
class gameboard():
    def __init__(self, colour, blockSize): # Constructor for a new gameboard
        self.randomcolour = random.randrange(0, 5)
        self.borderColour = [MAGENTA, LIME, BEIGE, INDIGO, TURQUOISE]
        self.multiplier = blockSize
        self.score = 0
        self.linescleared = 0
        self.level = 1
        self.clockpower = 0
        self.swappower = 30
        self.slowTime = False
        self.swapOne = False
        for y in range(gbWidth):
            for x in range(gbHeight):
                 gbActive[y][x] = False
                 gbActiveColours[y][x] = (76, 0, 0)

    def draw(self, screen): # Draws the gameboard on the screen
        pygame.draw.rect(screen, self.borderColour[self.randomcolour], [0, 0, self.multiplier * gbWidth, self.multiplier * gbHeight], 1)
        for num in range(1, gbWidth):
            pygame.draw.line(screen, self.borderColour[self.randomcolour], (self.multiplier * num, 0), (self.multiplier * num, self.multiplier * gbHeight - 1), 1)
        for num in range(1, gbHeight):
            pygame.draw.line(screen, self.borderColour[self.randomcolour], (0, self.multiplier * num), (self.multiplier * gbWidth - 1,self.multiplier * num), 1)
        for y in range(gbWidth):
            for x in range(gbHeight):
                if gbActive[y][x] == True:
                    pygame.draw.rect(screen, gbActiveColours[y][x], [y * self.multiplier + 1, x * self.multiplier + 1, self.multiplier-2, self.multiplier-2],0)

    def isthisloss(self): # checks for a game loss and returns a value

        for i in range(gbWidth):
            if gbActive[i][0] == True:

                gameover.play()
                return True
        return False

    def completerows(self,rowNum): # checks for (a) complete row(s) and returns a value
        for i in range(gbWidth):
            if gbActive[i][rowNum] == False:
                return False
        return True
    def clearrows(self): # Clears the row and moves all others down by 1
        tetris = 0
        for rowNum in range(gbHeight):
            if self.completerows(rowNum) == True:
                tetris += 1
                lineclear.play()
                self.score += 100
                self.linescleared += 1
                if self.linescleared >= 10:
                    self.linescleared = 0
                    self.level += 1
                    self.clockpower +=1
                    self.swappower += 1
                for c in range(rowNum, 1, -1):
                    for i in range(gbWidth):
                        gbActive[i][c] = gbActive[i][c-1]
                        gbActiveColours[i][c] = gbActiveColours[i][c-1]

                for i in range(gbActive[i][0]):
                    gbActiveColours[i][0] = (0,0,0)
        if tetris == 2:
            self.score += 50
        elif tetris == 3:
            self.score += 200
        elif tetris == 4:
            self.score += 400
            gotem.play()



