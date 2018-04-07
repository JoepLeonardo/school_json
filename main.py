from guiMenu import GuiMenu
from pongGame import PongGame
from subprocess import call

playGame = True
while playGame:
    menu = GuiMenu()
    action = menu.handleMenu()
    del menu
    if (action != 0):
        game = PongGame(action)
        game.playPong()
        del game
    else:
        playGame = False

# shutdown pi
#call("sudo shutdown -h now", shell=True)