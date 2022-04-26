import adafruit_ina260

def check_sensors(i2c):
    ina260_1 = adafruit_ina260.INA260(i2c)
    ina260_2 = adafruit_ina260.INA260(i2c, address = 0x41)
    ina260_3 = adafruit_ina260.INA260(i2c, address = 0x44)
    ina260_4 = adafruit_ina260.INA260(i2c, address = 0x45)

    if(isinstance(ina260_1, adafruit_ina260.INA260)):
        print("Found sensor at address 0x40")
    else:
        print("Sensor not found at address 0x40")
        
    if(isinstance(ina260_2, adafruit_ina260.INA260)):
        print("Found sensor at address 0x41")
    else:
        print("Sensor not found at address 0x41")
        
    if(isinstance(ina260_3, adafruit_ina260.INA260)):
        print("Found sensor at address 0x44")
    else:
        print("Sensor not found at address 0x44")
        
    if(isinstance(ina260_4, adafruit_ina260.INA260)):
        print("Found sensor at address 0x45")
    else:
        print("Sensor not found at address 0x45")
        
    return ina260_1, ina260_2, ina260_3, ina260_4;