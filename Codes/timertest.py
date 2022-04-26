import time
import datetime
from time import sleep
from EDS_2min_timer import *
import RPi.GPIO as GPIO

start = int(time.time())

GPIO.setwarnings(False) 
GPIO.setmode(GPIO.BCM)
GPIO.setup(26, GPIO.OUT)

while 1:
    
    timeEDS = int(time.time())
    print(timeEDS)
    
    if ((timeEDS - start) % 10 == 0):
        print('EDS is turned on')
        GPIO.output(26, False)
        stop_timer()
        GPIO.output(26, True)
        
    sleep(1)