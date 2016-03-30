"""
This is a simple game composed by James Hounshell in loving collaboration with Jake Truelove
"""

# IMPORTS
import BasicObjects
import pygame

pygame.init()
myGameState = BasicObjects.GameState()

isRunning = 1
while isRunning:
    isRunning = myGameState.update()
pygame.quit()  # idle friendly

# End of Main.py
