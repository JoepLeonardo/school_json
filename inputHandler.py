#####################################################
#
#        inputHandler.py functionality:
#
# * has all GPIO information
# * returns the pressed buttons on request
# * returns the controllerdata on request
#
#####################################################

import RPi.GPIO as GPIO
import pygame
from pygame.locals import *
from functools import partial

pygame.init()

class InputHandler():
    
    # GPIO pins
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
    JOYSTICK_IDLE = 4
    
    def callBackButtonPressed(self, channel):
        if (GPIO.input(self.PIN_SELECT)):
            self.selectPressed = True
        elif (GPIO.input(self.PIN_NEXT)):
            self.nextPressed = True
        elif (GPIO.input(self.PIN_PREV)):
            self.prevPressed = True
    
    def setInterrupts(self):
        # Set interrupts on rising edge
        GPIO.add_event_detect(self.PIN_SELECT, GPIO.RISING, callback=lambda *a: self.callBackButtonPressed(self.PIN_SELECT))
        GPIO.add_event_detect(self.PIN_NEXT, GPIO.RISING, callback=lambda *a: self.callBackButtonPressed(self.PIN_NEXT))
        GPIO.add_event_detect(self.PIN_PREV, GPIO.RISING, callback=lambda *a: self.callBackButtonPressed(self.PIN_PREV))        
        
    def removeInterrupts(self):
        GPIO.remove_event_detect(self.PIN_SELECT)
        GPIO.remove_event_detect(self.PIN_NEXT)
        GPIO.remove_event_detect(self.PIN_PREV)
    
    def __init__(self):
        # Use pinout from BCM
        GPIO.setmode(GPIO.BCM)
        # Set all pins as input
        GPIO.setup(self.PIN_SELECT, GPIO.IN)
        GPIO.setup(self.PIN_PREV, GPIO.IN)
        GPIO.setup(self.PIN_NEXT, GPIO.IN)
        GPIO.setup(self.PIN_J0_0, GPIO.IN)
        GPIO.setup(self.PIN_J0_1, GPIO.IN)
        GPIO.setup(self.PIN_J0_2, GPIO.IN)
        GPIO.setup(self.PIN_J1_0, GPIO.IN)
        GPIO.setup(self.PIN_J1_1, GPIO.IN)
        GPIO.setup(self.PIN_J1_2, GPIO.IN)
        # create variables
        self.selectPressed = False
        self.nextPressed = False
        self.prevPressed = False
        # Set interrupts
        self.removeInterrupts()
        self.setInterrupts()
        
    #def __del__(self):
        #print("exit inputHandler")
    
    def reset(self):
        # reset variables
        self.selectPressed = False
        self.nextPressed = False
        self.prevPressed = False
    
    def getConsole(self):
        # Returns the pin thats pressed
        data = self.DATA_NONE            
        if (self.selectPressed):
            self.selectPressed = False
            data = self.DATA_SELECT
        elif (self.nextPressed):
            self.nextPressed = False
            data = self.DATA_NEXT
        elif (self.prevPressed):
            self.prevPressed = False
            data = self.DATA_PREV
        return data
    
    def getControllerData(self, pin1, pin2, pin3):
        # data minus joystick idle value
        data = (self.JOYSTICK_IDLE*-1)
        # add controller values to data
        if(GPIO.input(pin1)):
            data += 1
        if (GPIO.input(pin2)):
            data += 2
        if (GPIO.input(pin3)):
            data += 4
        # controller recognizes 3 steps up and 4 down, last step down must be removed
        if (data == -4):
            data = -3
        #return data
        return data
                    
    def getController1(self):
        data = self.getControllerData(self.PIN_J0_0, self.PIN_J0_1, self.PIN_J0_2)
        return data
                
    def getController2(self):
        data = self.getControllerData(self.PIN_J1_0, self.PIN_J1_1, self.PIN_J1_2)
        return data
            
            
    