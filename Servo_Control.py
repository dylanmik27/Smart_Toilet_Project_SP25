#This module manages servo actuation using PWM on a microcontroller. 
# It initializes a servo output and a control switch, sets the PWM frequency to 50Hz (Per the MG995 datasheet), 
# and calculates duty cycle values for specified open and closed angles using a conversion function. 
# The module provides functions to open and close the servo—which also trigger a short jingle for audio feedback
# and maintains a state flag to track the servo position. Additionally, it offers a test function to simulate movement.

#import necessary dependencies, and other modules designed to be implemented in this script
    #native machine dependencies
from machine import Pin, PWM
from time import sleep
    #developed modules
import Speaker

#initialize the pins where the servo and transistor are connected
servo = PWM(Pin(0))     # the Pico PWM pin
servo_switch = Pin(1, Pin.OUT)
#set servo PWM frequency to 50Hz
servo.freq(50) #per the mg995 datasheet 50hz
#set two angles 90 degrees apart, these for chose for adjustability in each direction, and only are necessary when syncronizing the servo arm
s_closed_angle = 120
s_open_angle = 30
#create a global flag to determine state of servo.
is_open = False

#the duty cycle to open the servo given by formula: Duty = ((0.5 + (Angle / 90)) /20 )*100
def convert_angle(angle):
    percentage = ((0.5 + (angle / 90)) /20 )
    return int(percentage * (2**16 - 1))

#store and print duty cycle values
servo_closed_val = int(convert_angle(s_closed_angle))
servo_open_val = int(convert_angle(s_open_angle))
print(servo_closed_val)
print(servo_open_val)


#this function closes the servo
def close_servo():
    global is_open
    #allow current to flow through transistor
    servo_switch.value(1)
    #move servo to close
    servo.duty_u16(servo_closed_val)
    #play jingle
    Speaker.jingle()
    sleep(2) #wait for servo to move
    #set global variable to closed
    is_open = False
    #stop PWM and servo voltage
    servo.deinit
    servo_switch.value(0)
    return

def open_servo():
    global is_open
    #allow current to flow through transistor
    servo_switch.value(1)
    #move servo to open
    servo.duty_u16(servo_open_val)
    #play jingle
    Speaker.jingle()
    sleep(2) #wait for servo to move
     #set global variable to open
    is_open = True
        #stop PWM and servo voltage
    servo.deinit
    servo_switch.value(0)
    return

#return state of is_open
def get_open():
    return is_open

#legacy test code
#arbitrary test using defined values
def test_move():
    servo.duty_u16(6371)  
    sleep(2)                          
    servo.duty_u16(2730)  
    sleep(5)
    servo.deinit()           
    return