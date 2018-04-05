from inputHandler import InputHandler
from guiField import GuiField
from player import Player
from ball import Ball
import pygame
from pygame.locals import *
import sys
import time

# pygame init
pygame.init()
clock = pygame.time.Clock()

class PongGame():

#########################################################
###################   GAME SETTINGS   ###################


    # Set player bad size
    playerSizeX = 15
    playerSizeY = 80

    # Set ball size
    ballSize = 15
    ballSpeed = 30


###################  END OF SETTINGS  ###################
#########################################################

    
    # play pong loop
    PLAY_PONG=True
    
    # game states
    GAME_STATE = None
    STATE_PLAY_NORMAL = 0
    STATE_PLAYER1_SCORED = 1
    STATE_PLAYER2_SCORED = 2
    
    # all directions
    DIR_UP = -1
    DIR_DOWN = 1
    DIR_LEFT = -1
    DIR_RIGHT = 1 
    DIR_NORMAL = 0
    DIR_BALL_MISSED = 9
    
    # debug variables
    DEBUG_MAIN_LOOP_CNT = 0
    
    def __init__(self):
        # create objects
        self.input = InputHandler()
        self.guiField = GuiField()
        self.player1 = Player(self.guiField.getFieldStartX(), self.playerSizeX, self.playerSizeY, self.guiField.getFieldStartY(), (self.guiField.getFieldEndY()-self.playerSizeY))
        self.player2 = Player((self.guiField.getFieldEndX()-self.playerSizeX), self.playerSizeX, self.playerSizeY, self.guiField.getFieldStartY(), (self.guiField.getFieldEndY()-self.playerSizeY))
        self.ball = Ball(self.ballSize, self.ballSpeed)

        # creat variables that need info from object(s)
        self.player1WallX = self.guiField.getFieldStartX() + self.playerSizeX
        self.player2WallX = self.guiField.getFieldEndX() - self.playerSizeX
        self.fieldHeigtMiddle = (((int)(self.guiField.getFieldHeight()/2)))
        self.fieldWidthMiddle = (((int)(self.guiField.getFieldWidth()/2)))  

    def resetGame(self):
        # Reset the ball
        self.ball.reset(self.fieldWidthMiddle, self.fieldHeigtMiddle-(int(self.ballSize/2)), self.DIR_RIGHT, self.DIR_NORMAL)
        # Reset players
        self.player1.reset(self.fieldHeigtMiddle-(int(self.playerSizeY/2)))
        self.player2.reset(self.fieldHeigtMiddle-(int(self.playerSizeY/2)))
        # Draw the field and score
        self.guiField.drawFieldAndScore(self.player1.getPoints(), self.player2.getPoints())
        # Reset game state
        self.GAME_STATE = self.STATE_PLAY_NORMAL

    def ballHitPlayerDirection(self, playerY, ballY):
        dir = self.DIR_NORMAL
        # check if ball is higher than palyer
        if ((ballY+self.ballSize) < playerY):
            dir = self.DIR_BALL_MISSED
        # check if the middle of the ball hit upper part of the palyer
        elif ((ballY+self.ballSize) <= (playerY+(self.playerSizeY/3))):
            dir = self.DIR_UP
        # check if ball is lower than player
        elif (ballY > (playerY+self.playerSizeY)):
            dir = self.DIR_BALL_MISSED
        # check if the middle of the ball hit lower part of the palyer
        elif (ballY >= (playerY+(self.playerSizeY*2/3))):
            dir = self.DIR_DOWN
        # else dir is normal
        # return the direction of the ball
        return dir    

    def updateGame(self):
        for loopCnt in range(0, self.ball.getSpeed()):
            #print("for update")
            ballDirX = self.ball.getDirX()
            dirY_OrBallMissed = self.ball.getDirY()
            
            #Check ball hits wall player1
            if((self.ball.getPosX()+self.ball.getDirX()) == self.player1WallX):
                ballDirX = self.DIR_RIGHT
                dirY_OrBallMissed = self.ballHitPlayerDirection(self.player1.getPosY(), self.ball.getPosY())
            #Check ball hits wall player2
            elif((self.ball.getPosX()+self.ball.getDirX()+self.ballSize) == self.player2WallX):
                ballDirX = self.DIR_LEFT
                dirY_OrBallMissed = self.ballHitPlayerDirection(self.player2.getPosY(), self.ball.getPosY())
            #Check ball hits top
            elif((self.ball.getPosY()+self.ball.getDirY()) == self.guiField.getFieldStartY()):
                dirY_OrBallMissed = self.DIR_DOWN
            #Check ball hits bottom
            elif((self.ball.getPosY()+self.ball.getDirY()+self.ballSize) == self.guiField.getFieldEndY()):
                dirY_OrBallMissed = self.DIR_UP
            
            if(dirY_OrBallMissed != self.DIR_BALL_MISSED):
                # update ball dir and position
                self.ball.updateDir(ballDirX, dirY_OrBallMissed)
                self.ball.updatePos()
            else:
                #check who won via ballDirX left or right
                if (ballDirX == self.DIR_RIGHT):
                    self.GAME_STATE = self.STATE_PLAYER2_SCORED
                else:
                    self.GAME_STATE = self.STATE_PLAYER1_SCORED
                # end the loop
                loopCnt = self.ballSpeed
                    
    def handleConsoleinput(self):
        data = self.input.getConsole()
        if (data == 1):
            self.playGame = False
        
    def handleControllerInput(self):
        pixelsToMove = 20
        # update player1 pos
        data = self.input.getController1()
        if (data != 0):
            print("data1 " + str(data))
        self.player1.move((data*pixelsToMove));
        # update player2 pos
        data = self.input.getController2()
        if (data != 0):
            print("data2 " + str(data))
        self.player2.move((data*pixelsToMove));
        
    def handleInput(self):
        pixelsToMove = 20
        for event in pygame.event.get():
            # Check if 'esc' or close button is pressed
            if (event.type == QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE)):
                self.PLAY_PONG = False
            # Check if 'up' button is pressed
            elif (event.type == pygame.KEYDOWN and event.key == pygame.K_UP):
                # move player 1 100 pixels up
                self.player2.move(-pixelsToMove);
            # Check if 'down' button is pressed
            elif (event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN):
                # move player 1 100 pixels down
                self.player2.move(pixelsToMove);
           # Check if 'w' button is pressed
            elif (event.type == pygame.KEYDOWN and event.key == pygame.K_w):
                # move player 2 100 pixels up
                self.player1.move(-pixelsToMove);
            # Check if 's' button is pressed
            elif (event.type == pygame.KEYDOWN and event.key == pygame.K_s):
                # move player 2 100 pixels down
                self.player1.move(pixelsToMove); 

    def displayGame(self):
        # draw players and ball
        self.guiField.drawObject1(self.player1.getPosX(), self.player1.getPosY(), self.playerSizeX, self.playerSizeY)
        self.guiField.drawObject1(self.player2.getPosX(), self.player2.getPosY(), self.playerSizeX, self.playerSizeY)
        self.guiField.drawObject2(self.ball.getPosX(), self.ball.getPosY(), self.ballSize, self.ballSize)
        # display drawing
        self.guiField.display()
        # clear field
        self.guiField.removeObject(self.player1.getPosX(), self.player1.getPosY(), self.playerSizeX, self.playerSizeY)
        self.guiField.removeObject(self.player2.getPosX(), self.player2.getPosY(), self.playerSizeX, self.playerSizeY)
        self.guiField.removeObject(self.ball.getPosX(), self.ball.getPosY(), self.ballSize, self.ballSize)

    def playPong(self):
        # reset the game befor start
        self.resetGame()
        # play pong 
        while self.PLAY_PONG:
            # debug timer info
            #print(str(DEBUG_MAIN_LOOP_CNT) + " tick0 " + str(pygame.time.get_ticks()))
            #DEBUG_MAIN_LOOP_CNT = DEBUG_MAIN_LOOP_CNT+1
                        
            #self.handleControllerInput()  Can only be implemented when controllers are done
            #self.handleConsoleinput()     Can only be implemented when console board is done
            self.handleInput()
            
            if (self.GAME_STATE == self.STATE_PLAY_NORMAL):
                self.displayGame()
                self.updateGame()
            elif (self.GAME_STATE == self.STATE_PLAYER1_SCORED):
                self.player1.addPoint()
                self.resetGame()
            elif (self.GAME_STATE == self.STATE_PLAYER2_SCORED):
                self.player2.addPoint()
                self.resetGame()                          
            
            # debug timer info
            #print(str(DEBUG_MAIN_LOOP_CNT) + " tick1 " + str(pygame.time.get_ticks()-1))
            clock.tick(30)
            
        # end of programm
        #del self.guiField
        #del self.player1
        #del self.player2
        #del self.ball
        #pygame.quit
            


