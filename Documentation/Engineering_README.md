# Overview of Monitoring system

The current state of the monitoring system has 4 functioning INA260 power sensors that are able to read voltage and current. In order for the sensors to work, you have to make sure that they are connected to a common ground and that it is connected to the ground of the pi. Otherwise, the sensors will not be able to work. Also, the code to write the data to the CSV restarts everytime you run the main.py, so just be conscious of that when recording data. 

# Overview of storage system

The current storage system utilizes four 400 F,  2.7 V supercapacitors connected in parallel, resulting in 1600 F of capacitance. When designing our system, we intended to discharge the capacitors to 0.5 V, resulting in about 1.1 Wh of energy storage. After assembling the system and conducting tests on the energy storage, we realized that the primary boost converter is not able to operate (and thus provide power to our load) when the voltage across the capacitors dropped below 1.8 V, resulting in a shallower depth of discharge. The energy capacity of the capacitors dropped to  0.18 Wh of storage as a condition for operation for the EDS. Nonetheless, we are able to provide a runtime of about 20 minutes, which is just enough for demo purposes. We suggest using supercapacitors with higher voltage rating and more importantly more capacitance in order to support the system for longer. 

# Overview of supercapacitor charger

The supercapacitor charger implemented in our system is the TI BQ25173, which is a linear regulator. 

# Overview of the EDS

We have not been able to obtain an EDS film or power supply. However, we are using a simulated EDS load, a resistor network that can safely consume about the same amount of power as the EDS. To incorporate the EDS into the system, simply disconnect the resistor bank, and replace it with the EDS power supply. The power supply should turn on as soon as a voltage of 12 V is applied across its input terminals. Be careful since the power supply outputs 1.3kV three phase square wave which could shock you if you are not careful. Connect the power supply to the three EDS electrodes, and the system should be able to operate properly.

# Overview of Physical Chassis

To house our circuit, we opted to use an igloo beach cooler adapted into a housing unit. After holes were drilled into the top and side of the cooler, connections were made in and out of the chassis using wires which connect our solar panel mounted across the top lid, our central circuit held on a metal rack slotted into the inside of the cooler, and the Raspberry Pi running our software and UI located in a casing attached to the side of the cooler.

# Overview of Testing Setup

In order to utilize the circuit, you first have to ensure that the supercapacitors have enough charge to run the EDS. In our case, this is represented by a 12V DC dummy load which runs into a super capacitor bank. When charged, the user can flip a switch located on the side panel box, which can be used to deactivate or deactivate the dummy load. An LCD panel located next to this switch will then give the user information regarding the current and voltage of the circuit at various points, amongst other information, and this information can be cycled through by touching a button located next to it.
