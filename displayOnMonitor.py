import pygame
from pygame.locals import *

pygame.init()

class DisplayOnMonitor:
    # monitor resoluten
    MONITOR_WIDTH = pygame.display.Info().current_w
    MONITOR_HEIGHT = pygame.display.Info().current_h
    
    # surface resolution CTOUCH (1824x984)
    SURFACE_WIDTH = 1824
    SURFACE_HEIGHT = 984
        
    # colors
    COLOR_WHITE = (255, 255, 255)
    COLOR_BLACK = (0, 0, 0)
    COLOR_DEBUG1 = (0, 255, 0)
    COLOR_DEBUG2 = (0, 155, 255)
    
    # text settings
    FONT = 'Arial'
    TEXT_IN_THE_MIDDLE = 9999
    
    def __init__(self):        
        # create monitor screen where surface is going to be displayed on |FULLSCREEN
        self.monitorScreen = pygame.display.set_mode((self.MONITOR_WIDTH, self.MONITOR_HEIGHT),HWSURFACE|DOUBLEBUF)
        # create surface screen where all items are going to be displayed on
        self.surfaceScreen = pygame.Surface((self.SURFACE_WIDTH, self.SURFACE_HEIGHT))      
           
    def __del__(self):
        # close the display
        pygame.display.quit()
            
    def emptySurfaceScreen(self):
        # make the surface black
        self.surfaceScreen.fill(self.COLOR_BLACK)
    
    # draw a rect
    def drawRect(self, posX, posY, width, height):
        pygame.draw.rect(self.surfaceScreen, self.COLOR_WHITE, pygame.Rect(posX, posY, width, height))
    
    # draw a rect thats open from the inside
    def drawRectOpen(self, posX, posY, width, height, open):
        pygame.draw.rect(self.surfaceScreen, self.COLOR_WHITE, pygame.Rect(posX, posY, width, height), open)
        
    # DEBUG function to draw a rect in color    
    def drawRectDebug1(self, posX, posY, width, height):
        pygame.draw.rect(self.surfaceScreen, self.COLOR_DEBUG1, pygame.Rect(posX, posY, width, height))
    
    # DEBUG function to draw a rect in color    
    def drawRectDebug2(self, posX, posY, width, height):
        pygame.draw.rect(self.surfaceScreen, self.COLOR_DEBUG2, pygame.Rect(posX, posY, width, height))
    
    # remove a rect
    def removeRect(self, posX, posY, width, height):
        pygame.draw.rect(self.surfaceScreen, self.COLOR_BLACK, pygame.Rect(posX, posY, width, height))
        
    def drawText(self, text, size, bold, x, y):
        # Create the text on a surface
        myfont = pygame.font.SysFont(self.FONT, size, bold)
        surfaceText = myfont.render(text, False, self.COLOR_WHITE)
        # Check if text needs to be placed in the middle of the x-axis
        if (x==self.TEXT_IN_THE_MIDDLE):
            x = (self.SURFACE_WIDTH/2) - (surfaceText.get_width()/2)
        # Put text on surfaceScreen
        self.surfaceScreen.blit(surfaceText,(x, y))
        
                
    # display the surface on the monitor
    def display(self):
        # adjust and update the surfaceScreen to the monitorScreen
        pygame.transform.scale(self.surfaceScreen, (self.MONITOR_WIDTH, self.MONITOR_HEIGHT), self.monitorScreen)
        # display
        pygame.display.flip()
        
        



