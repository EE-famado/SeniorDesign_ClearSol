import adafruit_ina260

def get_values(ina260):

    v = float("{:.2f}".format(ina260.voltage))
    i = float("{:.2f}".format(ina260.current))
    p = float("{:.2f}".format(ina260.power))

    return v,i,p;