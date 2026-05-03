# Task-.2GUI
Embedded Systems Development  Task 5.2C Adding PWM and a GUI slider to 5.1P

GUI-Based Light Intensity Control using PWM
Overview

This project extends Task 5.1P by introducing Pulse Width Modulation (PWM) to control the brightness of an LED using a Graphical User Interface (GUI). The system allows the user to select different rooms and adjust the light intensity of the living room using a slider.

How PWM Works

Pulse Width Modulation (PWM) controls the brightness of an LED by rapidly switching it ON and OFF. The proportion of time the signal stays ON which is known as the duty cycle determines the perceived brightness.
0% duty cycle = LED OFF
50% duty cycle = Medium brightness
100% duty cycle = Full brightness
In this project, PWM is applied to the living room LED to allow dynamic brightness control via a GUI slider.

Wokwi Simulation (Proof of Concept)

The PWM functionality was first tested using a Wokwi simulation with a single LED. This served as a proof of concept before implementing the system on the actual Raspberry Pi hardware.
Wokwi simulation screenshot below:

![image alt](https://github.com/kuriajeremy/Task-.2GUI/blob/3e6cd8b26c43654deeeaddb66692ca9b5afc8a86/wokwi%20sim.png)

The simulation code used in Wokwi is also included in this repository.
Hardware Requirements

1.	Raspberry Pi (with OS installed and VNC enabled)
2.	Breadboard
3.	3 × LEDs
4.	3 × Resistors (220Ω–330Ω)
5.	Jumper wires
6.	Power supply


Circuit Diagram (Schematic)
The diagram used in this project is a schematic representation created in Wokwi. It serves as a guide for wiring the physical components on the Raspberry Pi.
Wokwi schematic diagram below:

![image alt](https://github.com/kuriajeremy/Task-.2GUI/blob/3e6cd8b26c43654deeeaddb66692ca9b5afc8a86/wokwi%20schematic.png)

GPIO Pin Mapping
Room	GPIO Pin
Living Room (PWM)	GPIO18
Bathroom	GPIO15
Closet	GPIO16

Part 1: PWM Testing
Before integrating the GUI, PWM functionality was tested independently to ensure the LED brightness could be varied smoothly.
Steps:
1.	Create a Python file (pwm_test.py) in /home/pi/
2.	Paste PWM test code
3.	Run using python3 pwm_test.py
4.	Observe LED fading effect

Part 2: GUI Implementation
Steps:

6.	Create a file slider_gui.py in /home/pi/
7.	Paste the GUI code with slider
8.	Run using python3 slider_gui.py

GUI Features:

1.	Radio buttons for room selection
2.	Slider to control living room brightness
3.	Exit button for safe shutdown

System Behavior

1.	Living room LED brightness changes with slider
2.	Other LEDs operate as ON/OFF
3.	Only one room is active at a time
4.	Safe exit cleans GPIO pins

