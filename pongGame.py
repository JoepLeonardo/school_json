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

######################################################
###################   GAME SETTINGS   ###################

    # Set player bad size
    PLAYER_SIZE_X = 15
    PLAYER_SIZE_Y = 80

    # Set ball size
    BALL_SIZE = 15
    BALL_SPEED = 30
    
    # Time before the game starts
    DELAY_BEFORE_START = 500
    DELAY_PLAYER_SCORED = 500

###################  END OF SETTINGS  ###################
#########################################################
    
    # play pong loop
    PLAY_PONG = True
    
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
        self.player1 = Player(self.guiField.getFieldStartX(), self.PLAYER_SIZE_X, self.PLAYER_SIZE_Y, self.guiField.getFieldStartY(), (self.guiField.getFieldEndY()-self.PLAYER_SIZE_Y))
        self.player2 = Player((self.guiField.getFieldEndX()-self.PLAYER_SIZE_X), self.PLAYER_SIZE_X, self.PLAYER_SIZE_Y, self.guiField.getFieldStartY(), (self.guiField.getFieldEndY()-self.PLAYER_SIZE_Y))
        self.ball = Ball(self.BALL_SIZE, self.BALL_SPEED)

        # creat variables that need info from object(s)
        self.player1WallX = self.guiField.getFieldStartX() + self.PLAYER_SIZE_X
        self.player2WallX = self.guiField.getFieldEndX() - self.PLAYER_SIZE_X
        self.fieldHeigtMiddle = (((int)(self.guiField.getFieldHeight()/2)))
        self.fieldWidthMiddle = (((int)(self.guiField.getFieldWidth()/2)))
        
        # reset the game so all variables are declared right
        self.resetGame()

    def resetGame(self):
        # Reset the ball
        self.ball.reset(self.fieldWidthMiddle, self.fieldHeigtMiddle-(int(self.BALL_SIZE/2)), self.DIR_RIGHT, self.DIR_NORMAL)
        # Reset players
        self.player1.reset(self.fieldHeigtMiddle-(int(self.PLAYER_SIZE_Y/2)))
        self.player2.reset(self.fieldHeigtMiddle-(int(self.PLAYER_SIZE_Y/2)))
        # Draw the field and score
        self.guiField.drawFieldAndScore(self.player1.getPoints(), self.player2.getPoints())
        # Game state to noraml
        self.GAME_STATE = self.STATE_PLAY_NORMAL
        # Display the current game state
        self.displayGame()
        # Wait 0.5sec before the game starts
        pygame.time.delay(self.DELAY_BEFORE_START)


    def ballHitPlayerDir(self, playerY, ballY):
        dir = self.DIR_NORMAL
        # check if ball is higher than palyer
        if ((ballY+self.BALL_SIZE) < playerY):
            dir = self.DIR_BALL_MISSED
        # check if the middle of the ball hit upper part of the palyer
        elif ((ballY+self.BALL_SIZE) <= (playerY+(self.PLAYER_SIZE_Y/3))):
            dir = self.DIR_UP
        # check if ball is lower than player
        elif (ballY > (playerY+self.PLAYER_SIZE_Y)):
            dir = self.DIR_BALL_MISSED
        # check if the middle of the ball hit lower part of the palyer
        elif (ballY >= (playerY+(self.PLAYER_SIZE_Y*2/3))):
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
                dirY_OrBallMissed = self.ballHitPlayerDir(self.player1.getPosY(), self.ball.getPosY())
            #Check ball hits wall player2
            elif((self.ball.getPosX()+self.ball.getDirX()+self.BALL_SIZE) == self.player2WallX):
                ballDirX = self.DIR_LEFT
                dirY_OrBallMissed = self.ballHitPlayerDir(self.player2.getPosY(), self.ball.getPosY())
            #Check ball hits top
            elif((self.ball.getPosY()+self.ball.getDirY()) == self.guiField.getFieldStartY()):
                dirY_OrBallMissed = self.DIR_DOWN
            #Check ball hits bottom
            elif((self.ball.getPosY()+self.ball.getDirY()+self.BALL_SIZE) == self.guiField.getFieldEndY()):
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
                loopCnt = self.BALL_SPEED
                    
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
        self.guiField.drawObject1(self.player1.getPosX(), self.player1.getPosY(), self.PLAYER_SIZE_X, self.PLAYER_SIZE_Y)
        self.guiField.drawObject1(self.player2.getPosX(), self.player2.getPosY(), self.PLAYER_SIZE_X, self.PLAYER_SIZE_Y)
        self.guiField.drawObject2(self.ball.getPosX(), self.ball.getPosY(), self.BALL_SIZE, self.BALL_SIZE)
        # display drawing
        self.guiField.display()
        # clear field
        self.guiField.removeObject(self.player1.getPosX(), self.player1.getPosY(), self.PLAYER_SIZE_X, self.PLAYER_SIZE_Y)
        self.guiField.removeObject(self.player2.getPosX(), self.player2.getPosY(), self.PLAYER_SIZE_X, self.PLAYER_SIZE_Y)
        self.guiField.removeObject(self.ball.getPosX(), self.ball.getPosY(), self.BALL_SIZE, self.BALL_SIZE)

    def playPong(self):
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
            


