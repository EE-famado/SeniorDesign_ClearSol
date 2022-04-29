# Overview

In this overview we describe at a high level the functionality of the code that we have, what it does and how to run it.

Our folder that contains all of our python code is “SeniorDesign_ClearSol/Codes/”, here we have all of our functions and our main.py, which is the main script to run our project. At a high level our code does 3 main things, samples data from the INA260 power sensors, allows for user input when they flip the switch or press the button, and it allows us to write the data to a CSV file to analyze later/ display the data on the LCD screen.

# Module Description

lcdscreen() - Initialized in the LCD.py script. We use this function in order to initialize the 7 bit LCD display. We configured the pins to correspond to the ones we have hooked up to the pi. If you disconnect the wires to the LCD and change the GPIO pins you will need to go to this function and change the pin assignment in lines 10-16 to the new pins you have.

getvalues() - Initialized in calc_sensor_value.py. This module is used to read the raw data coming from the sensor and calculate the current, voltage and power into float variables. The module takes in the adafruit_ina260.INA260() address of each sensor and uses it to get the data it is reading. It returns 3 floats, v, i,p.

check_sensors() - Initialized in check_sensors.py. This module creates the ina260 tags used to read from the sensors and error checks that they were created correctly. It returns a print statement saying if the sensor was found in the right I2C address.

csvdata() - Initialized in csv_code.py. This module takes the data the sensors are reading and puts it in a CSV file called “data.csv”. It takes in the v and i for all 4 sensors and creates a column for each one in the CSV file. It also takes in a “count” variable that is used to format the rows and make it easier to graph and analyze after you have collected the data. Since this function runs every time you run the program, you should clean the data.csv file and delete the previous data before running it. That way you know the data you collected is from the last time you ran the program.

fsm() - Initialized in fsm.py. This module creates the finite state machine used to toggle between the sensors when the user presses the button. Based on the “state” variable that is being passed to the function it will print a statement on the LCD screen telling the user which sensor is being read right now.

plot_csv.py - This script can be used to graph the data in the data.csv. However, we recommend just downloading the CSV file using a USB drive from the Pi and moving it to your laptop and just using MATLAB or Excel to plot the data. This is because plotting the data using python can be really slow, especially if you’re doing it directly from the pi.

![Software flow chart](/images/softwareflowchart.png)
