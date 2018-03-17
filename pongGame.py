from guiField import GuiField
from player import Player
import pygame
from pygame.locals import *

pygame.init()
clock = pygame.time.Clock()

playerSizeX = 30
playerSizeY = 70

guiField = GuiField()
player1 = Player(guiField.getBorderWidth(), (guiField.getFieldHeight()/2), playerSizeX, playerSizeY, guiField.getFieldStartY(), (guiField.getFieldEndY()-playerSizeY))
# TODO: update variables
#player2 = Player((guiField.getFieldWidth()-guiField.getBorderWidth()), (guiField.getFieldHeight()/2), playerSizeX, playerSizeY, 0, guiField.getFieldHeight())

playPong=True

# DEBUG:
player1.setPosY(140)

def handle_input():
    for event in pygame.event.get():
        # Check if 'esc' or close button is pressed
        if (event.type == QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE)):
            return False
        # Check if 'up' button is pressed
        elif (event.type == pygame.KEYDOWN and event.key == pygame.K_UP):
            # move player 1 100 pixels up
            player1.move(-100);
        # Check if 'down' button is pressed
        elif (event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN):
            # move player 1 100 pixels down
            player1.move(100);
    return True

while playPong:
    guiField.fieldClear()
    #guiField.fieldAddPlayer(10, 200, playerSizeX, playerSizeY, 0)
    guiField.fieldAddPlayer(player1.getPosX(), player1.getPosY(), playerSizeX, playerSizeY, 0)
    #guiField.fieldAddPlayer(player2.getPosX(), player2.getPosY(), playerSizeX, playerSizeY, 0)
    guiField.fieldDisplay()
    
    clock.tick(60)
    
    playPong = handle_input()

# end of programm
del guiField
del player1
del player2
pygame.quit


