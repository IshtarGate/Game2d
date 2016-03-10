# -*- coding: utf-8 -*-
"""
Created on Fri Feb 26 17:51:06 2016

@author: James Hounshell
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
class Bullet:
    def __init__(self,position,life):
        self.position=list(position)
        self.life=life
        self.isAlive=1
    def update(self,player2Pos,playerSize):
        self.position[0]=self.position[0]+1
        self.life=self.life-1
        if ((player2Pos[0]-self.position[0])**2+(player2Pos[1]-self.position[1])**2)**0.5<playerSize:
            self.isAlive=0
        if self.life<=0:
            self.isAlive=0
