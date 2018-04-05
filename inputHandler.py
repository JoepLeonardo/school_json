import pygame
from pygame.locals import *

pygame.init()

class InputHandler():
    
    def getConsole(self):
        data = 0
        for event in pygame.event.get():
            # Check if 'esc' or close button is pressed
            if (event.type == QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE)):
                data = 1
        return data
                
    def getController1(self):
        data = 0
        for event in pygame.event.get():
            # Check if 'w' button is pressed
            if (event.type == pygame.KEYDOWN and event.key == pygame.K_w):
                data = -1
            # Check if 's' button is pressed
            elif (event.type == pygame.KEYDOWN and event.key == pygame.K_s):
                data = 1
        return data
                
    def getController2(self):
        data = 0
        for event in pygame.event.get():
            # Check if 'up' button is pressed
            if (event.type == pygame.KEYDOWN and event.key == pygame.K_UP):
                data = -1
            # Check if 'down' button is pressed
            elif (event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN):
                data = 1
        return data
            
            
    