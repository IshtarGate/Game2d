# This is a simple game composed by Jake Truelove and 
# James Hounshell in loving collaboration
#
# RIP "the mill"

# IMPORTS
import BasicObjects
import pygame

# INITIAL VARIABLES
pygame.init()
screenSize = width, height = 300, 200
screen = pygame.display.set_mode(screenSize)
isRunning = 1
initialized = 0
enemiesList = []

# STARTING POSITIONS

player1Pos = [int(width / 3), int(height / 2)]
player2Pos = [2 * int(width / 3), int(height / 2)]
ball1Pos = [width / 2, height / 2]

# KEYS
pygame.key.set_repeat(0, 0)

# COLORS
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
blue = (75, 75, 255)
green = (0, 255, 0)

# Some Static Vars
playerSize = 20
bulletLife = 600

# SET UP FPS CLOCK
# http://www.pygame.org/docs/ref/time.html
clock = pygame.time.Clock()  # set up the object "clock" from class "pygame.time.Clock()"

while isRunning:
    # Set Framerate
    clock.tick(60)  # set the game to never run faster than 60 FPS

    for event in pygame.event.get():
        # ENDGAME
        if event.type == pygame.QUIT:
            isRunning = 0  # change isRunning to false

    # Set the initial color of the screen
    screen.fill(black)

    # CONTROLS
    keys = pygame.key.get_pressed()  # get incoming keys every frame
    # this seems more responsive than the "if event.key == pygame.K_a:" shit

    # Exit Game
    if keys[pygame.K_ESCAPE]:  # end the game
        isRunning = 0  # escape ends the game

    # PLAYER 1 CONTROLS
    if keys[pygame.K_a]:  # left or -x
        player1Pos[0] -= 1
    if keys[pygame.K_d]:  # right or +x
        player1Pos[0] += 1
    if keys[pygame.K_w]:  # up or -y
        player1Pos[1] -= 1
    if keys[pygame.K_s]:  # down or +y
        player1Pos[1] += 1
    # fire bullet/ create enemy
    if keys[pygame.K_j]:
        # this appends an instance of the BasicEnemy class to enemiesList
        enemiesList.append(BasicObjects.Bullet(player1Pos, bulletLife))
    # if keys[pygame.K_r]:
    for i in list(range(len(enemiesList) - 1, -1, -1)):
        enemiesList[i].update(player2Pos, playerSize)
        if enemiesList[i].isAlive == 0:  # test
            enemiesList.pop(i)

    # PLAYER 2 CONTROLS
    # def player2controls(keys)
    if keys[pygame.K_KP4]:  # left or -x
        player2Pos[0] -= 1
    if keys[pygame.K_KP6]:  # right or +x
        player2Pos[0] += 1
    if keys[pygame.K_KP8]:  # up or -y
        player2Pos[1] -= 1
    if keys[pygame.K_KP5]:  # down or +y
        player2Pos[1] += 1
    # return player2Pos
    # player2Pos = player2Controls(keys)

    # Ball Movement

    if abs(player1Pos[0] - ball1Pos[0]) <= 20:
        if abs(player1Pos[1] - ball1Pos[1]) <= 20:
            ball1Pos[0] += 1

    # DRAW OBJECTS

    # pygame.draw.rect(screen, green, [player1Pos[0] - playerSize/2,
    # player1Pos[1] - playerSize/2, playerSize/2, playerSize/2], 0)
    pygame.draw.circle(screen, green, player1Pos, playerSize, 0)
    pygame.draw.circle(screen, red, (player2Pos[0], player2Pos[1]), playerSize, 0)
    # pygame.draw.rect(
    # screen, red, [player2Pos[0]-playerSize/2,player2Pos[1]-playerSize/2, playerSize+1, playerSize+1], 0)
    pygame.draw.rect(screen, white, [ball1Pos[0], ball1Pos[1], 2, 2], 0)

    # draw enemies
    for i in list(range(len(enemiesList))):
        pygame.draw.rect(screen, white, [enemiesList[i].position[0], enemiesList[i].position[1], 2, 2], 0)
        # pygame.draw.rect(screen, white, [enemiesList[i].position[0],enemiesList[i].position[0], 2, 2], 0)
    # pygame.draw.circle(screen,white,player1Pos,20 , 1)
    # circle(Surface, color, pos, radius, width=0)
    # key presses

    pygame.display.flip()
    initialized = 1

pygame.quit()  # idle friendly

"""
# Ways to quit the game: 
#     1)isRunning=0 #change isRunning to false(x button)
#     2)isRunning=0 #escape ends the game (escape button)
   

#         if event.type == pygame.KEYDOWN:
#            isRunning=0
#         if event.key == pygame.K_a:
#             playerPos[0]-=1
"""

"""
# we should try to implement classes to take care of repetitive coding
# example below
#
class MyClass: # start defining a new class
    def __init__(self,position): #define initial variables
        self.position=position #define a variable called position (since this is a general case we say "self")
    def update(self): #define a method of MyClass
        self.position=self.position+1 # this function increases self.position by 1
    
jakesClass=MyClass(0)# initiate an instance of "MyClass" called "myClass"
print(jakesClass.position)#print the variable "jakesClass.position"
jakesClass.update() # call the MyClass method "MyClass.update" in this case "jakesClass.update"
print(jakesClass.position) #print the updated jakesClass.position

"""
