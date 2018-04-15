from displayOnMonitor import DisplayOnMonitor
from inputHandler import InputHandler
import pygame
from pygame.locals import *
import time

pygame.init()

class GuiSettings(DisplayOnMonitor):
    
    # display settings
    HEIGHT_ITEM = (DisplayOnMonitor.SURFACE_HEIGHT*1/7)
    ITEM_SIZE = 70
    ITEM_VALUE_MIN = 1
    ITEM_VALUE_MAX = 99    
    ITEM_DEFAULT_FACTOR = 1
    ITEM_LARGE_FACTOR = 5
    # game variables
    ITEM_BALL_SPEED_NAME = 'Ball Speed'
    ITEM_BALL_SPEED_DEFAULT = 15
    ITEM_BALL_SPEED_HEIGHT = (HEIGHT_ITEM*1)
    ITEM_BALL_SIZE_NAME = 'Ball Size'
    ITEM_BALL_SIZE_DEFAULT = 15
    ITEM_BALL_SIZE_HEIGHT = (HEIGHT_ITEM*2)
    ITEM_PLAYER_WIDTH_NAME = 'Player Width'
    ITEM_PLAYER_WIDTH_DEFAULT = 15
    ITEM_PLAYER_WIDTH_HEIGHT = (HEIGHT_ITEM*3)
    ITEM_PLAYER_HEIGHT_NAME = 'Player Height'
    ITEM_PLAYER_HEIGHT_DEFAULT = 60
    ITEM_PLAYER_HEIGHT_HEIGHT = (HEIGHT_ITEM*4)
    ITEM_RESET_NAME = 'Reset'
    ITEM_RESET_HEIGHT = (HEIGHT_ITEM*5)   
    ITEM_EXIT_NAME = 'Exit'
    ITEM_EXIT_HEIGHT = (HEIGHT_ITEM*6)
    # Menu state
    GAME_STATE = None
    STATE_BALL_SPEED = 20
    STATE_BALL_SIZE = 21
    STATE_PLAYER_WIDTH = 22
    STATE_PLAYER_HEIGHT = 23
    STATE_RESET = 24
    STATE_EXIT = 25
    STATE_MIN = STATE_BALL_SPEED
    STATE_MAX = STATE_EXIT
    # Delay (ms)
    DELAY_BETWEEN_INPUT = 300

    def __init__(self):
        # create object(s)
        self.input = InputHandler()
        # settings
        self.continueMenu = True
        self.ballSpeed = self.ITEM_BALL_SPEED_DEFAULT
        self.ballSize = self.ITEM_BALL_SIZE_DEFAULT
        self.playerWidth = self.ITEM_PLAYER_WIDTH_DEFAULT
        self.playerHeight = self.ITEM_PLAYER_HEIGHT_DEFAULT
            
    #def __del__(self):
        #print("exit guiSettings")
        
    def getBallSpeed(self):
        return self.ballSpeed
    
    def getBallSize(self):
        return self.ballSize
    
    def getPlayerWidth(self):
        return self.playerWidth
    
    def getPlayerHeight(self):
        return self.playerHeight
        
    def reset(self):
        DisplayOnMonitor.__init__(self)
        self.continueMenu = True
        self.GAME_STATE = self.STATE_BALL_SPEED
        
    def drawMenu(self):
        # clear the current screen
        self.emptySurfaceScreen()
        # draw items
        self.drawTextMiddle(self.ITEM_BALL_SPEED_NAME, self.ITEM_SIZE, self.ITEM_BALL_SPEED_HEIGHT, (self.GAME_STATE == self.STATE_BALL_SPEED))
        self.drawTextMiddle(self.ITEM_BALL_SIZE_NAME, self.ITEM_SIZE, self.ITEM_BALL_SIZE_HEIGHT, (self.GAME_STATE == self.STATE_BALL_SIZE))
        self.drawTextMiddle(self.ITEM_PLAYER_WIDTH_NAME, self.ITEM_SIZE, self.ITEM_PLAYER_WIDTH_HEIGHT, (self.GAME_STATE == self.STATE_PLAYER_WIDTH))
        self.drawTextMiddle(self.ITEM_PLAYER_HEIGHT_NAME, self.ITEM_SIZE, self.ITEM_PLAYER_HEIGHT_HEIGHT, (self.GAME_STATE == self.STATE_PLAYER_HEIGHT))
        self.drawTextMiddle(self.ITEM_RESET_NAME, self.ITEM_SIZE, self.ITEM_RESET_HEIGHT, (self.GAME_STATE == self.STATE_RESET))
        self.drawTextMiddle(self.ITEM_EXIT_NAME, self.ITEM_SIZE, self.ITEM_EXIT_HEIGHT, (self.GAME_STATE == self.STATE_EXIT))
        
    def drawMenuAndDisplay(self):
        # draw the menu
        self.drawMenu()
        # show the drawings
        self.display()
    
    def drawItemOverMenu(self, name, value, height):
        self.drawMenu()
        self.drawTextMiddle((name + ": < " + str(value) + " >"), self.ITEM_SIZE, height, False)
        # show the drawings
        self.display()
        
    def handleItem(self, name, value, height, factor):
        newValue = value
        continueItem = True
        # draw the submenu
        self.drawItemOverMenu(name, newValue, height)
        
        while (continueItem):            
            # delay between button presses
            pygame.time.delay(self.DELAY_BETWEEN_INPUT)
            # get input form console
            data = self.input.getConsole()
            # PRESSED NEXT
            if (data == self.input.DATA_NEXT):
                # inccrease value if possible
                if ((newValue+factor) <= (self.ITEM_VALUE_MAX*factor)):
                    newValue = newValue + factor
                    # draw the submenu
                    self.drawItemOverMenu(name, newValue, height)
            # PRESSED PREV
            elif (data == self.input.DATA_PREV):
                # decrease value if possible
                if ((newValue-factor) >= self.ITEM_VALUE_MIN):
                    newValue = newValue - factor
                    # draw the submenu
                    self.drawItemOverMenu(name, newValue, height)
            # PRESSED SELECT
            elif (data == self.input.DATA_SELECT):
                # quit this submenu
                continueItem = False
        # end of while
        self.drawMenuAndDisplay()
        return newValue
            
        
    def handleMenu(self):
        # reset
        self.reset()
        # draw the menu
        self.drawMenuAndDisplay()
        while (self.continueMenu):
            # get input form console
            data = self.input.getConsole()
            
            # PRESSED POWER OFF
            if (data == self.input.DATA_POWER_OFF):
                self.continueMenu = False
            # PRESSED NEXT
            elif (data == self.input.DATA_NEXT):
                if (self.GAME_STATE < self.STATE_MAX):
                    self.GAME_STATE = self.GAME_STATE + 1
                else:
                    self.GAME_STATE= self.STATE_MIN
                self.drawMenuAndDisplay()
            # PRESSED PREV
            elif (data == self.input.DATA_PREV):
                if (self.GAME_STATE > self.STATE_MIN):
                    self.GAME_STATE = self.GAME_STATE - 1
                else:
                    self.GAME_STATE= self.STATE_MAX
                self.drawMenuAndDisplay()
            # PRESSED SELECT
            elif (data == self.input.DATA_SELECT):
                # Check if ball speed gets update
                if (self.GAME_STATE == self.STATE_BALL_SPEED):
                    self.ballSpeed = self.handleItem(self.ITEM_BALL_SPEED_NAME, self.ballSpeed, self.ITEM_BALL_SPEED_HEIGHT, self.ITEM_DEFAULT_FACTOR)
                # Check if ball size  gets update
                elif (self.GAME_STATE == self.STATE_BALL_SIZE):
                    self.ballSize = self.handleItem(self.ITEM_BALL_SIZE_NAME, self.ballSize, self.ITEM_BALL_SIZE_HEIGHT, self.ITEM_DEFAULT_FACTOR)
                # Check if player witdth gets update
                elif (self.GAME_STATE == self.STATE_PLAYER_WIDTH):
                    self.playerWidth = self.handleItem(self.ITEM_PLAYER_WIDTH_NAME, self.playerWidth, self.ITEM_PLAYER_WIDTH_HEIGHT, self.ITEM_DEFAULT_FACTOR)
                # Check if player height gets update
                elif (self.GAME_STATE == self.STATE_PLAYER_HEIGHT):
                    self.playerHeight= self.handleItem(self.ITEM_PLAYER_HEIGHT_NAME, self.playerHeight, self.ITEM_PLAYER_HEIGHT_HEIGHT, self.ITEM_LARGE_FACTOR)
                # Check to reset settings
                elif (self.GAME_STATE == self.STATE_RESET):
                    self.ballSpeed = self.ITEM_BALL_SPEED_DEFAULT
                    self.ballSize = self.ITEM_BALL_SIZE_DEFAULT
                    self.playerWidth = self.ITEM_PLAYER_WIDTH_DEFAULT
                    self.playerHeight = self.ITEM_PLAYER_HEIGHT_DEFAULT                    
                # Check to exit settings menu
                elif (self.GAME_STATE == self.STATE_EXIT):
                    # exit settings menu
                    self.continueMenu = False
                else:
                    print("unknown settings state, exit")
                    self.continueMenu = False
                
            pygame.time.delay(self.DELAY_BETWEEN_INPUT)    