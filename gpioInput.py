import RPi.GPIO as GPIO
import time

PIN_OFF = 5
PIN_SELECT = 19
PIN_NEXT = 13
PIN_PREV = 26

J0_0 = 17
J0_1 = 27
J0_2 = 22

J1_0 = 10
J1_1 = 9
J1_2 = 11


GPIO.setmode(GPIO.BCM)

GPIO.setup(PIN_OFF, GPIO.IN)
GPIO.setup(PIN_SELECT, GPIO.IN)
GPIO.setup(PIN_PREV, GPIO.IN)
GPIO.setup(PIN_NEXT, GPIO.IN)

GPIO.setup(J0_0, GPIO.IN)
GPIO.setup(J0_1, GPIO.IN)
GPIO.setup(J0_2, GPIO.IN)

GPIO.setup(J1_0, GPIO.IN)
GPIO.setup(J1_1, GPIO.IN)
GPIO.setup(J1_2, GPIO.IN)

time.sleep(0.01)

print("Start")
try:
    while True:
        time.sleep(0.5)
        print("OFF : ", (GPIO.input(PIN_OFF)))
        print("SLCT: ", (GPIO.input(PIN_SELECT)))
        print("NEXT: ", (GPIO.input(PIN_NEXT)))
        print("PREV: ", (GPIO.input(PIN_PREV)))
                
        #print("J0 ",(GPIO.input(J0_0), GPIO.input(J0_1), GPIO.input(J0_2)) )
        print("J1 ",(GPIO.input(J1_0), GPIO.input(J1_1), GPIO.input(J1_2)) )
        
        #print("")       
except KeyboardInterrupt: #stop when cntrl+c is pressed
    GPIO.cleanup()
print("End")    
    


