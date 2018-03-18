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

#######################
### END OF SETTINGS ###
#######################

# pygame init
pygame.init()
clock = pygame.time.Clock()

# make objects
guiField = GuiField()
player1 = Player(guiField.getFieldStartX(), (guiField.getFieldHeight()/2), playerSizeX, playerSizeY, guiField.getFieldStartY(), (guiField.getFieldEndY()-playerSizeY))
player2 = Player((guiField.getFieldEndX()-playerSizeX), (guiField.getFieldHeight()/2), playerSizeX, playerSizeY, guiField.getFieldStartY(), (guiField.getFieldEndY()-playerSizeY))
ball = Ball((guiField.getFieldWidth()/2), (guiField.getFieldHeight()/2), 1, 1, ballSize, 20)

# variables
playPong=True
player1WallX = guiField.getFieldStartX() + playerSizeX
player2WallX = guiField.getFieldEndX()- playerSizeX

def update_ball():
    for x in range(0, ball.getSpeed()):
        #Check ball hits wall player1
        if((ball.getPosX()+ball.getDirX()) == player1WallX):
            ball.updateDir(1, ball.getDirY())
        
        #Check ball hits wall player2
        if((ball.getPosX()+ball.getDirX()+ballSize) == player2WallX):
            ball.updateDir(-1, ball.getDirY())
            
        #Check ball hits top
        if((ball.getPosY()+ball.getDirY()) == guiField.getFieldStartY()):
            ball.updateDir(ball.getDirX(), 1)
            
        #Check ball hits bottom
        if((ball.getPosY()+ball.getDirY()+ballSize) == guiField.getFieldEndY()):
            ball.updateDir(ball.getDirX(), -1)
            
            
        ball.updatePos((ball.getPosX()+ball.getDirX()), (ball.getPosY()+ball.getDirY()))
        
    

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


