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

#############################
######  GAME SETTINGS  ######
#############################

    # Set player bad size
    playerSizeX = 15
    playerSizeY = 80

    # Set ball size
    ballSize = 15
    ballSpeed = 15

###############################
######  END OF SETTINGS  ######
###############################

    # make objects
    input = InputHandler()
    guiField = GuiField()
    player1 = Player(guiField.getFieldStartX(), playerSizeX, playerSizeY, guiField.getFieldStartY(), (guiField.getFieldEndY()-playerSizeY))
    player2 = Player((guiField.getFieldEndX()-playerSizeX), playerSizeX, playerSizeY, guiField.getFieldStartY(), (guiField.getFieldEndY()-playerSizeY))
    ball = Ball(ballSize, ballSpeed)

    # variables that need info from object(s)
    player1WallX = guiField.getFieldStartX() + playerSizeX
    player2WallX = guiField.getFieldEndX() - playerSizeX
    fieldHeigtMiddle = (guiField.getFieldHeight()/2)
    fieldWidthMiddle = (guiField.getFieldWidth()/2)
    # variables
    playPong=True
    gameState = None
    statePlayNormal = 0
    statePlayer1Scored = 1
    statePlayer2Scored = 2
    dirUp = -1
    dirDown = 1
    dirLeft = -1
    dirRight = 1 
    dirNormal = 0
    dirPlayerMissedBall = 9
    # debug variables
    debugMainLoopCnt = 0

    def resetGame(self):
        # Reset the ball
        self.ball.reset(self.fieldWidthMiddle, self.fieldHeigtMiddle-(int(self.ballSize/2)), self.dirRight, self.dirNormal)
        # Reset players
        self.player1.reset(self.fieldHeigtMiddle-(int(self.playerSizeY/2)))
        self.player2.reset(self.fieldHeigtMiddle-(int(self.playerSizeY/2)))
        # Draw the field and score
        self.guiField.drawFieldAndScore(self.player1.getPoints(), self.player2.getPoints())
        # Reset game state
        self.gameState = self.statePlayNormal

    def ballHitPlayerDirection(self, playerY, ballY):
        dir = self.dirNormal
        # check if ball is higher than palyer
        if ((ballY+self.ballSize) < playerY):
            dir = self.dirPlayerMissedBall
        # check if the middle of the ball hit upper part of the palyer
        elif ((ballY+self.ballSize) <= (playerY+(self.playerSizeY/3))):
            dir = self.dirUp
        # check if ball is lower than player
        elif (ballY > (playerY+self.playerSizeY)):
            dir = self.dirPlayerMissedBall
        # check if the middle of the ball hit lower part of the palyer
        elif (ballY >= (playerY+(self.playerSizeY*2/3))):
            dir = self.dirDown
        # else dir is normal
        # return the direction of the ball
        return dir    

    def updateGame(self):
        for loopCnt in range(0, self.ball.getSpeed()):
            #print("for update")
            ballDirX = self.ball.getDirX()
            ballDirY_OrGameOver = self.ball.getDirY()
            
            #Check ball hits wall player1
            if((self.ball.getPosX()+self.ball.getDirX()) == self.player1WallX):
                ballDirX = self.dirRight
                ballDirY_OrGameOver = self.ballHitPlayerDirection(self.player1.getPosY(), self.ball.getPosY())
            #Check ball hits wall player2
            elif((self.ball.getPosX()+self.ball.getDirX()+self.ballSize) == self.player2WallX):
                ballDirX = self.dirLeft
                ballDirY_OrGameOver = self.ballHitPlayerDirection(self.player2.getPosY(), self.ball.getPosY())
            #Check ball hits top
            elif((self.ball.getPosY()+self.ball.getDirY()) == self.guiField.getFieldStartY()):
                ballDirY_OrGameOver = self.dirDown
            #Check ball hits bottom
            elif((self.ball.getPosY()+self.ball.getDirY()+self.ballSize) == self.guiField.getFieldEndY()):
                ballDirY_OrGameOver = self.dirUp
            
            if(ballDirY_OrGameOver != self.dirPlayerMissedBall):
                # update ball dir and position
                self.ball.updateDir(ballDirX, ballDirY_OrGameOver)
                self.ball.updatePos()
            else:
                #check who won via ballDirX left or right
                if (ballDirX == self.dirRight):
                    self.gameState = self.statePlayer2Scored
                else:
                    self.gameState = self.statePlayer1Scored
                # end the loop
                loopCnt = self.ballSpeed
                    
    def handleConsoleinput(self):
        data = self.input.getConsole()
        if (data == 1):
            self.playPong = False
        
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
                self.playPong = False
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
        self.guiField.drawPlayer(self.player1.getPosX(), self.player1.getPosY(), self.playerSizeX, self.playerSizeY)
        self.guiField.drawPlayer(self.player2.getPosX(), self.player2.getPosY(), self.playerSizeX, self.playerSizeY)
        self.guiField.drawBall(self.ball.getPosX(), self.ball.getPosY(), self.ballSize)
        # display drawing
        self.guiField.fieldDisplay()
        # clear field
        self.guiField.removePlayer(self.player1.getPosX(), self.player1.getPosY(), self.playerSizeX, self.playerSizeY)
        self.guiField.removePlayer(self.player2.getPosX(), self.player2.getPosY(), self.playerSizeX, self.playerSizeY)
        self.guiField.removeBall(self.ball.getPosX(), self.ball.getPosY(), self.ballSize)

    def playPong(self):
        
        self.resetGame()
        
        while self.playPong:
            # debug timer info
            #print(str(debugMainLoopCnt) + " tick0 " + str(pygame.time.get_ticks()))
            #debugMainLoopCnt = debugMainLoopCnt+1
                        
            #self.handleControllerInput()  Can only be implemented when controllers are done
            #self.handleConsoleinput()     Can only be implemented when console board is done
            self.handleInput()
            
            if (self.gameState == self.statePlayNormal):
                self.displayGame()
                self.updateGame()
            elif (self.gameState == self.statePlayer1Scored):
                self.player1.addPoint()
                self.resetGame()
            elif (self.gameState == self.statePlayer2Scored):
                self.player2.addPoint()
                self.resetGame()                          
            
            # debug timer info
            #print(str(debugMainLoopCnt) + " tick1 " + str(pygame.time.get_ticks()-1))
            clock.tick(30)
            
        # end of programm
        #del self.guiField
        #del self.player1
        #del self.player2
        #del self.ball
        #pygame.quit
            


