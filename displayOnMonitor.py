import pygame
from pygame.locals import *
pygame.init()

class DisplayOnMonitor:
    # monitor resoluten
    monitorWidth = pygame.display.Info().current_w
    monitorHeight = pygame.display.Info().current_h
    # create monitor screen |FULLSCREEN  
    monitorScreen = pygame.display.set_mode((monitorWidth, monitorHeight),HWSURFACE|DOUBLEBUF)
           
    def __del__(self):
        # close the display
        pygame.display.quit()
                
    # display the surface on the monitor
    def display(self, surface):
        # adjust the surface to the monitor size
        self.monitorScreen.blit(pygame.transform.scale(surface, (self.monitorWidth, self.monitorHeight)), (0, 0))
        # display
        pygame.display.flip()
        
        



