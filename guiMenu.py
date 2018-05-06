#####################################################
#
#        guiMenu.py functionality:
#
# * inheritance from displayOnMonitor.py
# * contains all the head menu info
# * handles the head menu via inputHandler.py
# * draws everything scaled
# * debug: keyboard esc key can end the program without shutting down
#
#####################################################

from displayOnMonitor import DisplayOnMonitor
from inputHandler import InputHandler
import pygame
from pygame.locals import *
import time

pygame.init()

class GuiMenu(DisplayOnMonitor):
    
    # display height
    HEIGHT_HEAD = (DisplayOnMonitor.SURFACE_HEIGHT*2/7)
    HEIGHT_ITEM1 = (DisplayOnMonitor.SURFACE_HEIGHT*4/7)
    HEIGHT_ITEM2 = (DisplayOnMonitor.SURFACE_HEIGHT*5/7)
    HEIGHT_ITEM3 = (DisplayOnMonitor.SURFACE_HEIGHT*6/7)
    # settings for the game from menu (can't add more niveaus here)
    HEAD_NAME = 'Pong 2D'
    HEAD_SIZE = 200
    ITEM_PLAY_NAME = 'Play'
    ITEM_SETTINGS_NAME = 'Settings'
    ITEM_POWER_OFF_NAME = 'Turn Off'
    ITEM_SIZE = 70
    # Menu state
    GAME_STATE = None
    STATE_PLAY = 10
    STATE_SETTINGS = 11
    STATE_POWER_OFF = 12
    STATE_MIN = STATE_PLAY
    STATE_MAX = STATE_POWER_OFF    
    # Debug code to exit the game via keyboard
    STATE_DEBUG_EXIT = 13
          
    def __init__(self, inInput):
        # create object(s)
        #self.input = InputHandler()
        self.input = inInput
        # settings
        self.continueShow = True
    
    #def __del__(self):
        #print("exit guiMenu")
    
    def reset(self):
        DisplayOnMonitor.__init__(self)
        self.continueShow = True
        self.GAME_STATE = self.STATE_PLAY
                                            
    def drawMenu(self):
        # clear the current screen
        self.emptySurfaceScreen()
        # draw the head text
        self.drawTextMiddle(self.HEAD_NAME, self.HEAD_SIZE, self.HEIGHT_HEAD, False)
        # draw items
        self.drawTextMiddle(self.ITEM_PLAY_NAME, self.ITEM_SIZE, self.HEIGHT_ITEM1, (self.GAME_STATE == self.STATE_PLAY))
        self.drawTextMiddle(self.ITEM_SETTINGS_NAME, self.ITEM_SIZE, self.HEIGHT_ITEM2, (self.GAME_STATE == self.STATE_SETTINGS))
        self.drawTextMiddle(self.ITEM_POWER_OFF_NAME, self.ITEM_SIZE, self.HEIGHT_ITEM3, (self.GAME_STATE == self.STATE_POWER_OFF))       
        # show the drawings
        self.display()
        
    def handleKeyboardInput(self):
        for event in pygame.event.get():
            # Check if 'esc' or close button is pressed
            if (event.type == QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE)):
                self.continueShow = False
                self.GAME_STATE = self.STATE_DEBUG_EXIT                
                   
    def handleMenu(self):
        self.reset()
        # draw the menu
        self.drawMenu()
        while (self.continueShow):
            # get input form console
            data = self.input.getConsole()
            
            # PRESSED NEXT
            if (data == self.input.DATA_NEXT):
                if (self.GAME_STATE < self.STATE_MAX):
                    self.GAME_STATE = self.GAME_STATE + 1
                else:
                    self.GAME_STATE= self.STATE_MIN
                self.drawMenu()
            # PRESSED PREV
            elif (data == self.input.DATA_PREV):
                if (self.GAME_STATE > self.STATE_MIN):
                    self.GAME_STATE = self.GAME_STATE - 1
                else:
                    self.GAME_STATE= self.STATE_MAX
                self.drawMenu()    
            # PRESSED SELECT
            elif (data == self.input.DATA_SELECT):
                self.continueShow = False
            # Check keyboard
            self.handleKeyboardInput()
        # end of while, return menu choice
        return (self.GAME_STATE)
    