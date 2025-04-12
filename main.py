print("import")
from machine import Pin
import time
import Servo_Control
import Speaker
import Motion


seat_switch = Pin(15, Pin.IN, Pin.PULL_UP)

print("loaded")
Servo_Control.open_servo()
while True:
    Motion.detect_motion
    if Motion.motion_detected:
        Servo_Control.open_servo()
        Speaker.jingle()
        while seat_switch.value() != 0:
            time.sleep(0.1)
        while seat_switch.value() == 0:
            time.sleep(0.1)
        time.sleep(60)
        Servo_Control.close_servo()
        Speaker.jingle()
        time.sleep(60)