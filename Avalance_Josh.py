import pygame  # Import the pygame library
import random
import time
from block_JO import block
from gameboard_JO import gameboard
from shape_JO import shape
from ghostshapes_JO import ghostshapes
BLACK = (0, 0, 0)  # RGB Values for colours of blocks
BLUE = (54, 238, 224)
TURQUOISE = (66, 239, 245)
GREEN = (87, 245, 66)
RED = (224, 38, 38)
YELLOW = (224, 227, 68)
ORANGE = (224, 144, 38)
PURPLE = (177, 68, 227)
MAGENTA = (252, 3, 127)
INDIGO = (112, 54, 247)
LIME = (81, 255, 0)
BEIGE = (235, 107, 52)
delay = 0

shapetimer = 0
def keycheck(): # Function that checks for keys being pressed during the game
    if event.key == pygame.K_UP:
        Shape.rotationCW()
    elif event.key == pygame.K_SPACE:
        Shape.slam()
    elif event.key == pygame.K_RSHIFT:
        Shape.rotationCCW()
    elif event.key == pygame.K_DOWN:
        Shape.movedown()
    elif event.key == pygame.K_LEFT:
        Shape.moveleft()
    elif event.key == pygame.K_RIGHT:
        Shape.moveright()
    elif event.key == pygame.K_F1:
        pygame.mixer.music.load("Sonic.mp3")
        pygame.mixer.music.play(4)
    elif event.key == pygame.K_F2:
        pygame.mixer.music.load("Duck.mp3")
        pygame.mixer.music.play(10)
    elif event.key == pygame.K_F3:
        pygame.mixer.music.load("Tetris.mp3")
        pygame.mixer.music.play(10)
    elif event.key == pygame.K_F4:
        pygame.mixer.music.load("TTA.mp3")
        pygame.mixer.music.play(5)
    elif event.key == pygame.K_F5:
        pygame.mixer.music.load("X.mp3")
        pygame.mixer.music.play(5)
    elif event.key == pygame.K_i:
        nextshape.changeshape(1)
    elif event.key == pygame.K_j:
        nextshape.changeshape(0)
    elif event.key == pygame.K_l:
        nextshape.changeshape(5)
    elif event.key == pygame.K_s:
        nextshape.changeshape(2)
    elif event.key == pygame.K_z:
        nextshape.changeshape(3)
    elif event.key == pygame.K_q:
        nextshape.changeshape(4)
    elif event.key == pygame.K_t:
         nextshape.changeshape(6)
    elif event.key == pygame.K_n and Gameboard.clockpower > 0:
        Gameboard.clockpower -= 1
        Gameboard.slowTime = True
    elif event.key == pygame.K_m and Gameboard.swappower > 0:
        Gameboard.swappower -= 1
        Gameboard.swapOne = True


if __name__ == "__main__" : # The startup statement

    pygame.init()  # Initializes the game engine function
    pygame.display.set_caption("Josh's Ultimate Avalanche Game!")  # Set the window title
    name = ""
    started = False
    educated = False
    size = (975, 575)  # Set the screen variable
    screen = pygame.display.set_mode(size)  # Initialize the screen size
    pygame.mixer.init()
    pygame.mixer.music.load("Namco.mp3")
    pygame.mixer.music.play(3)
    myfont = pygame.font.Font("freesansbold.ttf", 30)
    highscorefont = pygame.font.Font("freesansbold.ttf", 20)
    smallfont = pygame.font.Font("freesansbold.ttf", 14)
    namelist = [0 for i in range(8)]
    scorelist = [0 for i in range(8)]
    highscorefile = open("highscore.txt", "r")
    for i in range(8):
        namelist[i] = highscorefile.readline().rstrip("\n")
    for i in range(8):
        scorelist[i] = highscorefile.readline().rstrip("\n")
    highscorefile.close()
    blockSize = 25
    blockXPos = 120
    blockYPos = 200
    Gameboard = gameboard(MAGENTA, blockSize)
    Shape = shape()
    nextshape = shape()
    nextnextshape = shape()
    ghostshape = ghostshapes(Shape.shapenum)
    holdShape = None

    done = False
