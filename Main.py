# This is a simple game composed by Jake Truelove and 
# James Hounshell in loveing collaboration
#
# RIP "the mill"

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

#IMPORTS

import pygame


#INITIAL VARIABLES
pygame.init()
size = width, height = 300, 200
screen=pygame.display.set_mode(size)

isRunning=1
initialized=0

#STARTING POSITIONS

player1Pos=[int(width/3), int(height/2)]
player2Pos=[2*width/3,height/2]
ball1Pos=[width/2, height/2]


#KEYS
pygame.key.set_repeat (1, 1)

#COLORS
black=(0,0,0)
white=(255,255,255)
red=(255,0,0)
blue=(75,75,255)
green=(0,255,0)

#SET UP FPS CLOCK
# http://www.pygame.org/docs/ref/time.html
clock=pygame.time.Clock() # set up the object "clock" from class "pygame.time.Clock()"


while isRunning:
    #Set Framerate
    clock.tick(60) # set the game to never run faster than 30 FPS
    
    for event in pygame.event.get():
        #ENDGAME
        if event.type == pygame.QUIT:
            isRunning=0 #change isRunning to false
    
    screen.fill(black)
    

    #CONTROLS
    keys=pygame.key.get_pressed() # get incoming keys every frame
    
    #Exit Game
    if keys[pygame.K_ESCAPE]:#end the game
        isRunning=0 #escape ends the game

    #PLAYER 1 CONTROLS

    if keys[pygame.K_a]:#left or -x
        player1Pos[0]-=1
    if keys[pygame.K_d]:#right or +x
        player1Pos[0]+=1
    if keys[pygame.K_w]:#up or -y
        player1Pos[1]-=1
    if keys[pygame.K_s]:#down or +y
        player1Pos[1]+=1

    #PLAYER 2 CONTROLS
    #def player2controls(keys)
    if keys[pygame.K_KP4]:#left or -x
        player2Pos[0]-=1
    if keys[pygame.K_KP6]:#right or +x
        player2Pos[0]+=1
    if keys[pygame.K_KP8]:#up or -y
        player2Pos[1]-=1
    if keys[pygame.K_KP5]:#down or +y
        player2Pos[1]+=1
    #return player2Pos
    #player2Pos = player2Controls(keys)
            
    #Ball Movement

    if abs(player1Pos[0] - ball1Pos[0]) <= 20:
        if abs(player1Pos[1] - ball1Pos[1]) <=20:
            ball1Pos[0]+=1
        
        

        
    #DRAW OBJECTS
        
    playerSize = 32
    #pygame.draw.rect(screen, green, [player1Pos[0] - playerSize/2,player1Pos[1] - playerSize/2, playerSize/2, playerSize/2], 0)
    pygame.draw.circle(screen, green, (player1Pos[0], player1Pos[1]), 20, 1)
    pygame.draw.rect(screen, red, [player2Pos[0],player2Pos[1], 2, 2], 0)
    pygame.draw.rect(screen, white, [ball1Pos[0],ball1Pos[1], 2, 2], 0)

    #pygame.draw.circle(screen,white,newPlayerPos,20 , 1)
    #circle(Surface, color, pos, radius, width=0)
    #key presses


    pygame.display.flip()
    initialized=1

pygame.quit(); #idle friendly

# Ways to quit the game: 
#     1)isRunning=0 #change isRunning to false(x button)
#     2)isRunning=0 #escape ends the game (escape button)
   
# return playerPos,playerSpeed,playerMoveInitialized


#         if event.type == pygame.KEYDOWN:
#            isRunning=0
#         if event.key == pygame.K_a:
#             playerPos[0]-=1
#         if event.key == pygame.K_d:
#             playerPos[0]+=1
#         if event.key == pygame.K_w:
#             playerPos[1]-=1
#         if event.key == pygame.K_s:
#             playerPos[1]+=1

