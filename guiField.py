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
    colorDebug1 = (155, 255, 0)
    colorDebug2 = (0, 155, 255)
    
    # border
    border_width = 5
    border_height = 20
       
           
    def drawFieldAndScore(self, scoreP1, scoreP2):
        # make the surface black
        self.surfaceScreen.fill(self.colorBlack)
        
        # draw board border
        pygame.draw.rect(self.surfaceScreen, self.colorWhite, pygame.Rect(0, self.surfaceTop, self.surfaceWidth, self.surfaceHeight-self.surfaceTop), (self.border_width*2))
        # draw board half line
        half_line_x = self.surfaceWidth/2
        half_line_y = self.surfaceTop
        while half_line_y < self.surfaceHeight:
            pygame.draw.rect(self.surfaceScreen, self.colorWhite, pygame.Rect(half_line_x, half_line_y, self.border_width, self.border_height))
            half_line_y += (self.border_height*2)
        # draw score player1
        if (scoreP1==0):
            self.drawScore0(self.surfaceWidth/4)
        else:
            self.drawScore1(self.surfaceWidth/4)
        # draw score player2
        if (scoreP2==0):
            self.drawScore0(self.surfaceWidth*3/4)
        else:
            self.drawScore1(self.surfaceWidth*3/4)
    
    def drawScore0(self, posX):
        # draw a 0 via an empty rectangele
        pygame.draw.rect(self.surfaceScreen, self.colorWhite, pygame.Rect((posX), (self.surfaceTop/6), (self.surfaceTop*2/6), (self.surfaceTop*4/6)), (int(self.surfaceTop/10)))
    
    def drawScore1(self, posX):
        # draw a 1 via a rectangele
        pygame.draw.rect(self.surfaceScreen, self.colorWhite, pygame.Rect((posX), (self.surfaceTop/6), (self.surfaceTop/10), (self.surfaceTop*4/6)))

    def drawPlayer(self, posX, posY, sizeX, sizeY):
        # draw players bad
        pygame.draw.rect(self.surfaceScreen, self.colorDebug1, pygame.Rect((posX), (posY), sizeX, sizeY))
        
    def removePlayer(self, posX, posY, sizeX, sizeY):
        # remove players bad
        pygame.draw.rect(self.surfaceScreen, self.colorBlack, pygame.Rect((posX), (posY), sizeX, sizeY))
                
    def drawBall(self, posX, posY, size):
        # draw ball
        pygame.draw.rect(self.surfaceScreen, self.colorDebug2, pygame.Rect((posX), (posY), size, size))
        
    def removeBall(self, posX, posY, size):
        # remove ball
        pygame.draw.rect(self.surfaceScreen, self.colorBlack, pygame.Rect((posX), (posY), size, size))
        
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
    
    def getFieldStartY(self):
        # field y-axis start
        fieldStartY = self.surfaceTop + self.border_width
        return fieldStartY
    
    def getFieldEndY(self):
        # field y-axis end
        fieldEndY = self.surfaceHeight - self.border_width
        return fieldEndY
    
    def getFieldStartX(self):
        # field x-axis start
        fieldStartX = self.border_width
        return fieldStartX
    
    def getFieldEndX(self):
        # field x-axis end
        fieldEndX = self.surfaceWidth - self.border_width
        return fieldEndX

    
