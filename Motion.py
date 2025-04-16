#This module sets up a PIR sensor on a microcontroller by configuring a specific pin as input. 
# It maintains a Boolean flag to indicate whether motion is detected and defines a function to update this flag based on the sensor's digital state. 
# Commented-out test code demonstrates how the function could be used in a loop for continuous monitoring.

#import necessary dependencies
from machine import Pin
from time import sleep

# Define the PIR sensor input pin
motion = Pin(22, Pin.IN)

# Flags to indicate motion detection state
motion_detected = False

# Callback function to handle motion detection
def detect_motion():
    global motion_detected
    if motion.value() == 1:  # Rising edge (motion detected)
        motion_detected = True
    else:  # Falling edge (motion stopped)
        motion_detected = False


#Test code utilized in file to verify function of PIR sensor
    # while True:
    #     detect_motion()
    #     if motion_detected:
    #         print("Motion detected!")
    #     else: 
    #         print("oh no")
    #     sleep(1)  # Main loop delay