def newhighscore():
    tempScoreArray = [0 for i in range(8)]
    tempNameArray = [0 for i in range(8)]
    isHighScore = False
    for i in range(8):
        if Gameboard.score > int(scorelist[i]) and isHighScore == False:
            tempNameArray[i] = name
            tempScoreArray[i] = Gameboard.score
            isHighScore = True
        elif isHighScore == True:
            tempNameArray[i] = namelist[i - 1]
            tempScoreArray[i] = scorelist[i-1]
        else:
            tempScoreArray[i] = scorelist[i]
            tempNameArray[i] = namelist[i]
    for i in range(8):
        namelist[i] = tempNameArray[i]
        scorelist[i] = tempScoreArray[i]
    highscorefile = open("highscore.txt", "w")
    for i in range(8):
        highscorefile.write(str(namelist[i]) + "\n")
    for i in range(8):
        highscorefile.write(str(scorelist[i]) + "\n")
    highscorefile.close()
def instructions():
    screen.fill(BLACK)
    line1 = smallfont.render("Are you ready to play some Avalanche? Here's how to play.", 1, INDIGO)
    line2 = smallfont.render("Press on the arrow keys to move your shape left, right or down.", 1, INDIGO)
    line3 = smallfont.render("The up arrow key rotates clockwise and the LShift key rotates counter-clockwise.", 1, INDIGO)
    line4 = smallfont.render("Press SPACE to slam your shape down, N to slow time, and M to hold/swap shapes.(Watch your powerup quantities!)", 1, INDIGO)
    line5 = smallfont.render("To help a player out, you can press the corresponding letter key to alter the next shape.\n Q for Square, I for Line and so on.", 1, INDIGO)
    line6 = smallfont.render("Try to get a high score by completing lines in the grid using the shapes given.", 1, INDIGO)
    line7 = smallfont.render("Change your music at any time during the game by pressing F1, 2, 3, 4 or 5.", 1, INDIGO)
    line8 = smallfont.render("P.S. Watch out for Level 10 and above!", 1, INDIGO)
    screen.blit(line1,(00, 00))
    screen.blit(line2,(00, 80))
    screen.blit(line3,(00, 160))
    screen.blit(line4,(00, 240))
    screen.blit(line5,(00, 320))
    screen.blit(line6,(00, 400))
    screen.blit(line7,(00, 480))
    screen.blit(line8,(00, 560))
    pygame.display.flip()

def screenload():# Loads the screen and all objects on it
    screen.fill(BLACK)
    ghostshape.drawghostshapes(screen)
    Gameboard.draw(screen)

    for num in range(6):
        pygame.draw.line(screen, YELLOW, (Gameboard.multiplier * num + 400,  100), (Gameboard.multiplier * num + 400, Gameboard.multiplier * 12 + 99), 1)
    for num in range(12):
        pygame.draw.line(screen, YELLOW, (400, Gameboard.multiplier * num + 100), (399+ Gameboard.multiplier * 6, Gameboard.multiplier * num + 100), 1)
    for num in range(6):
        pygame.draw.line(screen, BEIGE, (Gameboard.multiplier * num + 800,  405), (Gameboard.multiplier * num + 800, Gameboard.multiplier * 6 + 404), 1)
    for num in range(6):
        pygame.draw.line(screen, BEIGE, (800, Gameboard.multiplier * num + 405), (799 + Gameboard.multiplier * 6, Gameboard.multiplier * num + 405), 1)
    pygame.draw.rect(screen, YELLOW, [400, 100, 6 * Shape.blockList[0].blockSize, 12 * Shape.blockList[0].blockSize], 1)
    pygame.draw.rect(screen, PURPLE, [575, 100, 223, 300], 1)
    pygame.draw.rect(screen, BEIGE, [800, 405, 6 * Shape.blockList[0].blockSize, 6 * Shape.blockList[0].blockSize], 1)
    leveltext = myfont.render("Level: " + str(Gameboard.level) , 1, YELLOW )
    scoretext = myfont.render("Score: " + str(Gameboard.score), 1, YELLOW)
    newshapetext = myfont.render("Next", 1, YELLOW)
    highscoretext = myfont.render("HIGH SCORES: ", 1, PURPLE)
    clocktext = highscorefont.render("Clocks: " + str(Gameboard.clockpower), 1, BLUE)
    swaptext = highscorefont.render("Swaps: " + str(Gameboard.swappower), 1, BLUE)
    holdtext = highscorefont.render("Hold", 1, BEIGE)
    clocks = pygame.image.load("clock.png")
    swaps = pygame.image.load("swap.png")
    screen.blit(swaptext, (575, 475))
    screen.blit(swaps, (670, 440))
    screen.blit(clocktext, (575, 500))
    screen.blit(clocks, (670, 490))
    screen.blit(scoretext,(375, 525))
    screen.blit(leveltext,(375, 460))
    screen.blit(newshapetext,(410, 50))
    screen.blit(highscoretext,(575, 50))
    screen.blit(holdtext, (850, 380))
    for i in range(8):
        hsnametext = highscorefont.render(str(namelist[i]), 1, PURPLE)
        screen.blit(hsnametext,(580, 140 + 30 * i))
    for i in range(8):
        hsscoretext = highscorefont.render(str(scorelist[i]), 1, PURPLE)
        screen.blit(hsscoretext,(700, 140 + 30 * i))
    Shape.draw(screen)
    nextshape.drawnextshape(screen)
    nextnextshape.drawnextnextshape(screen)
    if holdShape != None:
        holdShape.drawholdshape(screen)

    playernametext = myfont.render(name, 1, GREEN)
    screen.blit(playernametext, (50, 525))
    pygame.display.flip()  # Updates the screen with everything drawn
