from displayOnMonitor import DisplayOnMonitor
from inputHandler import InputHandler
import pygame
from pygame.locals import *
import time

pygame.init()

class GuiSettings(DisplayOnMonitor):

    HEIGHT_ITEM = (DisplayOnMonitor.SURFACE_HEIGHT*1/6)
    ITEM_SPEED_NAME = 'Speed'
    ITEM_SIZE = 70
    # Delay (ms)
    DELAY_BETWEEN_INPUT = 300

    def __init__(self):
        # create object(s)
        self.input = InputHandler()
        # settings
        self.continueShow = True
            
    def __del__(self):
        print("exit guiSettings")
        
    def reset(self):
        DisplayOnMonitor.__init__(self)
        self.continueShow = True
        
    def drawMenu(self):
        # clear the current screen
        self.emptySurfaceScreen()
        # draw items
        self.drawTextMiddle(self.ITEM_SPEED_NAME, self.ITEM_SIZE, self.HEIGHT_ITEM, True)
        # show the drawings
        self.display()
        
    def handleMenu(self):
        # reset
        self.reset()
        # draw the menu
        self.drawMenu()
        data = self.input.DATA_NONE        
        while (self.continueShow):
            data = self.input.getConsole()
            
            if (data == self.input.DATA_POWER_OFF):
                self.continueShow = False                
            elif ((data == self.input.DATA_PREV) or (data == self.input.DATA_NEXT)):                
                self.drawMenu()
            elif (data == self.input.DATA_SELECT):
                self.drawMenu()
                
            pygame.time.delay(self.DELAY_BETWEEN_INPUT)
    
    
    