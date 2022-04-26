import time
import datetime

def stop_timer(lcd):
    h = 0
    m = 0
    s = 5
    total_seconds = h * 3600 + m * 60 + s
    
    #While loop that checks if total_seconds reaches zero
    #If not zero, decrement total time by one second
    while total_seconds > 0:
        #Timer represents time left on countdown
        timer = datetime.timedelta(seconds = total_seconds)
        
        #Converted to a string to print on lcd screen
        timers = str(timer)
        
        #Prints the time left on the timer
        print(timer, end="\r")
        lcd.message = "EDS activated" + "\n" + timers
        time.sleep(1)
 
        total_seconds -= 1