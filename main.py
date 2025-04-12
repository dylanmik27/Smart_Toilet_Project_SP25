print("import")
from machine import Pin
import time
import Servo_Control
import Speaker



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

seat_switch = Pin(15, Pin.IN, Pin.PULL_UP)

print("loaded")
Servo_Control.open_servo()
Servo_Control.close_servo()
while True:
    detect_motion()
    if motion_detected:
        print("hey")
        Servo_Control.open_servo()
        while seat_switch.value() != 0:
            time.sleep(0.1)
        while seat_switch.value() == 0:
            time.sleep(0.1)
        time.sleep(60)
        Servo_Control.close_servo()
        time.sleep(60)
    else:
        time.sleep(1)