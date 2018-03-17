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
    colorDebug = (155, 255, 0)
    
    # border
    border_width = 5
    border_height = 20
       
           
    def fieldClear(self):
        # make the surface black
        self.surfaceScreen.fill(self.colorBlack)
        
        # draw board border
        pygame.draw.rect(self.surfaceScreen, self.colorWhite, pygame.Rect(0, self.surfaceTop, self.surfaceWidth, self.surfaceHeight-self.surfaceTop), self.border_width)
        # draw board half line
        half_line_x = self.surfaceWidth/2
        half_line_y = self.surfaceTop
        while half_line_y < self.surfaceHeight:
            pygame.draw.rect(self.surfaceScreen, self.colorWhite, pygame.Rect(half_line_x, half_line_y, self.border_width, self.border_height))
            half_line_y += (self.border_height*2)
                       
    def fieldAddPlayer(self, posX, posY, sizeX, sizeY, points):
        # draw players bad
        pygame.draw.rect(self.surfaceScreen, self.colorWhite, pygame.Rect((posX), (posY), sizeX, sizeY))
        # TODO: draw players score
        
    def fieldDisplay(self):
        # display the surface
        self.display(self.surfaceScreen)
    
    def getFieldWidth(self):
        # Width of the black part of the field
        fieldWidth = self.surfaceWidth -(self.border_width*2)
        return fieldWidth

    def getFieldHeight(self):
        # Height of the black part of the field
        fieldHeight = self.surfaceHeight -self.surfaceTop -(self.border_width*2)
        return fieldHeight
    
    def getBorderWidth(self):
        return self.border_width

    