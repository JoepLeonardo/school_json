# command // print ("hello world %i" %(half_line_y)) // |FULLSCREEN
import pygame
from pygame.locals import *
pygame.init()

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
        



