import pygame
from pygame.locals import *
from time import sleep

# pygame init
pygame.init()
pygame.mixer.init()

class Sound():
    def __init__(self):
        self.hit_player = pygame.mixer.Sound('pong_8bit_hit_player.wav')
        self.hit_wall= pygame.mixer.Sound('pong_8bit_hit_wall.wav')
        self.scored= pygame.mixer.Sound('pong_8bit_scored.wav')
        
    def play(self, sound):
        sound.play()        
    
    def playHitPlayer(self):
        print("")
        self.play(self.hit_player)
    
    def playHitWall(self):
        print("")
        self.play(self.hit_wall)
        
    def playHitScored(self):
        print("")
        self.play(self.scored)
        
    def waitWhenBusy(self):
        while pygame.mixer.music.get_busy():
            sleep(1)

#sound = Sound()
#sound.fakeDelay(200)
#sound.playHitWall()
#sound.fakeDelay(200)
#sound.playHitScored()
#sound.fakeDelay(200)

pygame.mixer.music.load('pong_8bit_hit_wall.wav')
pygame.mixer.music.play()

pygame.mixer.music.play()
