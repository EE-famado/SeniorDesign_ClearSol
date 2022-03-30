import time
import datetime

def stop_timer(input_state):
    h = 0
    m = 2
    s = 0
    total_seconds = h * 3600 + m * 60 + s
    
    #While loop that checks if total_seconds reaches zero
    #If not zero, decrement total time by one second
    while total_seconds > 0 && input_state == False:
        #Timer represents time left on countdown
        timer = datetime.timedelta(seconds = total_seconds)
        
        #Prints the time left on the timer
        print(timer, end="\r")
 
        time.sleep(1)
 
        total_seconds -= 1
    
    input_state = True
    return  input_state;

stop_timer(int(h), int(m), int(s))
