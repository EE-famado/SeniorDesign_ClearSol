import time
import datetime

def stop_timer(h, m, s):
    total_seconds = h * 3600 + m * 60 + s
    
    #While loop that checks if total_seconds reaches zero
    #If not zero, decrement total time by one second
    while total_seconds > 0:
        #Timer represents time left on countdown
        timer = datetime.timedelta(seconds = total_seconds)
        
        #Prints the time left on the timer
        print(timer, end="\r")
 
        time.sleep(1)
 
        total_seconds -= 1
    flagon = 0
    flagoff = 1
    return flagon, flagoff;
h = 0
m = 2
s = 0
stop_timer(int(h), int(m), int(s))