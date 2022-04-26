from time import sleep

def fsm(lcd,v1,i1,p1,v2,i2,p2,v3,i3,p3,v4,i4,p4,state):
    
    if state == 1:
        lcd.clear()
        lcd.message = "Solar panel" + "\n" + "output"
        sleep(2)
    elif state == 2:
        lcd.clear()
        lcd.message = "Supercapacitors" + "\n" + "input"
        sleep(2)
    elif state == 3:
        lcd.clear()
        lcd.message = "EDS"
        sleep(2)
    elif state == 4:
        lcd.clear()
        lcd.message = "Supercapacitors" + "\n" + "output"
        sleep(2)
    