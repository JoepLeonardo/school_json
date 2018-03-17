# command // print ("hello world %i" %(half_line_y))
import pygame
from pygame.locals import *
pygame.init()
clock = pygame.time.Clock()

# monitor resoluten
monitorWidth = pygame.display.Info().current_w
monitorHeight = pygame.display.Info().current_h
# create monitor screen
monitorScreen = pygame.display.set_mode((monitorWidth, monitorHeight),HWSURFACE|DOUBLEBUF|FULLSCREEN )

# CTOUCH resolution (1824x984)
surfaceWidth = 1824
surfaceHeight = 984
# size above the game to display score and gamename
surfaceTop = 100
# create surface screen where all items are going to be displayed on
surfaceScreen = pygame.Surface((surfaceWidth, surfaceHeight))

# colors
colorWhite = (255, 255, 255)
colorBlack = (0, 0, 0)

def getSurfaceWidth():
    return surfaceWidth

def getSurfaceHeight():
    return surfaceHeight

# display the surface on the monitor
def display(surface):
    # adjust the surface to the monitor size
    monitorScreen.blit(pygame.transform.scale(surface, (monitorWidth, monitorHeight)), (0, 0))
    # display
    pygame.display.flip()
    
def handle_input():
    for event in pygame.event.get():
        if event.type == QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE) :
            pygame.display.quit() 
            pygame.quit()

while True:
    handle_input()
    
    surfaceScreen.fill(colorBlack)
    # draw board border
    pygame.draw.rect(surfaceScreen, colorWhite, pygame.Rect(0, surfaceTop, getSurfaceWidth(), getSurfaceHeight()-surfaceTop), 5)
    # draw board half line
    half_line_x = getSurfaceWidth()/2
    half_line_y = surfaceTop
    half_line_w = 5
    half_line_h = 20
    while half_line_y < getSurfaceHeight():
        pygame.draw.rect(surfaceScreen, colorWhite, pygame.Rect(half_line_x, half_line_y, half_line_w, half_line_h))
        half_line_y += (half_line_h*2)
    # display the surface
    display(surfaceScreen)
    
    clock.tick(60)



