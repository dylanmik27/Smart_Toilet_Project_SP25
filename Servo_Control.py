from machine import Pin, PWM
from time import sleep
import Speaker

servo = PWM(Pin(0))     # the Pico PWM pin
servo_switch = Pin(1, Pin.OUT)
servo.freq(50) #per the mg995 datasheet 50hz
s_closed_angle = 30
s_open_angle = 120
is_open = False

#the duty cycle to open the servo given by formula: Duty = ((0.5 + (Angle / 90)) /20 )*100
def convert_angle(angle):
    percentage = ((0.5 + (angle / 90)) /20 )
    return int(percentage * (2**16 - 1))

servo_closed_val = int(convert_angle(s_closed_angle))
servo_open_val = int(convert_angle(s_open_angle))
print(servo_closed_val)
print(servo_open_val)



def close_servo():
    global is_open
    servo_switch.value(1)
    servo.duty_u16(servo_closed_val)
    Speaker.jingle()
    sleep(2) #wait for servo to move
    is_open = False
    servo.deinit
    servo_switch.value(0)
    return

def open_servo():
    global is_open
    servo_switch.value(1)
    servo.duty_u16(servo_open_val)
    Speaker.jingle()
    sleep(2) #wait for servo to move
    is_open = True
    servo.deinit
    servo_switch.value(0)
    return

def get_open():
    return is_open

#arbitrary test using defined values
def test_move():
    servo.duty_u16(6371)  
    sleep(2)                          
    servo.duty_u16(2730)  
    sleep(5)
    servo.deinit()           
    return