from machine import Pin, PWM
from time import sleep

servo = PWM(Pin(29))     # the Pico PWM pin
servo.freq(50) #per the mg995 datasheet 50hz
s_closed_angle = 30
s_open_angle = 130
is_open = False

#the duty cycle to open the servo given by formula: Duty = ((0.5 + (Angle / 90)) /20 )*100
def convert_angle(angle):
    percentage = ((0.5 + (angle / 90)) /20 )*100
    return percentage * (2^16 - 1)

servo_closed_val =  convert_angle(s_closed_angle)
servo_open_val = convert_angle(s_open_angle)



def close_servo():
    servo.duty_u16(servo_closed_val)
    sleep(2) #wait for servo to move
    is_open = False

def open_servo():
    servo.duty_u16(servo_open_val)
    sleep(2) #wait for servo to move
    is_open = True

def get_open():
    return is_open