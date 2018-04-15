import pygame
from pygame.locals import *
from guiMenu import GuiMenu
from guiSettings import GuiSettings
from pongGame import PongGame
from subprocess import call

# Here so settings stay remembered
settings = GuiSettings()
menu = GuiMenu()

playGame = True
while playGame:
    # get action from menu
    action = menu.handleMenu()
    # check if game needs to start
    if (action == menu.STATE_PLAY):
        # create game
        game = PongGame(10)
        # play game
        game.playPong()
        # delete game
        del game
    # check if settings needs to be openend
    elif (action == menu.STATE_SETTINGS):
        settings.handleMenu()
        print("ball speed:    " + str(settings.getBallSpeed()))
        print("ball size:     " + str(settings.getBallSize()))
        print("player width:  " + str(settings.getPlayerWidth()))
        print("player height: " + str(settings.getPlayerHeight()))
        print("")
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
# shutdown rpi
#call("sudo shutdown -h now", shell=True)