# This is a simple game composed by Jake Truelove and 
# James Hounshell in loving collaboration
#
# RIP "the mill"

# IMPORTS
import BasicObjects
import pygame


pygame.init()
myGameState = BasicObjects.GameState()

isRunning=1
while isRunning:
    isRunning=myGameState.update()

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
