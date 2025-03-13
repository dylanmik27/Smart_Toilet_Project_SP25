from machine import Pin, PWM
from time import sleep
speaker = PWM(Pin(2))
melody = [
        (262, 0.01), (294, 0.01), (330, 0.01), (262, 0.01),
        (262, 0.01), (294, 0.01), (330, 0.01), (262, 0.01),
        (330, 0.01), (349, 0.01), (392, 0.02),
        (330, 0.01), (349, 0.01), (392, 0.02)
    ]
def play_tone(frequency, duration):
    if frequency == 0:
        speaker.duty_u16(0)
    else:
        speaker.duty_u16(1000)
        speaker.freq(frequency)
    sleep(duration)
    speaker.duty_u16(0) 

def jingle():
    for note, duration in melody:
        play_tone(note, duration)
        sleep(0.05)  # Short pause between notes
jingle()