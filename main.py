import pygame
from pygame.locals import *
from guiMenu import GuiMenu
from pongGame import PongGame
from subprocess import call

playGame = True
while playGame:
    menu = GuiMenu()
    action = menu.handleMenu()
    if (action != 0):
        game = PongGame(action)
        game.playPong()
    else:
        playGame = False

# end of program
pygame.quit()
# shutdown rpi
#call("sudo shutdown -h now", shell=True)