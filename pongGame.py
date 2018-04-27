from inputHandler import InputHandler
from guiField import GuiField
from player import Player
from ball import Ball
import pygame
from pygame.locals import *
import sys
import time
import random

# pygame init
pygame.init()
clock = pygame.time.Clock()

class PongGame():
    
    # play pong loop
    PLAY_PONG = True
    # Maximum points a player can score (guiField display's until 3)
    POINTS_MAX = 3
    # maxiumum framerate if programm runs fast enough
    FPS_MAX = 60
    # Ball speed increasement after hit with player
    BALL_SPEED_INCREASE = 1    
    # Time before the game starts (ms)
    DELAY_BEFORE_START = 500
    DELAY_PLAYER_SCORED = 1000
    DELAY_PLAYER_WON = 3000    
    # Space between wall and player
    SPACE_WALL_PLAYER = 50
    # Sensitivity of the controllers (px's moved per step)
    CONTROLLER_SENSITIVITY = 10
    
    # Game states
    GAME_STATE = None
    STATE_PLAY_NORMAL = 0
    STATE_PLAYER1_SCORED = 1
    STATE_PLAYER2_SCORED = 2
    # Directions (opposites must be inverted)
    DIR_LEFT = -1
    DIR_RIGHT = (DIR_LEFT*-1) 
    DIR_NORMAL = 0
    DIR_MAX = 2.0
    
    # Sound files
    SOUND_SCORED = "pong_8bit_scored.wav"
    SOUND_HIT_WALL = "pong_8bit_hit_wall.wav"
    SOUND_HIT_PLAYER = "pong_8bit_hit_player.wav"
    
    # debug variables
    DEBUG_LOOP_CNT = 0
    DEBUG_LOOP_START_TIME = 0
    DEBUG_LOOP_END_TIME = 0
        
    def __init__(self, inInput, ballSpeed, ballSize, playerWidth, playerHeight):        
        pygame.init()        
        
        # create objects
        self.input = inInput
        self.guiField = GuiField()
        self.ball = Ball(ballSize, self.guiField.getFieldStartY(), (self.guiField.getFieldEndY()-ballSize))
        player1PosX = self.guiField.getFieldStartX() + self.SPACE_WALL_PLAYER
        player2PosX = self.guiField.getFieldEndX() -self.SPACE_WALL_PLAYER - playerWidth
        self.player1 = Player(player1PosX, playerWidth, playerHeight, self.guiField.getFieldStartY(), (self.guiField.getFieldEndY()-playerHeight))
        self.player2 = Player(player2PosX, playerWidth, playerHeight, self.guiField.getFieldStartY(), (self.guiField.getFieldEndY()-playerHeight))
                
        # create variables
        self.ballStartSpeed = ballSpeed
        self.fieldHeigtMiddle = (((int)(self.guiField.getFieldHeight()/2)))
        self.fieldWidthMiddle = (((int)(self.guiField.getFieldWidth()/2)))
    
    def ballDirRandomHorizontal(self):
        dir = self.DIR_NORMAL
        if (self.GAME_STATE == self.STATE_PLAYER1_SCORED):
            dir = self.DIR_LEFT
        elif (self.GAME_STATE == self.STATE_PLAYER2_SCORED):
            dir = self.DIR_RIGHT
        # random left or right
        else:            
            if (bool(random.getrandbits(1))):
                dir = self.DIR_RIGHT
            else:
                dir = self.DIR_LEFT
        return dir
    
    def ballDirRandomVertical(self):
        # random direction between half the maximum
        dir = self.DIR_MAX/4        
        dir = float(random.uniform((dir*-1), dir))
        return dir
        
    def resetGame(self):
        # Reset the ball
        ballPosY = self.fieldHeigtMiddle-(int(self.ball.getSize()/2))
        self.ball.reset(self.fieldWidthMiddle, ballPosY, self.ballDirRandomHorizontal(), self.ballDirRandomVertical(), self.ballStartSpeed)
        # Reset players
        playerPosY = self.fieldHeigtMiddle-(int(self.player1.getHeight()/2))
        self.player1.reset(playerPosY)
        self.player2.reset(playerPosY)
        # Draw the field and score
        self.guiField.drawFieldAndScore(self.player1.getPoints(), self.player2.getPoints())
        # Game state to noraml
        self.GAME_STATE = self.STATE_PLAY_NORMAL
        # Display the current game state
        self.displayGame()
        # Wait before the game starts
        pygame.time.wait(self.DELAY_BEFORE_START)
    
    def playSound(self, path):
        pygame.mixer.Sound(path).play(0)

    def playerHitBall(self, playerY, ballY):
        # Attention: function only checks hit on y-axis 
        playerHitBall = True        
        # Check if player missed ball ( (ball above player) or (ball below player) )
        if (((ballY+self.ball.getSize()) < playerY) or (ballY > (playerY + self.player1.getHeight()))):
            playerHitBall= False
        return playerHitBall

    def playerHitBallDir(self, playerY, ballY):
        # Attention: playerHigh is a lower number than playerLow,
        # because the higher the part off the screen, the lower the number
        playerHigh = playerY - self.ball.getSize()
        playerLow = playerY + self.player1.getHeight()
        hitLength = playerLow - playerHigh
        middleOfHitRange = playerHigh + int(hitLength/2)
        # the further the hit is from the middle of the hit range, the more dirY goes to DIR_MAX
        distanceFromMiddle = ballY - middleOfHitRange
        dirY = distanceFromMiddle * self.DIR_MAX / (int(hitLength/2)) 
        return dirY
    
    def updateBallDirX(self):       
        playerHitball = False
        playerMissedBall = False
        ballDiry = self.ball.getDirY()
        #Check ball hit player1 x-axis
        if((self.ball.getPosX()+self.ball.getDirX()) == self.player1.getPosX() + self.player1.getWidth()):
            if(self.playerHitBall(self.player1.getPosY(), int(self.ball.getPosY()))):
                playerHitball = True
                ballDiry = self.playerHitBallDir(self.player1.getPosY(), int(self.ball.getPosY()))
        #Check ball hit player2 x-axis line
        elif((self.ball.getPosX()+self.ball.getDirX()+self.ball.getSize()) == self.player2.getPosX()):
            if(self.playerHitBall(self.player2.getPosY(), int(self.ball.getPosY()))):
                playerHitball = True                    
                ballDiry = self.playerHitBallDir(self.player2.getPosY(), int(self.ball.getPosY()))
        #Check ball hit player1 wall
        elif((self.ball.getPosX()+self.ball.getDirX()) <= self.guiField.getFieldStartX()):
            playerMissedBall = True
        #Check ball hit player2 wall
        elif((self.ball.getPosX()+self.ball.getDirX()+self.ball.getSize()) >= self.guiField.getFieldEndX()):
            playerMissedBall = True
        #Check if player hit the ball
        if(playerHitball):
            self.playSound(self.SOUND_HIT_PLAYER)
            ballDirX = (self.ball.getDirX()*-1)
            self.ball.updateDir(ballDirX, ballDiry)
            self.ball.increaseSpeed(self.BALL_SPEED_INCREASE)            
        return playerMissedBall
            
    def updateBallDirY(self):
        ballHitWall = False
        #Check ball hits top
        if(int((self.ball.getPosY()+self.ball.getDirY())) <= self.guiField.getFieldStartY()):
            ballHitWall = True
        #Check ball hits bottom
        elif(int((self.ball.getPosY()+self.ball.getDirY()+self.ball.getSize())) >= self.guiField.getFieldEndY()):
            ballHitWall = True
        if(ballHitWall):
            # play sound
            self.playSound(self.SOUND_HIT_WALL)
            # invert the vertical ball direction
            self.ball.updateDir(self.ball.getDirX(), (self.ball.getDirY()*-1))
  
    def updateGame(self):
        # Ball speed is the number of loops
        loops = self.ball.getSpeed()
        for loopCnt in range(0, loops):            
            # Update ball y direction (if ball hits top or bottom) 
            self.updateBallDirY()            
            # Update ball x (and y) direction (if ball hits player or wall) 
            playerMissedBall = self.updateBallDirX()
            if (playerMissedBall):
                # check who won via ballDirX left or right
                if (self.ball.getDirX() == self.DIR_LEFT):
                    self.GAME_STATE = self.STATE_PLAYER2_SCORED
                else:
                    self.GAME_STATE = self.STATE_PLAYER1_SCORED
                # end the loop
                loopCnt = self.ball.getSpeed()            
            # update ball position            
            self.ball.updatePos()
        
    def handleControllerInput(self):
        # update player1 pos
        data = self.input.getController1()        
        self.player1.move((data*self.CONTROLLER_SENSITIVITY));
        # update player2 pos
        data = self.input.getController2()
        self.player2.move((data*self.CONTROLLER_SENSITIVITY));
        
    def handleInput(self):
        pixelsToMove = 40
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
        self.guiField.drawObject(self.player1.getPosX(), self.player1.getPosY(), self.player1.getWidth(), self.player1.getHeight())
        self.guiField.drawObject(self.player2.getPosX(), self.player2.getPosY(), self.player2.getWidth(), self.player2.getHeight())
        self.guiField.drawObject(self.ball.getPosX(), int(self.ball.getPosY()), self.ball.getSize(), self.ball.getSize())
        # display drawing
        self.guiField.displayFast()
        # clear field
        self.guiField.removeObject(self.player1.getPosX(), self.player1.getPosY(), self.player1.getWidth(), self.player1.getHeight())
        self.guiField.removeObject(self.player2.getPosX(), self.player2.getPosY(), self.player2.getWidth(), self.player2.getHeight())
        self.guiField.removeObject(self.ball.getPosX(), int(self.ball.getPosY()), self.ball.getSize(), self.ball.getSize())
        
    def playerScored(self):
        self.playSound(self.SOUND_SCORED)
        while pygame.mixer.get_busy():
            pygame.time.wait(200)
        # Display new score (can be optimized)
        self.guiField.drawFieldAndScore(self.player1.getPoints(), self.player2.getPoints())
        # Display current player and ball positions
        self.displayGame()                
        # Check if a player has max points
        if ((self.player1.getPoints() == self.POINTS_MAX) or (self.player2.getPoints() == self.POINTS_MAX)):
             # Wait to show player won
            pygame.time.wait(self.DELAY_PLAYER_WON)
            # End pong game
            self.PLAY_PONG = False
        else:
            # Wait to show player scored
            pygame.time.wait(self.DELAY_PLAYER_SCORED)
            # Reset all positons
            self.resetGame()

    def playPong(self):
        # reset the game so all variables are declared right
        self.resetGame()
        # play pong 
        while self.PLAY_PONG:
            # debug timer info
            #self.DEBUG_LOOP_START_TIME = pygame.time.get_ticks()
            
            # handle keyboard input
            self.handleInput()
            
            if (self.GAME_STATE == self.STATE_PLAY_NORMAL):
                self.handleControllerInput()
                self.updateGame()
                self.displayGame()
            elif (self.GAME_STATE == self.STATE_PLAYER1_SCORED):
                self.player1.addPoint()
                self.playerScored()                
            elif (self.GAME_STATE == self.STATE_PLAYER2_SCORED):
                self.player2.addPoint()
                self.playerScored()                                    
            
            # debug timer info
            #print(str(self.DEBUG_LOOP_CNT) + " time " + str(pygame.time.get_ticks()-self.DEBUG_LOOP_START_TIME) + " tick: "+ str(pygame.time.get_ticks()))
            #print(" gebruik: " + str(pygame.time.get_ticks()-self.DEBUG_LOOP_START_TIME) + " over: "+ str(self.DEBUG_LOOP_START_TIME - self.DEBUG_LOOP_END_TIME))
            #self.DEBUG_LOOP_CNT = self.DEBUG_LOOP_CNT+1
            #self.DEBUG_LOOP_END_TIME = pygame.time.get_ticks()
            
            clock.tick(self.FPS_MAX)
        # end of playPong
            


