from displayOnMonitor import DisplayOnMonitor
import pygame
from pygame.locals import *

pygame.init()

class GuiField(DisplayOnMonitor):
    
    # size above the game to display score and gamename
    SURFACE_TOP = 100
    # border and halfline settings
    BORDER_WIDTH = 5
    BORDER_HEIGHT = 20
        
    def __init__(self):
        DisplayOnMonitor.__init__(self)
        self.halfLineX = ((int(self.SURFACE_WIDTH/2)) - (int(self.BORDER_WIDTH/2)))
            
    def drawHalfLine(self):
        # draw board half line
        halfLineY = self.SURFACE_TOP
        while halfLineY < self.SURFACE_HEIGHT:
            self.drawRect(self.halfLineX, halfLineY, self.BORDER_WIDTH, self.BORDER_HEIGHT)
            halfLineY += (self.BORDER_HEIGHT*2)
           
    def drawFieldAndScore(self, scoreP1, scoreP2):
        # make the surface black
        self.emptySurfaceScreen()
        
        # draw border gamefield (line above, right, left, under)
        self.drawRect(0, self.SURFACE_TOP, self.SURFACE_WIDTH, self.BORDER_WIDTH)
        self.drawRect(0, self.SURFACE_TOP, self.BORDER_WIDTH, (self.SURFACE_HEIGHT-self.SURFACE_TOP))
        self.drawRect((self.SURFACE_WIDTH-self.BORDER_WIDTH), self.SURFACE_TOP, self.BORDER_WIDTH, (self.SURFACE_HEIGHT-self.SURFACE_TOP))
        self.drawRect(0, (self.SURFACE_HEIGHT-self.BORDER_WIDTH), self.SURFACE_WIDTH, self.BORDER_WIDTH)
                         
        # draw board half line
        self.drawHalfLine()
        
        # draw score player1
        if (scoreP1==0):
            self.drawScore0(self.SURFACE_WIDTH/4)
        else:
            self.drawScore1(self.SURFACE_WIDTH/4)
        # draw score player2
        if (scoreP2==0):
            self.drawScore0(self.SURFACE_WIDTH*3/4)
        else:
            self.drawScore1(self.SURFACE_WIDTH*3/4)
        
    def drawScore0(self, posX):
        # draw a 0 via an empty rectangele
        self.drawRectOpen(posX, (self.SURFACE_TOP/6), (self.SURFACE_TOP*2/6), (self.SURFACE_TOP*4/6), (int(self.SURFACE_TOP/10)))
    
    def drawScore1(self, posX):
        # draw a 1 via a rectangele
        self.drawRect(posX, (self.SURFACE_TOP/6), (self.SURFACE_TOP/10), (self.SURFACE_TOP*4/6))

    def drawObject1(self, posX, posY, sizeX, sizeY):
        # draw players bad
        self.drawRectDebug1(posX, posY, sizeX, sizeY)
                
    def drawObject2(self, posX, posY, sizeX, sizeY):
        # draw ball
        self.drawRectDebug2(posX, posY, sizeX, sizeY)
                
    def removeObject(self, posX, posY, sizeX, sizeY):
        # remove object
        self.removeRect(posX, posY, sizeX, sizeY)
        # check if object is on half line
        if (((posX+sizeY) >= self.halfLineX) and (posX <= (self.halfLineX+self.BORDER_WIDTH))):
            # draw board half line
            self.drawHalfLine()        
            
    def getFieldWidth(self):
        # Width of the black part of the field
        fieldWidth = self.SURFACE_WIDTH -(self.BORDER_WIDTH*2)
        return fieldWidth

    def getFieldHeight(self):
        # Height of the black part of the field
        fieldHeight = self.SURFACE_HEIGHT -self.SURFACE_TOP -(self.BORDER_WIDTH*2)
        return fieldHeight
    
    def getBORDER_WIDTH(self):
        return self.BORDER_WIDTH
    
    def getFieldStartY(self):
        # field y-axis start
        fieldStartY = self.SURFACE_TOP + self.BORDER_WIDTH
        return fieldStartY
    
    def getFieldEndY(self):
        # field y-axis end
        fieldEndY = self.SURFACE_HEIGHT - self.BORDER_WIDTH
        return fieldEndY
    
    def getFieldStartX(self):
        # field x-axis start
        return self.BORDER_WIDTH
    
    def getFieldEndX(self):
        # field x-axis end
        fieldEndX = self.SURFACE_WIDTH - self.BORDER_WIDTH
        return fieldEndX

    
