from displayOnMonitor import DisplayOnMonitor
from inputHandler import InputHandler
import pygame
from pygame.locals import *
import time

pygame.init()

class GuiMenu(DisplayOnMonitor):
    
    # display height
    HEIGHT_HEAD = (DisplayOnMonitor.SURFACE_HEIGHT*2/6)
    HEIGHT_ITEM1 = (DisplayOnMonitor.SURFACE_HEIGHT*4/6)
    HEIGHT_ITEM2 = (DisplayOnMonitor.SURFACE_HEIGHT*5/6)
    # settings for the game from menu (can't add more niveaus here)
    HEAD_NAME = 'Pong 2D'
    HEAD_SIZE = 200
    ITEM_PLAY_NAME = 'Play'
    ITEM_SETTINGS_NAME = 'Settings'
    ITEM_SIZE = 70
    # Menu state
    GAME_STATE = None
    STATE_PLAY = 10
    STATE_SETTINGS = 11
    STATE_RETURN = 12
    STATE_POWER_OFF = 13    
          
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
        if (self.GAME_STATE == self.STATE_PLAY):
            self.drawTextMiddle(self.ITEM_PLAY_NAME, self.ITEM_SIZE, self.HEIGHT_ITEM1, True)
            self.drawTextMiddle(self.ITEM_SETTINGS_NAME, self.ITEM_SIZE, self.HEIGHT_ITEM2, False)
        else:
            self.drawTextMiddle(self.ITEM_PLAY_NAME, self.ITEM_SIZE, self.HEIGHT_ITEM1, False)
            self.drawTextMiddle(self.ITEM_SETTINGS_NAME, self.ITEM_SIZE, self.HEIGHT_ITEM2, True)
        # show the drawings
        self.display()
                   
    def handleMenu(self):
        self.reset()
        # draw the menu
        self.drawMenu()
        while (self.continueShow):
            data = self.input.getConsole()
            
            if (data == self.input.DATA_POWER_OFF):
                self.GAME_STATE = self.STATE_POWER_OFF
                self.continueShow = False                
            elif ((data == self.input.DATA_PREV) or (data == self.input.DATA_NEXT)):
                if (self.GAME_STATE != self.STATE_PLAY):
                    self.GAME_STATE = self.STATE_PLAY
                else:
                    self.GAME_STATE = self.STATE_SETTINGS
                self.drawMenu()
            elif (data == self.input.DATA_SELECT):
                self.continueShow = False                  
        # end of while, return menu choice
        return (self.GAME_STATE)
    