import RPi.GPIO as GPIO
import pygame
from pygame.locals import *

pygame.init()

class InputHandler():
    
    # GPIO pins
    PIN_POWER_OFF = 5
    PIN_SELECT = 19
    PIN_NEXT = 13
    PIN_PREV = 26
    PIN_J0_0 = 17
    PIN_J0_1 = 27
    PIN_J0_2 = 22
    PIN_J1_0 = 10
    PIN_J1_1 = 9
    PIN_J1_2 = 11
    
    # values
    DATA_NONE = 0
    DATA_POWER_OFF = 1
    DATA_SELECT = 2
    DATA_NEXT = 3
    DATA_PREV = 4
    
    def __init__(self):
        # Use pinout from BCM
        GPIO.setmode(GPIO.BCM)
        # Set all pins as input
        GPIO.setup(self.PIN_POWER_OFF, GPIO.IN)
        GPIO.setup(self.PIN_SELECT, GPIO.IN)
        GPIO.setup(self.PIN_PREV, GPIO.IN)
        GPIO.setup(self.PIN_NEXT, GPIO.IN)
        GPIO.setup(self.PIN_J0_0, GPIO.IN)
        GPIO.setup(self.PIN_J0_1, GPIO.IN)
        GPIO.setup(self.PIN_J0_2, GPIO.IN)
        GPIO.setup(self.PIN_J1_0, GPIO.IN)
        GPIO.setup(self.PIN_J1_1, GPIO.IN)
        GPIO.setup(self.PIN_J1_2, GPIO.IN)
    
    #def __del__(self):
        #print("exit inputHandler")
    
    def getConsole(self):
        # Returns the pin that's pressed
        data = self.DATA_NONE 
        if (GPIO.input(self.PIN_POWER_OFF)):
            data = self.DATA_POWER_OFF
        elif (GPIO.input(self.PIN_SELECT)):
            data = self.DATA_SELECT
        elif (GPIO.input(self.PIN_NEXT)):
            data = self.DATA_NEXT
        elif (GPIO.input(self.PIN_PREV)):
            data = self.DATA_PREV
        return data
                
    def getController1(self):
        data = 0
        for event in pygame.event.get():
            # Check if 'w' button is pressed
            if (event.type == pygame.KEYDOWN and event.key == pygame.K_w):
                data = -1
            # Check if 's' button is pressed
            elif (event.type == pygame.KEYDOWN and event.key == pygame.K_s):
                data = 1
        return data
                
    def getController2(self):
        data = 0
        for event in pygame.event.get():
            # Check if 'up' button is pressed
            if (event.type == pygame.KEYDOWN and event.key == pygame.K_UP):
                data = -1
            # Check if 'down' button is pressed
            elif (event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN):
                data = 1
        return data
            
            
    