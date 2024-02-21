# Lab3
 Group 18's Lab3

This project is used to apply proportional control to an encoder-DC motor system through an interface between a PC and STM32 microcontroller.
This project contains the main.py, lab3.py, motor_driver.py, encoder_reader.py, and motor_control.py programs. As made previously, the module, motor_driver.py, creates the class "MotorDriver" which initializes the GPIO pins as PWM outputs for one motor and allows the PWM duty cycle to be set, and the module, encoder_reader.py, creates the class "Encoder" which initializes the timers/counters required for on motor encoder using provided channel pins and a timer/counter and allows the absolute position (accounting for overflow and underflow) to be read and zeroed. The module, motor_control.py, creates the class "MotorControl" which creates a proportional gain controller, allowing for PWM effort to be calculated and returned to be used by the motor based off of user input Kp and desired motor position. The program, main.py, is ran on the microcontroller and contains the three class modules to run the step response for motor position. The program, lab3.py, is ran on the PC and contains a GUI to input a Kp value for a step response to be ran and plotted.

The responses for Kp values that produced underdamped (Kp = 0.5), overdamped (Kp = 0.01), and well-damped (Kp = 0.025) can be seen below.
![Step_Responses](https://github.com/Cadre1/Lab3/assets/55156855/72065c72-d0cc-42c1-8597-2e8f926d0227)
