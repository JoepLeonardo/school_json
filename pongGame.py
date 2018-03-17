from guiField import GuiField
import pygame
from pygame.locals import *
pygame.init()

guiField = GuiField()

def handle_input():
    for event in pygame.event.get():
        if event.type == QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE) :
            pygame.display.quit() 
            pygame.quit()

while True:
    handle_input()
    guiField.clearSurface()