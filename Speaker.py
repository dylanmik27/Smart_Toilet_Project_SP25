from machine import Pin, PWM
from time import sleep
speaker = PWM(Pin(2))
def play_tone(frequency, duration):
    if frequency == 0:
        speaker.duty_u16(0)
    else:
        speaker.duty_u16(1000)
        speaker.freq(frequency)
    sleep(duration)
    speaker.duty_u16(0) 

# def jingle():
#     while True: 
#         play_tone(100) 
#         sleep(0.5) 
#         off() 
#         sleep(1)
# jingle()