#####################################################
#
#        main.py functionality:
#
# * file that starts the game
# * connects all the components (guiMenu.py, guiSettings.py, pongGame.py)
# * bug fix: plays on startup one sound here
#
#####################################################

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

# Hide the cursor
pygame.mouse.set_visible(False)

# Create objects here so settings stay remembered
input = InputHandler()
settings = GuiSettings(input)
menu = GuiMenu(input)

# Bug fix, the first sound the game plays doesn't make sound.
pygame.mixer.Sound('/home/pi/Desktop/pong2d/pong_8bit_scored.wav').play(0)

playGame = True
shutDown = False
while playGame:
    # get action from menu
    action = menu.handleMenu()
    # check if game needs to start
    if (action == menu.STATE_PLAY):
        # create game
        game = PongGame(input, settings.getMaxScore(), settings.getBallSpeed(), settings.getBallSize(), settings.getPlayerWidth(), settings.getPlayerHeight())
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
        shutDown = True
    # check if console must exit the game
    elif (action == menu.STATE_DEBUG_EXIT):
        playGame = False
    else:
        print("unknown menu state, exit")
        playGame = False

# end of game so exit program
pygame.quit()
del menu
del settings
del input
# shutdown rpi
if (shutDown):
    call("sudo shutdown -h now", shell=True)
# end
