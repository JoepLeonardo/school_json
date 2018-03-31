from guiField import GuiField
from player import Player
from ball import Ball
import pygame
from pygame.locals import *

#####################
### GAME SETTINGS ###
#####################

# Set player bad size
playerSizeX = 20
playerSizeY = 100

# Set ball size
ballSize = 20
ballSpeed = 20

#######################
### END OF SETTINGS ###
#######################

# pygame init
pygame.init()
clock = pygame.time.Clock()

# variables
playPong=True
dirUp = -1
dirDown = 1
dirLeft = -1
dirRight = 1 
dirNormal = 0
playerMissedBall = 9

# make objects
guiField = GuiField()
player1 = Player(guiField.getFieldStartX(), (guiField.getFieldHeight()/2), playerSizeX, playerSizeY, guiField.getFieldStartY(), (guiField.getFieldEndY()-playerSizeY))
player2 = Player((guiField.getFieldEndX()-playerSizeX), (guiField.getFieldHeight()/2), playerSizeX, playerSizeY, guiField.getFieldStartY(), (guiField.getFieldEndY()-playerSizeY))
ball = Ball((guiField.getFieldWidth()/2), (guiField.getFieldHeight()/2), dirRight, dirNormal, ballSize, ballSpeed)

# variables that need info from object(s)
player1WallX = guiField.getFieldStartX() + playerSizeX
player2WallX = guiField.getFieldEndX()- playerSizeX

def ballHitPlayerDirection(playerY, playerSize, ballY, ballSize):
    dir = dirNormal
    # check if ball is higher than palyer
    if ((ballY+ballSize) < playerY):
        dir = playerMissedBall
    # check if the middle of the ball hit upper part of the palyer
    elif ((ballY+ballSize) <= (playerY+(playerSize/3))):
        dir = dirUp
        
    # check if ball is lower than player
    elif (ballY > (playerY+playerSize)):
        dir = playerMissedBall
    # check if the middle of the ball hit lower part of the palyer
    elif (ballY >= (playerY+(playerSize*2/3))):
        dir = dirDown
    
    #else dir is normal
    return dir    

def update_ball():
    for x in range(0, ball.getSpeed()):
        dirX = ball.getDirX()
        dirY_OrGameOver = ball.getDirY()
        
        #Check ball hits wall player1
        if((ball.getPosX()+ball.getDirX()) == player1WallX):
            dirX = dirRight
            dirY_OrGameOver = ballHitPlayerDirection(player1.getPosY(), player1.getSizeY(), ball.getPosY(), ball.getSize())
        #Check ball hits wall player2
        elif((ball.getPosX()+ball.getDirX()+ballSize) == player2WallX):
            dirX = dirLeft
            dirY_OrGameOver = ballHitPlayerDirection(player2.getPosY(), player2.getSizeY(), ball.getPosY(), ball.getSize())
        #Check ball hits top
        elif((ball.getPosY()+ball.getDirY()) == guiField.getFieldStartY()):
            dirY_OrGameOver = dirDown
        #Check ball hits bottom
        elif((ball.getPosY()+ball.getDirY()+ballSize) == guiField.getFieldEndY()):
            dirY_OrGameOver = dirUp
        
        #if(dirY_OrGameOver != playerMissedBall):
        # update ball dir and position
        ball.updateDir(dirX, dirY_OrGameOver)
        ball.updatePos()
        #else
        #check who won via dirX left or right  

def handle_input():
    pixelsToMove = 30
    for event in pygame.event.get():
        # Check if 'esc' or close button is pressed
        if (event.type == QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE)):
            return False
        # Check if 'up' button is pressed
        elif (event.type == pygame.KEYDOWN and event.key == pygame.K_UP):
            # move player 1 100 pixels up
            player2.move(-pixelsToMove);
        # Check if 'down' button is pressed
        elif (event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN):
            # move player 1 100 pixels down
            player2.move(pixelsToMove);
       # Check if 'w' button is pressed
        elif (event.type == pygame.KEYDOWN and event.key == pygame.K_w):
            # move player 2 100 pixels up
            player1.move(-pixelsToMove);
        # Check if 's' button is pressed
        elif (event.type == pygame.KEYDOWN and event.key == pygame.K_s):
            # move player 2 100 pixels down
            player1.move(pixelsToMove); 
    return True

while playPong:
    update_ball()
    # draw
    guiField.fieldClear()
    guiField.fieldAddPlayer(player1.getPosX(), player1.getPosY(), playerSizeX, playerSizeY, 0)
    guiField.fieldAddPlayer(player2.getPosX(), player2.getPosY(), playerSizeX, playerSizeY, 0)
    guiField.fieldAddBall(ball.getPosX(), ball.getPosY(), ballSize)
    guiField.fieldDisplay()
    
    clock.tick(60)
    
    playPong = handle_input()
        
# end of programm
del guiField
del player1
del player2
pygame.quit


