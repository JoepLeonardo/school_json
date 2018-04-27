import pygame
from pygame.locals import *
# pygame init
pygame.mixer.pre_init(22050, -16, 1, 64)
pygame.mixer.init()
pygame.init()

from inputHandler import InputHandler
from guiMenu import GuiMenu
from guiSettings import GuiSettings
from pongGame import PongGame
from subprocess import call

# Create objects here so settings stay remembered
input = InputHandler()
settings = GuiSettings(input)
menu = GuiMenu(input)

playGame = True
while playGame:
    # get action from menu
    action = menu.handleMenu()
    # check if game needs to start
    if (action == menu.STATE_PLAY):
        # create game
        game = PongGame(input, settings.getBallSpeed(), settings.getBallSize(), settings.getPlayerWidth(), settings.getPlayerHeight())
        # play game
        game.playPong()
        # delete game
        del game
        # reset the flags from buttons pressed
        input.reset()
    # check if settings needs to be openend
    elif (action == menu.STATE_SETTINGS):
        settings.handleMenu()
    # check if console must shut down
    elif (action == menu.STATE_POWER_OFF):
        playGame = False
    else:
        print("unknown menu state, exit")
        playGame = False
        
# end of program
pygame.quit()
del menu
del settings
del input
# shutdown rpi
#call("sudo shutdown -h now", shell=True)+