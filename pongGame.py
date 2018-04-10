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
    PLAYER_SIZE_X = 15
    PLAYER_SIZE_Y = 70

    # Set ball size
    BALL_SIZE = PLAYER_SIZE_X
    BALL_SPEED_NIV1 = 15
    BALL_SPEED_NIV2 = 30
    BALL_SPEED_NIV3 = 45
    
    # Ball speed increasement after hit with player
    BALL_SPEED_INCREASE = 1
    
    # Time before the game starts (ms)
    DELAY_BEFORE_START = 500
    DELAY_PLAYER_SCORED = 1000
    DELAY_PLAYER_WON = 3000
    
    # Spcae between wall and player
    SPACE_WALL_PLAYER = 50

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
    # maximum points a player can score
    POINTS_MAX = 2
    
    # debug variables
    DEBUG_MAIN_LOOP_CNT = 0
    
    def __init__(self, niveau):
        pygame.init()
        # create objects
        self.input = InputHandler()
        self.guiField = GuiField()
        self.player1 = Player((self.guiField.getFieldStartX()+self.SPACE_WALL_PLAYER), self.PLAYER_SIZE_X, self.PLAYER_SIZE_Y, self.guiField.getFieldStartY(), (self.guiField.getFieldEndY()-self.PLAYER_SIZE_Y))
        self.player2 = Player((self.guiField.getFieldEndX()-self.PLAYER_SIZE_X-self.SPACE_WALL_PLAYER), self.PLAYER_SIZE_X, self.PLAYER_SIZE_Y, self.guiField.getFieldStartY(), (self.guiField.getFieldEndY()-self.PLAYER_SIZE_Y))
        ballSpeed = self.BALL_SPEED_NIV1
        if (niveau == 2):
            ballSpeed = self.BALL_SPEED_NIV2
        if (niveau == 3):
            ballSpeed = self.BALL_SPEED_NIV3
        self.ball = Ball(self.BALL_SIZE, ballSpeed)

        # creat variables that need info from object(s)
        self.player1WallX = self.player1.getPosX() + self.PLAYER_SIZE_X
        self.player2WallX = self.player2.getPosX()
        self.fieldHeigtMiddle = (((int)(self.guiField.getFieldHeight()/2)))
        self.fieldWidthMiddle = (((int)(self.guiField.getFieldWidth()/2)))
        
        # reset the game so all variables are declared right
        self.resetGame()

    def resetGame(self):
        # Reset the ball
        self.ball.reset(self.fieldWidthMiddle+750, self.fieldHeigtMiddle-(int(self.BALL_SIZE/2)), self.DIR_RIGHT, self.DIR_NORMAL)
        # Reset players
        self.player1.reset(self.fieldHeigtMiddle-(int(self.PLAYER_SIZE_Y/2)))
        self.player2.reset(self.fieldHeigtMiddle-(int(self.PLAYER_SIZE_Y/2)))
        # Draw the field and score
        self.guiField.drawFieldAndScore(self.player1.getPoints(), self.player2.getPoints())
        # Game state to noraml
        self.GAME_STATE = self.STATE_PLAY_NORMAL
        # Display the current game state
        self.displayGame()
        # Wait before the game starts
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
            ballDirX = self.ball.getDirX()
            dirY_OrBallMissed = self.ball.getDirY()
            
            #Check ball hits wall player1
            if((self.ball.getPosX()+self.ball.getDirX()) == self.player1WallX):
                ballDirX = self.DIR_RIGHT
                dirY_OrBallMissed = self.ballHitPlayerDir(self.player1.getPosY(), self.ball.getPosY())
                self.ball.increaseSpeed(self.BALL_SPEED_INCREASE)
            #Check ball hits wall player2
            elif((self.ball.getPosX()+self.ball.getDirX()+self.BALL_SIZE) == self.player2WallX):
                ballDirX = self.DIR_LEFT
                dirY_OrBallMissed = self.ballHitPlayerDir(self.player2.getPosY(), self.ball.getPosY())
                self.ball.increaseSpeed(self.BALL_SPEED_INCREASE)
            #Check ball hits top
            elif((self.ball.getPosY()+self.ball.getDirY()) == self.guiField.getFieldStartY()):
                dirY_OrBallMissed = self.DIR_DOWN
            #Check ball hits bottom
            elif((self.ball.getPosY()+self.ball.getDirY()+self.BALL_SIZE) == self.guiField.getFieldEndY()):
                dirY_OrBallMissed = self.DIR_UP
            
            #Check if player not missed the ball
            if(dirY_OrBallMissed != self.DIR_BALL_MISSED):
                # update ball dir
                self.ball.updateDir(ballDirX, dirY_OrBallMissed)
            else:
                #check who won via ballDirX left or right
                if (ballDirX == self.DIR_RIGHT):
                    self.GAME_STATE = self.STATE_PLAYER2_SCORED
                else:
                    self.GAME_STATE = self.STATE_PLAYER1_SCORED
                # end the loop
                loopCnt = self.ball.getSpeed()
             # update ball position
            self.ball.updatePos()
                    
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
        self.guiField.drawObject(self.player1.getPosX(), self.player1.getPosY(), self.PLAYER_SIZE_X, self.PLAYER_SIZE_Y)
        self.guiField.drawObject(self.player2.getPosX(), self.player2.getPosY(), self.PLAYER_SIZE_X, self.PLAYER_SIZE_Y)
        self.guiField.drawObject(self.ball.getPosX(), self.ball.getPosY(), self.BALL_SIZE, self.BALL_SIZE)
        # display drawing
        self.guiField.display()
        # clear field
        self.guiField.removeObject(self.player1.getPosX(), self.player1.getPosY(), self.PLAYER_SIZE_X, self.PLAYER_SIZE_Y)
        self.guiField.removeObject(self.player2.getPosX(), self.player2.getPosY(), self.PLAYER_SIZE_X, self.PLAYER_SIZE_Y)
        self.guiField.removeObject(self.ball.getPosX(), self.ball.getPosY(), self.BALL_SIZE, self.BALL_SIZE)
        
    def playerScored(self):
        # Display new score CAN BE OPTIMIZED
        self.guiField.drawFieldAndScore(self.player1.getPoints(), self.player2.getPoints())
        # Display current player and ball positions
        self.displayGame()                
        # Check if a player has max points
        if ((self.player1.getPoints() == self.POINTS_MAX) or (self.player2.getPoints() == self.POINTS_MAX)):
             # Wait to show player won
            pygame.time.delay(self.DELAY_PLAYER_WON)
            # End pong game
            self.PLAY_PONG = False
        else:
            # Wait to show player scored
            pygame.time.delay(self.DELAY_PLAYER_SCORED)
            # Reset all positons
            self.resetGame()

    def playPong(self):
        # play pong 
        while self.PLAY_PONG:
            # debug timer info
            #print(str(self.DEBUG_MAIN_LOOP_CNT) + " tick0 " + str(pygame.time.get_ticks()))
            #self.DEBUG_MAIN_LOOP_CNT = self.DEBUG_MAIN_LOOP_CNT+1
            
            #self.handleConsoleinput()     Can only be implemented when console board is done
            self.handleInput()
            
            if (self.GAME_STATE == self.STATE_PLAY_NORMAL):
                #self.handleControllerInput()  Can only be implemented when controllers are done
                self.displayGame()
                self.updateGame()
            elif (self.GAME_STATE == self.STATE_PLAYER1_SCORED):
                self.player1.addPoint()
                self.playerScored()                
            elif (self.GAME_STATE == self.STATE_PLAYER2_SCORED):
                self.player2.addPoint()
                self.playerScored()                                       
            
            # debug timer info
            #print(str(self.DEBUG_MAIN_LOOP_CNT) + " tick1 " + str(pygame.time.get_ticks()-1))
            
            clock.tick(30)
            


