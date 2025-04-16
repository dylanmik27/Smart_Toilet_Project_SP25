#Legacy code that remnains from the servo development, utilized to implement main.py
#Code is not ran when device is operated, and only remains for documentation

from machine import Pin
from utime import sleep
import Servo_Control
#print("starting code")
#momentary switch connected between pin 15 and ground
#Servo_Control.test_move()
#print("test completed")
# initialize pin 20 as input w/ pull up resistor
button = Pin(15, Pin.IN, Pin.PULL_UP)

#initialize initial condition for assembly
Servo_Control.close_servo()
while button.value() != 0:
    continue
#print("button")
#loop for test
#Servo_Control.open_servo()
#Servo_Control.close_servo()

while True:
    if button.value() == 0:  # pressed
        #print("button")
        #print(Servo_Control.is_open)
        if Servo_Control.get_open() == True: 
            Servo_Control.close_servo()
        else:
            Servo_Control.open_servo()
        sleep(0.1)  # debounce