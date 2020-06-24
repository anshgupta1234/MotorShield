import PiMotor
import time
import RPi.GPIO as GPIO
import keyboard

#Name of Individual MOTORS 
m1 = PiMotor.Motor("MOTOR1",1)
m2 = PiMotor.Motor("MOTOR2",1)

#To drive all motors together
motorAll = PiMotor.LinkedMotors(m1,m2)

#Names for Individual Arrows
ab = PiMotor.Arrow(1)
al = PiMotor.Arrow(2)
af = PiMotor.Arrow(3) 
ar = PiMotor.Arrow(4)

try:
    while True:
        if keyboard.is_pressed('w'):
            af.on()
            motorAll.forward(100)
            time.sleep(3)
            