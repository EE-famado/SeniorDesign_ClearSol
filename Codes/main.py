import time
import board
import adafruit_ina260
from time import sleep
import RPi.GPIO as GPIO
from check_sensors import *
from calc_sensor_values import *
from EDS_2min_timer import *
from LCD import *
from fsm import *
from csv_code import *

i2c = board.I2C()
start = int(time.time())

#Confirms that sensors are detected
ina260_1, ina260_2, ina260_3, ina260_4 = check_sensors(i2c)

# Configures the lcd
lcd = lcdscreen()

# Initialize GPIO pins 
GPIO.setup(14, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(4, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(26, GPIO.OUT)
state = 1
flagon = 0
count = 0
mainflag = 0
mainflag1 = 1

try:
    while 1:
        lcd.clear()
        if GPIO.input(4) == True:
            print("EDS is turned on")
            GPIO.output(26, False)
        elif GPIO.input(4) == False:
            GPIO.output(26,  True)
        
        #Creates timer for EDS
        timeEDS = int(time.time())
        timeEDS = timeEDS + 1
        
        #Reads the Voltage, Current and power from the sensors using get_values function
        v1,i1,p1 = get_values(ina260_1)
        v2,i2,p2 = get_values(ina260_2)
        v3,i3,p3 = get_values(ina260_3)
        v4,i4,p4 = get_values(ina260_4)
        
        csvdata(count, v1, i1, v2, i2, v3, i3, v4, i4)
        
        if state == 1:
            lcd.clear()
            lcd.message = "Voltage:" + str(v1) + "V \n" + "Current:" + str(i1) + "mA"
            print("Solar Panel Output Current1: %.2f mA Voltage: %.2f V  Power: %.2f mW \n" % (i1, v1, p1))
        elif state == 2:
            lcd.clear()
            lcd.message = "Voltage:" + str(v2) + "V \n" + "Current:" + str(i2) + "mA"
            print("Supercapacitor input Current2: %.2f mA Voltage: %.2f V  Power: %.2f mW \n" % (i2, v2, p2))
        elif state == 3:
            lcd.clear()
            lcd.message = "Voltage:" + str(v3) + "V \n" + "Current:" + str(i3) + "mA"
            print("EDS Current3: %.2f mA Voltage: %.2f V  Power: %.2f mW \n" % (i3, v3, p3))
        elif state == 4:
            lcd.clear()
            lcd.message = "Voltage:" + str(v4) + "V \n" + "Current:" + str(i4) + "mA"
            print("Supercapacitor output Current4: %.2f mA Voltage: %.2f V  Power: %.2f mW \n" % (i4, v4, p4))
        
        if flagon == 0:
            state = 1
            flagon = 1
            fsm(lcd,v1,i1,p1,v2,i2,p2,v3,i3,p3,v4,i4,p4,state)
        elif GPIO.input(14) == False:
            print("Switching Sensors")
            state = state + 1
            fsm(lcd,v1,i1,p1,v2,i2,p2,v3,i3,p3,v4,i4,p4,state)
            if state > 4:
                state = 1
                flagon = 0
            
        sleep(1)
        count = count + 1
except KeyboardInterrupt:
    print("\nCtrl-C pressed. Program exiting")
