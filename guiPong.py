#####################################################
#
#        guiPong.py functionality:
#
# * inheritance from displayOnMonitor.py
# * contains the size of the pong field
# * draws the field, score and bats
# * draws everything fast
#
#####################################################

from displayOnMonitor import DisplayOnMonitor
import pygame
from pygame.locals import *

pygame.init()

class GuiPong(DisplayOnMonitor):
    
    # size of gui of the game
    GUI_WIDTH = DisplayOnMonitor.MONITOR_WIDTH
    GUI_HEIGHT = DisplayOnMonitor.MONITOR_HEIGHT
    # size above the game to display score and gamename
    GUI_TOP = 100
    # border and halfline settings
    BORDER_WIDTH = 5
    BORDER_HEIGHT = 20
        
    def __init__(self):
        DisplayOnMonitor.__init__(self)
        self.halfLineX = ((int(self.GUI_WIDTH/2)) - (int(self.BORDER_WIDTH/2)))
            
    def drawHalfLine(self):
        # draw board half line
        halfLineY = self.GUI_TOP
        while halfLineY < self.GUI_HEIGHT:
            self.drawRectFast(self.halfLineX, halfLineY, self.BORDER_WIDTH, self.BORDER_HEIGHT)
            halfLineY += (self.BORDER_HEIGHT*2)
           
    def drawFieldAndScore(self, scoreP1, scoreP2):
        # make the screen black
        self.emptyScreenFast()
        
        # draw border gamefield (line above, right, left, under)
        self.drawRectFast(0, self.GUI_TOP, self.GUI_WIDTH, self.BORDER_WIDTH)
        self.drawRectFast(0, self.GUI_TOP, self.BORDER_WIDTH, (self.GUI_HEIGHT-self.GUI_TOP))
        self.drawRectFast((self.GUI_WIDTH-self.BORDER_WIDTH), self.GUI_TOP, self.BORDER_WIDTH, (self.GUI_HEIGHT-self.GUI_TOP))
        self.drawRectFast(0, (self.GUI_HEIGHT-self.BORDER_WIDTH), self.GUI_WIDTH, self.BORDER_WIDTH)
                         
        # draw board half line
        self.drawHalfLine()
        
        # draw score players
        self.drawScore(scoreP1, self.GUI_WIDTH*1/4)            
        self.drawScore(scoreP2, self.GUI_WIDTH*3/4)
    
    def drawScore(self, score, posX):
        if (score==0):
            self.drawScore0(posX)
        elif (score==1):
            self.drawScore1(posX)
        elif (score==2):
            self.drawScore2(posX)
        elif (score==3):
            self.drawScore3(posX)
        elif (score==4):
            self.drawScore4(posX)
        else:
            self.drawScore5(posX)
            
    def drawScore0(self, posX):
        # draw a 0 via multiple rectangeles
        # horizontal lines (up to down)
        self.drawRectFast(posX, (self.GUI_TOP*1/12), (self.GUI_TOP*2/6), (self.GUI_TOP*1/6))
        self.drawRectFast(posX, (self.GUI_TOP*9/12), (self.GUI_TOP*2/6), (self.GUI_TOP*1/6))
        # vertical lines (left to right)
        self.drawRectFast(posX, (self.GUI_TOP*1/12), (self.GUI_TOP*1/6), (self.GUI_TOP*10/12))
        self.drawRectFast((posX+self.GUI_TOP*2/6), (self.GUI_TOP*1/12), (self.GUI_TOP*1/6), (self.GUI_TOP*10/12))
    
    def drawScore1(self, posX):
        # draw a 1 via a rectangele
        self.drawRectFast(posX, (self.GUI_TOP*1/12), (self.GUI_TOP*1/6), (self.GUI_TOP*10/12))
        
    def drawScore2(self, posX):
        # draw a 2 via multiple rectangeles
        # horizontal lines (up to down)
        self.drawRectFast(posX, (self.GUI_TOP*1/12), (self.GUI_TOP*4/6), (self.GUI_TOP*1/6))
        self.drawRectFast(posX, (self.GUI_TOP*5/12), (self.GUI_TOP*4/6), (self.GUI_TOP*1/6))
        self.drawRectFast(posX, (self.GUI_TOP*9/12), (self.GUI_TOP*4/6), (self.GUI_TOP*1/6))
        # vertical lines (left to right)
        self.drawRectFast(posX, (self.GUI_TOP*5/12), (self.GUI_TOP*1/6), (self.GUI_TOP*5/12))
        self.drawRectFast((posX+self.GUI_TOP*3/6), (self.GUI_TOP*1/12), (self.GUI_TOP*1/6), (self.GUI_TOP*5/12))
    
    def drawScore3(self, posX):
        # draw a 3 via multiple rectangeles
        # horizontal lines (up to down)
        self.drawRectFast(posX, (self.GUI_TOP*1/12), (self.GUI_TOP*4/6), (self.GUI_TOP*1/6))
        self.drawRectFast(posX, (self.GUI_TOP*5/12), (self.GUI_TOP*4/6), (self.GUI_TOP*1/6))
        self.drawRectFast(posX, (self.GUI_TOP*9/12), (self.GUI_TOP*4/6), (self.GUI_TOP*1/6))
        # vertical lines (left to right)
        self.drawRectFast((posX+self.GUI_TOP*3/6), (self.GUI_TOP*1/12), (self.GUI_TOP*1/6), (self.GUI_TOP*10/12))
        
    def drawScore4(self, posX):
        # draw a 4 via multiple rectangeles
        # horizontal lines (up to down)
        self.drawRectFast(posX, (self.GUI_TOP*5/12), (self.GUI_TOP*4/6), (self.GUI_TOP*1/6))
        # vertical lines (left to right)        
        self.drawRectFast(posX, (self.GUI_TOP*1/12), (self.GUI_TOP*1/6), (self.GUI_TOP*5/12))
        self.drawRectFast((posX+self.GUI_TOP*3/6), (self.GUI_TOP*1/12), (self.GUI_TOP*1/6), (self.GUI_TOP*10/12))
        
    def drawScore5(self, posX):
        # draw a 5 via multiple rectangeles
        # horizontal lines (up to down)
        self.drawRectFast(posX, (self.GUI_TOP*1/12), (self.GUI_TOP*4/6), (self.GUI_TOP*1/6))
        self.drawRectFast(posX, (self.GUI_TOP*5/12), (self.GUI_TOP*4/6), (self.GUI_TOP*1/6))
        self.drawRectFast(posX, (self.GUI_TOP*9/12), (self.GUI_TOP*4/6), (self.GUI_TOP*1/6))
        # vertical lines (left to right)        
        self.drawRectFast(posX, (self.GUI_TOP*1/12), (self.GUI_TOP*1/6), (self.GUI_TOP*5/12))
        self.drawRectFast((posX+self.GUI_TOP*3/6), (self.GUI_TOP*5/12), (self.GUI_TOP*1/6), (self.GUI_TOP*5/12))
    
    def drawObject(self, posX, posY, sizeX, sizeY):
        # draw ball
        self.drawRectFast(posX, posY, sizeX, sizeY)
                
    def removeObject(self, posX, posY, sizeX, sizeY):
        # remove object
        self.removeRectFast(posX, posY, sizeX, sizeY)
        # check if object is on half line
        if (((posX+sizeY) >= self.halfLineX) and (posX <= (self.halfLineX+self.BORDER_WIDTH))):
            # draw board half line
            self.drawHalfLine()        
            
    def getFieldWidth(self):
        # Width of the black part of the field
        fieldWidth = self.GUI_WIDTH -(self.BORDER_WIDTH*2)
        return fieldWidth

    def getFieldHeight(self):
        # Height of the black part of the field
        fieldHeight = self.GUI_HEIGHT -self.GUI_TOP -(self.BORDER_WIDTH*2)
        return fieldHeight
    
    def getFieldStartY(self):
        # field y-axis start
        fieldStartY = self.GUI_TOP + self.BORDER_WIDTH
        return fieldStartY
    
    def getFieldEndY(self):
        # field y-axis end
        fieldEndY = self.GUI_HEIGHT - self.BORDER_WIDTH
        return fieldEndY
    
    def getFieldStartX(self):
        # field x-axis start
        return self.BORDER_WIDTH
    
    def getFieldEndX(self):
        # field x-axis end
        fieldEndX = self.GUI_WIDTH - self.BORDER_WIDTH
        return fieldEndX

    
