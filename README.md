# stm8flash_script
Programming multiple STM8S001J3 MCUs at once using multiple STLinks with Python3 script

Project based on a Raspberry Pi 4 Computer (Model B) to upload programs to the STM8S001J3.
It is possible to add more microcontrollers and ST-Links as needed.

Components for the project:
- Raspberry Pi 4
- STM8S001J3
- ST-Link
- USB Hub
- LED diodes
- Breadboard wires
- Logic Level Converter

How to use it
Each microcontroller is connected to an ST-Link, and then the ST-Link is plugged into the USB Hub. The USB Hub is connected to the Raspberry Pi via USB communication.
LED diodes are used to signal whether the code has been successfully programmed. The LEDs need to be connected to the Raspberry Pi.
However, the LEDs and the Raspberry Pi cannot be directly connected due to different power voltage levels. This issue is resolved using a logic level converter. 
Once everything is connected, a previously written Python script is run in the terminal, which searches for the serial numbers of the ST-Links.
After the serial numbers are found, the program to be uploaded to the microcontroller is sent to the corresponding serial numbers. 
If the code is successfully programmed, the LED will light up green.

