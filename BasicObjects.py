# -*- coding: utf-8 -*-
"""
Created on Fri Feb 26 17:51:06 2016

@author: James Hounshell
"""

import pygame
import math

def calcVelocity(position, target):
    """
    calculate velocity using position (start pos) and target (mouse pos)
    :param position: [x,y]
    :param target: [x,y]
    :return: velocity -> [Vx,Vy]
    """
    opposite = target[1] - position[1]
    adjacent = target[0] - position[0]

    if adjacent == 0: # catches divide by zero error when adjacent == 0
        velocity = [0 ,opposite/abs(opposite)]

    elif opposite == 0: # catches divide by zero error when opposite == 0
        velocity = [adjacent/abs(adjacent),0]

    else: # all other cases
        oppDir = opposite/abs(opposite)
        adjDir = adjacent/abs(adjacent)

        #used abs() to keep radians positive
        angle = math.atan(abs(opposite)/abs(adjacent))

        # corrected direction by multiplying by direction +1 -1
        velocity=[math.cos(angle)*adjDir,math.sin(angle)*oppDir]
    return velocity

class Bullet:
    def __init__(self, surface, position, target, life):
        self.position = list(position)
        self.life = life
        self.isAlive = 1
        self.surface = surface
        # calculate velocity
        self.velocity=calcVelocity(position,target)

    def update(self, player2Pos, playerSize):
        self.position[0] = self.position[0] + self.velocity[0]
        self.position[1] = self.position[1] + self.velocity[1]
        self.life = self.life - 1
        if ((player2Pos[0] - self.position[0]) ** 2 + (player2Pos[1] - self.position[1]) ** 2) ** 0.5 < playerSize:
            self.isAlive = 0
        if self.life <= 0:
            self.isAlive = 0

        # draw the bullet
        pygame.draw.line(self.surface, (255,255,255), self.position,self.position, 1)


class Player2:
    """
    Test Docstring
    """

    def __init__(self,screen, position, life):
        self.position = list(position)
        self.life = life
        self.isAlive = 1
        self.screen = screen

    def update(self, keys):
        # PLAYER 2 CONTROLS
        # def player2controls(keys)
        if keys[pygame.K_KP4]:  # left or -x
            self.position[0] -= 1
        if keys[pygame.K_KP6]:  # right or +x
            self.position[0] += 1
        if keys[pygame.K_KP8]:  # up or -y
            self.position[1] -= 1
        if keys[pygame.K_KP5]:  # down or +y
            self.position[1] += 1
        pygame.draw.circle(self.screen, (255,0,0), self.position, 20, 0)

class Player1:
    def __init_(self, position, life, fireRateCountDown):
        self.position = list(position)
        self.life = life
        self.isAlive = 1
        self.fireRateCountDown = fireRateCountDown

    def update(self, keys):
        if keys[pygame.K_KP4]:  # left or -x
            self.position[0] -= 1
        if keys[pygame.K_KP6]:  # right or +x
            self.position[0] += 1
        if keys[pygame.K_KP8]:  # up or -y
            self.position[1] -= 1
        if keys[pygame.K_KP5]:  # down or +y
            self.position[1] += 1


class Timer:
    def __init__(self, frames):
        self.frames = frames

    def update(self):
        self.frames = self.frames - 1


