from displayOnMonitor import DisplayOnMonitor
import pygame
from pygame.locals import *
pygame.init()

class GuiField(DisplayOnMonitor):
    # CTOUCH resolution (1824x984)
    surfaceWidth = 1824
    surfaceHeight = 984
    # size above the game to display score and gamename
    surfaceTop = 100
    # create surface screen where all items are going to be displayed on
    surfaceScreen = pygame.Surface((surfaceWidth, surfaceHeight))

    # colors
    colorWhite = (255, 255, 255)
    colorBlack = (0, 0, 0)
           
    def clearSurface(self):
        print(self)
        # make the surface black
        self.surfaceScreen.fill(self.colorBlack)
        
        # draw board border
        pygame.draw.rect(self.surfaceScreen, self.colorWhite, pygame.Rect(0, self.surfaceTop, self.surfaceWidth, self.surfaceHeight-self.surfaceTop), 5)
        # draw board half line
        half_line_x = self.surfaceWidth/2
        half_line_y = self.surfaceTop
        half_line_w = 5
        half_line_h = 20
        while half_line_y < self.surfaceHeight:
            pygame.draw.rect(self.surfaceScreen, self.colorWhite, pygame.Rect(half_line_x, half_line_y, half_line_w, half_line_h))
            half_line_y += (half_line_h*2)
            
        # display the surface
        self.display(self.surfaceScreen) 
    

    def getSurfaceWidth():
        return surfaceWidth

    def getSurfaceHeight():
        return surfaceHeight
    
