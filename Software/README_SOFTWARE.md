# Overview

In this overview we describe at a high level the functionality of the code that we have, what it does and how to run it.

Our folder that contains all of our python code is “SeniorDesign_ClearSol/Codes/”, here we have all of our functions and our main.py, which is the main script to run our project. At a high level our code does 3 main things, samples data from the INA260 power sensors, allows for user input when they flip the switch or press the button, and it allows us to write the data to a CSV file to analyze later/ display the data on the LCD screen.

---

# Module Description

[lcdscreen()](https://github.com/EE-famado/SeniorDesign_ClearSol/blob/main/Codes/LCD.py) - Initialized in the LCD.py script. We use this function in order to initialize the 7 bit LCD display. We configured the pins to correspond to the ones we have hooked up to the pi. If you disconnect the wires to the LCD and change the GPIO pins you will need to go to this function and change the pin assignment in lines 10-16 to the new pins you have.

[getvalues()](https://github.com/EE-famado/SeniorDesign_ClearSol/blob/main/Codes/calc_sensor_values.py) - Initialized in calc_sensor_value.py. This module is used to read the raw data coming from the sensor and calculate the current, voltage and power into float variables. The module takes in the adafruit_ina260.INA260() address of each sensor and uses it to get the data it is reading. It returns 3 floats, v, i,p.

[check_sensors()](https://github.com/EE-famado/SeniorDesign_ClearSol/blob/main/Codes/check_sensors.py) - Initialized in check_sensors.py. This module creates the ina260 tags used to read from the sensors and error checks that they were created correctly. It returns a print statement saying if the sensor was found in the right I2C address.

[csvdata()](https://github.com/EE-famado/SeniorDesign_ClearSol/blob/main/Codes/csv_code.py) - Initialized in csv_code.py. This module takes the data the sensors are reading and puts it in a CSV file called “data.csv”. It takes in the v and i for all 4 sensors and creates a column for each one in the CSV file. It also takes in a “count” variable that is used to format the rows and make it easier to graph and analyze after you have collected the data. Since this function runs every time you run the program, you should clean the data.csv file and delete the previous data before running it. That way you know the data you collected is from the last time you ran the program.

[fsm()](https://github.com/EE-famado/SeniorDesign_ClearSol/blob/main/Codes/fsm.py) - Initialized in fsm.py. This module creates the finite state machine used to toggle between the sensors when the user presses the button. Based on the “state” variable that is being passed to the function it will print a statement on the LCD screen telling the user which sensor is being read right now.

[plot_csv.py](https://github.com/EE-famado/SeniorDesign_ClearSol/blob/main/Codes/plot_csv.py) - This script can be used to graph the data in the data.csv. However, we recommend just downloading the CSV file using a USB drive from the Pi and moving it to your laptop and just using MATLAB or Excel to plot the data. This is because plotting the data using python can be really slow, especially if you’re doing it directly from the pi.

![Software flow chart](/images/softwareflowchart.png)

Chart of our overall software

# Dev/Build Information

The following lists below are of the libraries installed and used in this project. Most of these libraries and modules are by default installed in the raspberry pi 4. If you are missing any of these in your pi you can install them using

```
sudo apt install python-package_name
or  
sudo apt install python3-package_name if using Python3.
```

 Else, you can use

 ```
 pip install python-package_name or sudo pip3 install python-package_name if using Python3.
```
 Pip is installed on the raspberry pi OS by default but if it is not installed then
 
 ```
 sudo apt install python-pip.
 ```

Import board - This module is used in LCD.py and main.py in our code folder of the github repository. The board module contains constants for the pins on a specific board. The board module in CircuitPython for a different board will have different constants specific to that board. The user does not have to tell CircuitPython what board it is running on, it knows. The board module is the safest, most reliable way to use your board's pins. It allows you to not worry about what MCU pins the board pins are connected to.

Import digitalio - This module is used in LCD.py in our code folder of the github repository. The digitalio module contains classes to provide access to basic digital IO.

Import adafruit_character_lcd.character_lcd as characterlcd - This module is used in LCD.py in our code folder of the github repository. Module for interfacing with monochromatic character LCDs.

Import adafruit_ina260 - This library is used in calc_sensor_values.py, check_sensors.py, and main.py in our git repository. On supported GNU/Linux systems like the Raspberry Pi, you can install the driver locally from PyPI. To install this driver for current users use: pip3 install adafruit-circuitpython-ina260 or if that doesn’t work install it system-wide by using: sudo pip3 install adafruit-circuitpython-ina260.

From csv import writer - This library is used in csv_code.py in our code folder of the github repository. The csv module implements classes to read and write tabular data in CSV format. In this case we imported only the write() method from the module. It returns a writer object responsible for converting the user’s data into delimited strings on the given file-like object. A CSV file can be any object with a write() method.

From time import sleep - This module is used in fsm.py and main.py in our code folder of the github repository. The time module has several functions for time-related tasks but the focus is only on the sleep() method from the timer module. The sleep() function suspends (waits) execution of the current thread for a given number of seconds.

Import time - This library is used in the main.py in our code folder of the github repository. The module provides several time related functions.

Import RPi.GPIO as GPIO - This library is used in the main.py in our code folder of the github repository. It provides basic interactions with the GPIO pins, but no implementation of any connection protocol yet.

Import csv - The csv module is used in the plot_csv.py of our code folder of the github repository. The csv module implements classes to read and write tabular data in CSV format.

Import matplotlib.pyplot as plt - This library is used in the plot_csv.py of our code folder of the github repository. The matplotlib.pyplot is a collection of command style functions that make matplotlib work like MATLAB. Each pyplot function makes some change to a figure: e.g., creates a figure, creates a plotting area in a figure, plots some lines in a plotting area, decorates the plot with labels, etc. In matplotlib.pyplot various states are preserved across function calls, so that it keeps track of things like the current figure and plotting area, and the plotting functions are directed to the current axes.
