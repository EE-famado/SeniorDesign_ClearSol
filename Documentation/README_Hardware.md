# Overview

In this overview, we describe the technical layout of our circuit as well as its operational behavior, in addition to the way in which it is incorporated and housed into our overall assembly. We have attached photos of the circuit layout, assembly, and graphs regarding the behavior of our circuit below.

# Circuit Description

![Solar Panel](/images/solarpanel1.png)

Solar panel specs

The solar panel we are using for the project is a 30W solar panel, with an optimum output voltage of 18.0V and an optimum output current of 1.67A. With the LED lamp we used to illuminate it, its performance was reduced, operating at roughly 2W at a voltage of 18.3V and current of 110mA. The solar panel should be placed underneath the LED lamp, or outside in sunlight. In its current configuration, the system is optimized for use with the solar panel underneath an LED lamp in close proximity.

![LED lamp](/images/LEDlamp2.png)

We are using a Phlizon PH-R15 grow lamp for our artificial light source. For our tests, it is turned to its highest setting, and placed roughly one foot above our solar panel.

# Buck Converter

[LM2596 Buck Controller](https://www.amazon.com/HiLetgo-Step-down-Converter-1-25-37V-Voltmeter/dp/B00LSEBYHU/)

The solar panel is connected to a buck converter at the input of our power system. This buck converter is utilized for two reasons. First, our supercapacitor charge controller has a maximum input voltage of 18V. Since our unloaded panel output voltage exceeds this, a buck converter is necessary to reduce the panel input to a manageable voltage for the controller. Second, because the controller uses a linear regulator, it becomes more inefficient as its input voltage increases. We want the input voltage to the charge controller to be as low as possible to reduce losses in the chip, reducing thermal limitations on performance and increasing efficiency.

So, the buck converter is set to output 3.5V. This is higher than the minimum input voltage of the charge controller, but still low to optimize performance.

# Supercapacitor Charge controller

[TI BQ25173](https://www.ti.com/product/BQ25173)

The supercap charge controller charges the supercapacitor bank up to a voltage of 2.7V. This controller has two configurable settings: the target charge voltage and the charge current. For our supercapacitor bank, which is a set of parallel 2.7V supercaps, the target voltage is set to 2.7V. The charge current setting is more complicated. While more conventional solar charge controllers feature MPPT capability, this controller has no such functionality. So, there is no way to dynamically adjust the charge current to get the most power given the incident light on the solar panel. If the charge current is set lower than ideal, the charge rate will be reduced. If the charge current is set higher than ideal, the solar panel voltage will be pulled low and the supercapacitors will not charge. Depending on expected operating conditions, the charge limit can be adjusted to prioritize reliability or charge rate. For the current prototype, the charge current was adjusted to get the most power out of the panel with our grow lamp.

For this design we are using this controller as installed on an evaluation board from Texas Instruments. There are two settings for charge current on the controller. A fixed 400mA, and an adjustable charge current from 15mA to 800mA. The charge current was tuned to be 370mA, which drew the most power from our panel before it started to be pulled low by too much load.

# Supercapacitors

[Kyocera AVX SCCY60B407SNB 400F Supercapacitors](https://www.mouser.com/ProductDetail/Kyocera-AVX/SCCY60B407SNB?qs=bAKSY%2FctAC5fL6o%2Fe157YA%3D%3D)

We are utilizing a bank of four 400F supercapacitors connected in parallel, for a total capacitance of 1600F. The main concern with this bank is a short circuit, which can result in very large discharge currents and dangerous conditions as a result. There are two main mitigations against this in the design. First, the supercapacitor terminals are covered to prevent shorts across the terminals. Second, the connection from the supercapacitor bank to the rest of the power system is fused with a 5A fast acting fuse.

# Relay

This is the primary control element placed in the power circuit. It connects the supercapacitor bank to the primary boost converter. This allows the whole load side of the system to be shut off when the EDS is not being used, increasing overall efficiency. A relay was chosen mainly for simplicity in interfacing with our Raspberry Pi. An option that could be implemented later on would be to instead turn on the primary boost converter directly. It has an enable pin, which could be connected to/controlled by the Raspberry Pi.

# Primary boost Converter

[TI TPS61022](https://www.mouser.com/new/texas-instruments/ti-tps61022-converters/?gclid=Cj0KCQjwma6TBhDIARIsAOKuANxVnfk3HlMo2V_M8QLFp7y296KK6AfBvFQMPAUdqdjZADcjVMwiP-IaAtI0EALw_wcB)

The primary boost converter connects to the supercapacitor bank, and boosts the supercapacitor voltage up to a consistent 5V output. An important thing to note is at what supercapacitor voltages the boost converter can operate. The boost converter only turns on when the supercapacitor voltage is greater than or equal to 1.8V. Once it turns on and starts to convert, it can operate down to a theoretical input voltage of 0.5V. (In practice, the converter shuts off around 0.8V.) So, in the course of regular operation, the supercapacitor voltage should be kept above 1.8V if immediate turn on is required. Otherwise, an operation scheme where the supercapacitors are allowed to discharge below 1.8V, and then recharge up to that point before subsequent operation, would need to be employed.

This converter, as used on our project, is implemented on an evaluation board from Texas Instruments. It is configured to have a constant output voltage of 5V.

# Secondary boost converter

[Boost converter](https://www.amazon.com/Aceirmc-Current-Converter-Adjustable-Regulator/dp/B082XQC2DS/)

The secondary boost converter connects to the output of the primary boost converter. Its purpose is to boost the 5V output from the primary boost converter up to the desired load voltage of 12V. It has an adjustable output voltage, and as such can be adjusted to suit a different load requirements if need be.

# Simulated EDS load

Since we did not have access to an actual EDS and accompanying power supply for this project, we constructed a bank of resistors to replicate the power draw of the EDS, to the best of our knowledge of its operation. The EDS draws 1.3W off of a 12V DC bus during operation, so we constructed a resistor bank of roughly 110 Ohms, with the capability to dissipate 1.3W safely. This bank is connected to the output of the secondary boost converter.

# Power Sensors

[INA260](https://www.adafruit.com/product/4226)

In order to accurately monitor the power flow within key elements of our system, we are implementing four INA 260 power sensors. These power sensors are connected in series with the elements that it monitors, measuring the voltage of with respect to a common ground. It also measures the current going through it, enabling us to obtain power measurements. We have placed the sensors in the following locations: at the output of the solar panel, at the input and output of the supercapacitors (allowing us to monitor charge and discharge) and at the simulated EDS load. The power sensors then send the measurement information to the raspberry pi, that then displays voltage and current measurement to our LCD screen located on the user input box. Output measurements of different power sensors can be cycled through the display by pressing the yellow button next to the display.

# Raspberry Pi 4 Microcontroller

We implement a Raspberry Pi 4 as a microcontroller for monitoring and control purposes. Data from the power sensors are sent to the Raspberry Pi that would display the measurements on the LCD screen located on the user input box. The Raspberry Pi also controls the relay switch which activates the EDS load. The EDS can be activated manually through a switch on the user input box. Since the microcontroller consumes a significant amount of power, and has to be operational all the time, we are powering it through the wall socket. Due to budget limitation, the storage system does not store enough energy to maintain the microcontroller powered on. In a future implementation of our project, we intend to use a low power microcontroller, such as the [STM32F070](https://www.digikey.com/en/products/detail/stmicroelectronics/NUCLEO-F070RB/5047473?s=N4IgTCBcDaIMoBUCyBmMAxADAdkyAugL5A), alongside a larger capacitance bank that exceeds the budget allowance, in order to obtain a self sufficient system.

![System](/images/systemoverview3.png)

# System Activation

Starting the system is actually very easy. So long as there is an appropriate level of charge in our supercapacitors to run our raspberry pi, the front LED panel will be functional and thus allow for the user to both view internal behaviors and activate/deactivate the 12 V EDS load via the mechanical switch on the front of the user panel, simulating EDS film functionality.

In the case the supercapacitors have completely lost all charge, the system will not be usable again until enough sunlight has been absorbed by the solar panel to power our raspberry pi, bringing the system back online. Once online, all information regarding the circuit and its behavior will be demonstrated on our LCD screen, and information on this screen can be swapped through using the button on the front panel, with each click cycling through a piece of information.

# Housing Description

The actual containment unit of the circuit is built into a small igloo beach cooler which we have modified to house our components. We specifically wanted to use a beach cooler as the unit is already built to be toted around with wheels and a handle, and has insulative properties which would theoretically protect the sensitive electronic components inside from both extreme weather and temperature conditions as well as the fairly extreme amounts of martian dust that would be encountered by the externals of the assembly.

To adapt our cooler to its new function, holes were drilled through the top door of the cooler, and wooden rails were used to sandwich this door. Nails were then driven through the top central holes to bite them together, rendering us with a ‘rail system’ which we could attach our solar panel to. The panel was when mounted onto a hinge, which was screwed into the physical rail, allowing for a tilt to be applied to the panel and to thus measure energy changes in relation to the angle and positioning of the sun. In order to keep the panel at these different angles, wooden ‘teeth’ were connected to the rail so that a kickstand coming out of the panel can seat into them. The DC wire from the panel then runs through a hole milled in the door so that it can connect to the circuit.

![Cooler](/images/hardwaremount4.png)

On the inside of the housing, what was formerly a metal paper rack was modified in order to be able to house the completed circuit. In order to prevent any form of accidental conduction between the circuit and the metal, a piece of plexiglass was measured and cut in order to slide into the rack. The individual pieces of the circuit are then mounted to this using velcro. Wires from this circuit make connections to the solar panel itself as well as the user interface located at the front of the cooler. As a final component of the metal racking, holes were milled into the tops so that they can be used as handles to theoretically pull out and service the circuit while mounted on the racking system. The tape is to prevent the user from cutting themselves on the sharp edges left by the saw used to cut them open.

The last major component of the assembly is the user IO panel. The panel, which connects to the interior of the cooler via a 1 inch diameter milled hole, houses an LCD screen used to demonstrate information regarding the circuit behavior to the user, as well as 2 LED’s, a button to cycle settings, and lastly a mechanical switch to activate or deactivate our dummy 12v load. Note however the buttons, although installed, are ultimately nonfunctional as this is what was available in the lab. Theoretically, if one wanted to wire them up to demonstrate behavior it would be fairly easy, we just chose not to waste the power on it. Lastly, the wiring for all of these components is connected to the raspberry pi located inside that UI box, with the pi being connected to our interior circuit through the previously mentioned 1inch diameter hole.
