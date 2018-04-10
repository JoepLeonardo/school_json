from displayOnMonitor import DisplayOnMonitor
import pygame
from pygame.locals import *

pygame.init()

class GuiMenu(DisplayOnMonitor):
    
    # display height
    HEIGHT_HEAD = (DisplayOnMonitor.SURFACE_HEIGHT*2/6)
    HEIGHT_NIV = (DisplayOnMonitor.SURFACE_HEIGHT*4/6)
    
    # settings for the game from menu (can't add more niveaus here)
    HEAD_NAME = 'Pong 2D'
    HEAD_SIZE = 200
    NIVEAU_MIN = 1
    NIVEAU_MAX = 3
    NIVEAU1_NAME = 'easy'
    NIVEAU2_NAME = 'medium'
    NIVEAU3_NAME = 'hard'
    NIVEAU_SIZE = 70
          
    def __init__(self):
        pygame.init()
        DisplayOnMonitor.__init__(self)
        # clear the current screen
        self.emptySurfaceScreen()
         # show the drawings
        self.display()
        # settings
        self.continueShow = True
        self.niveau = self.NIVEAU_MIN
        # draw the menu
        self.drawNiv(self.niveau)
                    
    def drawHead(self):
        self.drawText(self.HEAD_NAME, self.HEAD_SIZE, True, self.TEXT_IN_THE_MIDDLE, self.HEIGHT_HEAD)
        
    def getNivName(self, niveau):
        text = ''
        if (niveau == self.NIVEAU_MIN):
            text = self.NIVEAU1_NAME
        elif (niveau == self.NIVEAU_MAX):
            text = self.NIVEAU3_NAME
        else:
            text = self.NIVEAU2_NAME
        return text
        
    def drawNiv(self, niveau):
        # get the niveau text
        text = self.getNivName(niveau)        
        # clear the current screen
        self.emptySurfaceScreen()
        # draw the head text
        self.drawHead()
        # draw the niveau
        self.drawText(('< '+ text + ' >'), self.NIVEAU_SIZE, True, self.TEXT_IN_THE_MIDDLE, self.HEIGHT_NIV)
        # show the drawings
        self.display()
        
    def handleMenu(self):
        action = 0
        while (self.continueShow):
            for event in pygame.event.get():
                if (event.type == QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE)):
                    action = 0
                    self.continueShow = False
                elif (event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT):
                    if (self.niveau > self.NIVEAU_MIN):
                        self.niveau = self.niveau - 1
                    self.drawNiv(self.niveau)
                elif (event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT):
                    if (self.niveau < self.NIVEAU_MAX):
                        self.niveau = self.niveau + 1
                    self.drawNiv(self.niveau)
                elif (event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN):
                    action = self.niveau
                    self.continueShow = False
        # end of while, return menu choice
        return action
                    
                    



