print("import")
from machine import Pin
import time
import Servo_Control
import Motion
import Speaker

seat_switch = Pin(15, Pin.IN, Pin.PULL_UP)
Speaker.play_tone(660, 0.15)
Speaker.play_tone(880, 0.3)
print("loaded")
Servo_Control.open_servo()
Servo_Control.close_servo()
while True:
    Motion.detect_motion()
    if Motion.motion_detected:
        Servo_Control.open_servo()
        while seat_switch.value() != 0:
            time.sleep(0.1)
        while seat_switch.value() == 0:
            time.sleep(0.1)
        Speaker.play_tone(440,.15)
        time.sleep(30)
        Servo_Control.close_servo()
        time.sleep(30)
    else:
        time.sleep(1)