from machine import Pin, PWM
from time import sleep
speaker = PWM(Pin(2))
melody = [
    (440, 0.15), (660, 0.15), (880, 0.2), (660, 0.15),
        (440, 0.2), (550, 0.15), (660, 0.25)
    ]
def play_tone(frequency, duration):
    if frequency == 0:
        speaker.duty_u16(0)
    else:
        speaker.duty_u16(2000)
        speaker.freq(frequency)
    sleep(duration)
    speaker.duty_u16(0) 

def jingle():
    for note, duration in melody:
        play_tone(note, duration)
        sleep(0.05)  # Short pause between notes
jingle()