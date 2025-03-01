from machine import Pin, PWM
from time import sleep

servo = PWM(Pin(0))     # the Pico PWM pin
servo.freq(50)
while(True):
    servo.duty_u16(6700)   # sets servo to about 150 deg
    sleep(5)                           # the 2 secs is to allow the servo to rotate
    servo.duty_u16(3200)  # sets servo to about 30 deg
    sleep(10)
    servo.deinit()                 # stops the PWM signal - 

# work in progress code, unnecessary below
# from machine import Pin, PWM
# class Servo:
#     # these defaults work for the standard TowerPro SG90
#     __servo_pwm_freq = 50
#     __min_u16_duty = 1640 + 400 # offset for correction
#     __max_u16_duty = 7864 - 35  # offset for correction
#     min_angle = -90
#     max_angle = 90    
#     current_angle = 0.001
    
    
#     def __init__(self, pin):
#         self.__initialise(pin)
        
        
#     def update_settings(self, servo_pwm_freq, min_u16_duty, max_u16_duty, min_angle, max_angle, pin):
#         self.__servo_pwm_freq = servo_pwm_freq
#         self.__min_u16_duty = min_u16_duty
#         self.__max_u16_duty = max_u16_duty
#         self.min_angle = min_angle
#         self.max_angle = max_angle
#         self.__initialise(pin)
        
        
#     def move(self, angle):
#         # round to 2 decimal places, so we have a chance of reducing unwanted servo adjustments
#         angle = round(angle, 2)
#         # do we need to move?
#         if angle == self.current_angle:
#             return
#         self.current_angle = angle
#         # calculate the new duty cycle and move the motor
#         duty_u16 = self.__angle_to_u16_duty(angle)        
#         self.__motor.duty_u16(duty_u16)
        
        
#     def __angle_to_u16_duty(self, angle):
#         return int((angle - self.min_angle) * self.__angle_conversion_factor) + self.__min_u16_duty
    
    
#     def __initialise(self, pin):
#         self.current_angle = -0.001
#         self.__angle_conversion_factor = (self.__max_u16_duty - self.__min_u16_duty) / (self.max_angle - self.min_angle)
#         self.__motor = PWM(Pin(pin))
#         self.__motor.freq(self.__servo_pwm_freq)



# # from machine import Pin
# # from utime import sleep
# # import time, math
# # import machine
# # pin22 = machine.Pin(22)
# # seat_servo = machine.PWM(pin22)

# # seat_servo.freq(50)
# # seat_servo.duty_u16(9000)



# # pin = Pin("LED", Pin.OUT)

# # print("LED starts flashing...")
# # while True:
# #     try:
# #         pin.toggle()
# #         sleep(1) # sleep 1sec
# #     except KeyboardInterrupt:
# #         break
# # pin.off()
# # print("Finished.")



# #set up servo using pin 29
# toiletSeat = Servo(29)

# toiletSeat.move(45)
# toiletSeat.move(90)
# print("finished")