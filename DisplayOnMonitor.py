# command // print ("hello world %i" %(half_line_y)) // |FULLSCREEN
import pygame
from pygame.locals import *
pygame.init()
clock = pygame.time.Clock()

class DisplayOnMonitor:
    # monitor resoluten
    monitorWidth = pygame.display.Info().current_w
    monitorHeight = pygame.display.Info().current_h
    # create monitor screen
    monitorScreen = pygame.display.set_mode((monitorWidth, monitorHeight),HWSURFACE|DOUBLEBUF )    

    # display the surface on the monitor
    def display(self, surface):
        # adjust the surface to the monitor size
        self.monitorScreen.blit(pygame.transform.scale(surface, (self.monitorWidth, self.monitorHeight)), (0, 0))
        # display
        pygame.display.flip()
        
class GuiField:
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
    
    monitor = DisplayOnMonitor()
    
    def clearSurface(self):
        print(self)
        # make the surface black
        self.surfaceScreen.fill(self.colorBlack)
        
        # draw board border
        pygame.draw.rect(self.surfaceScreen, self.colorWhite, pygame.Rect(0, self.surfaceTop, self.surfaceWidth, self.surfaceHeight-self.surfaceTop), 5)
        # draw board half line
        half_line_x = self.surfaceWidth/2
        half_line_y = self.surfaceTop
        half_line_w = 5
        half_line_h = 20
        while half_line_y < self.surfaceHeight:
            pygame.draw.rect(self.surfaceScreen, self.colorWhite, pygame.Rect(half_line_x, half_line_y, half_line_w, half_line_h))
            half_line_y += (half_line_h*2)
            
        # display the surface
        self.monitor.display(self.surfaceScreen) 
    

    def getSurfaceWidth():
        return surfaceWidth

    def getSurfaceHeight():
        return surfaceHeight


guiField = GuiField()

def handle_input():
    for event in pygame.event.get():
        if event.type == QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE) :
            pygame.display.quit() 
            pygame.quit()

while True:
    handle_input()
    guiField.clearSurface()
    clock.tick(60)