while not started:
    enterednametext = myfont.render(name, 1, RED)
    nametext = myfont.render("Please enter your name here!", 1, RED)
    musictext = highscorefont.render("Press F1, 2, 3, 4 or 5 for different music!", 1, RED)
    titlescreen = pygame.image.load("Backdrop.png")
    screen.blit(nametext,(180, 286))
    screen.blit(enterednametext,(300, 325))
    pygame.display.flip()
    screen.blit(titlescreen,(0,0))
    screen.blit(musictext,(370, 500))


    for event in pygame.event.get():  # for loop that cchecks for events that happen within the game
        if event.type == pygame.QUIT:
            educated = True
            started = True
            done = True
        if event.type == pygame.KEYDOWN:
            if event.key >= 33 and event.key <= 126 and len(name) < 10:
                name = name + chr(event.key)
            if event.key == pygame.K_RETURN:
                if name == "":
                    name = "NiceName"
                started = True
            if event.key == pygame.K_BACKSPACE:
                name = name[:-1]
while not educated:
    instructions()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            educated = True
            done = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                started = True
                educated = True
while not done:  # While loop that runs the game

    screenload()
    ADDTIME = 0.1


    if Gameboard.slowTime == True:
        delay = delay + ADDTIME
        if delay >= 10:
            Gameboard.slowTime = False
            delay = 0
    if Gameboard.swapOne == True:
        if holdShape == None:
            holdShape = Shape
            Shape = nextshape
            nextshape = nextnextshape
            nextnextshape = shape()
        else:
            tempShape = Shape
            Shape = holdShape
            holdShape = tempShape


        ghostshape.colour = Shape.colour
        Shape.draw(screen)
        nextshape.drawnextshape(screen)

        Gameboard.swapOne = False

    if (0.11 - Gameboard.level *0.01) >= 0:
        time.sleep(0.11- Gameboard.level * 0.01 + Gameboard.slowTime * ADDTIME)
    shapetimer += 1 # Timer for falling shapes
    if shapetimer >= 11:
        shapetimer = 0
        Shape.fallingshapes()
    for event in pygame.event.get():  # for loop that cchecks for events that happen within the game
        if event.type == pygame.QUIT:
            done = True
        if Shape.active == True:
            if event.type == pygame.KEYDOWN:
                keycheck()
    if Shape.active == False:
        Gameboard.score += 5
        Shape = nextshape
        nextshape = nextnextshape
        nextnextshape = shape()
        ghostshape = ghostshapes(Shape.shapenum)
    Gameboard.clearrows()

    if Gameboard.isthisloss() == True: # Checking if there is a loss to reset
        newhighscore()
        Gameboard = gameboard(MAGENTA, blockSize)

        Shape = shape()
        ghostshape = ghostshapes(Shape.shapenum)


    ghostshape.update(Shape)


