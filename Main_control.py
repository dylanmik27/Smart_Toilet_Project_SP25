from machine import Pin
from utime import sleep
import Servo_Control
print("starting code")
#momentary switch connected between pin 20 and ground

# initialize pin 20 as input w/ pull up resistor
button = Pin(20, Pin.IN, Pin.PULL_UP)

#initialize initial condition for assembly
Servo_Control.close_servo()
while button.value() != 0:
    continue

#loop for test
while True:
    if button.value() == 0:  # pressed
        if Servo_Control.get_open() == True: 
            Servo_Control.close_servo()
        else:
            Servo_Control.open_servo()
        sleep(0.1)  # debounce