class GameState:
    """
    GameState is a class that is called once per loop that manages all initialized variables and work to draw the game
    """

    def __init__(self):
        # INITIAL VARIABLES
        self.screenSize = width, height = 300, 200
        self.screen = pygame.display.set_mode(self.screenSize)
        self.isRunning = 1
        self.initialized = 0
        self.enemiesList = []

        # STARTING POSITIONS

        self.player1Pos = [int(width / 3), int(height / 2)]
        self.player2Pos = [2 * int(width / 3), int(height / 2)]
        self.ball1Pos = [width / 2, height / 2]

        # KEYS
        #pygame.key.set_repeat(0, 0)

        # COLORS
        self.black = (0, 0, 0)
        self.white = (255, 255, 255)
        self.red = (255, 0, 0)
        self.blue = (75, 75, 255)
        self.green = (0, 255, 0)

        # Some Static Vars
        self.playerSize = 20
        self.bulletLife = 600

        # INITIATE CLASSES
        self.player2 = Player2(self.screen,self.player2Pos, 100)
        # SET UP FPS CLOCK
        # http://www.pygame.org/docs/ref/time.html
        self.clock = pygame.time.Clock()  # set up the object "clock" from class "pygame.time.Clock()"

    def update(self):
        # Set Framerate
        self.clock.tick(60)  # set the game to never run faster than 60 FPS

        for self.event in pygame.event.get():
            if self.event.type == pygame.QUIT:
                self.isRunning = 0  # change self.isRunning to false

        # Set the initial color of the screen
        self.screen.fill(self.black)

        # CONTROLS
        self.keys = pygame.key.get_pressed()  # get incoming keys every frame

        # outputs booleans (0 or 1) if pressed: get_pressed() -> (button1, button2, button3)
        self.mouse = pygame.mouse.get_pressed()

        #get mouse cursor position
        self.cursorPos = pygame.mouse.get_pos()

        # this seems more responsive than the "if event.key == pygame.K_a:" shit

        # Exit Game
        if self.keys[pygame.K_ESCAPE]:  # end the game
            self.isRunning = 0  # escape ends the game

        # PLAYER 1 CONTROLS
        if self.keys[pygame.K_a]:  # left or -x
            self.player1Pos[0] -= 1
        if self.keys[pygame.K_d]:  # right or +x
            self.player1Pos[0] += 1
        if self.keys[pygame.K_w]:  # up or -y
            self.player1Pos[1] -= 1
        if self.keys[pygame.K_s]:  # down or +y
            self.player1Pos[1] += 1
        # fire bullet/ create enemy
        if self.mouse[0] == 1: # old: keys[pygame.K_j]:
            # if shootWait=0 # add a wait timer
            # this appends an instance of the BasicEnemy class to self.enemiesList
            self.enemiesList.append(Bullet(self.screen,self.player1Pos,pygame.mouse.get_pos(),self.bulletLife))

        # PLAYER 2 CONTROLS
        self.player2.update(self.keys)
        # def self.player2controls(keys)
        # if keys[pygame.K_KP4]:  # left or -x
        #     self.self.player2Pos[0] -= 1
        # if keys[pygame.K_KP6]:  # right or +x
        #     self.self.player2Pos[0] += 1
        # if keys[pygame.K_KP8]:  # up or -y
        #     self.self.player2Pos[1] -= 1
        # if keys[pygame.K_KP5]:  # down or +y
        #     self.self.player2Pos[1] += 1
        # return self.self.player2Pos
        # self.self.player2Pos = self.player2Controls(keys)

        # BALL MOVEMENT
        if abs(self.player1Pos[0] - self.ball1Pos[0]) <= 20:
            if abs(self.player1Pos[1] - self.ball1Pos[1]) <= 20:
                self.ball1Pos[0] += 1

        # BULLET INTERACTION
        for i in list(range(len(self.enemiesList) - 1, -1, -1)):
            self.enemiesList[i].update(self.player2.position, self.playerSize)
            if self.enemiesList[i].isAlive == 0:  # test
                self.enemiesList.pop(i)

        # DRAW OBJECTS

        # pygame.draw.rect(self.screen, self.green, [self.player1Pos[0] - self.playerSize/2,
        # self.player1Pos[1] - self.playerSize/2, self.playerSize/2, self.playerSize/2], 0)
        pygame.draw.circle(self.screen, self.green, self.player1Pos, self.playerSize, 0)
        # pygame.draw.circle(self.screen, self.red, self.player2.position, self.playerSize, 0)
        # pygame.draw.rect(
        # self.screen, self.red, [self.self.player2Pos[0]-self.playerSize/2,self.self.player2Pos[1]-self.playerSize/2, self.playerSize+1, self.playerSize+1], 0)
        pygame.draw.rect(self.screen, self.white, [self.ball1Pos[0], self.ball1Pos[1], 2, 2], 0)

        # draw enemies
        # for i in list(range(len(self.enemiesList))):
        #     pygame.draw.rect(self.screen, self.white,
        #                      [self.enemiesList[i].position[0], self.enemiesList[i].position[1], 2, 2], 0)
            # pygame.draw.rect(self.screen, self.white, [self.enemiesList[i].position[0],self.enemiesList[i].position[0], 2, 2], 0)
        # pygame.draw.circle(self.screen,self.white,self.player1Pos,20 , 1)
        # circle(Surface, color, pos, radius, width=0)
        # key presses

        pygame.display.flip()
        self.initialized = 1

        #print fps
        # print(self.clock.get_fps())

        return self.isRunning

        # End of file
