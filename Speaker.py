

#import necessary dependencies, and other modules designed to be implemented in this script
    #native machine dependencies
from machine import Pin, PWM
from time import sleep

#create PWM output for Speaker pin
speaker = PWM(Pin(2))
#store melodic series of tuple notes consisting of frequency and time playedddddddddddd
melody = [
    (440, 0.15), (660, 0.15), (880, 0.2), (660, 0.15),
        (440, 0.2), (550, 0.15), (660, 0.25)
    ]

#play a single tone givena frequency and duration
def play_tone(frequency, duration):
    #off / make no sound
    if frequency == 0:
        speaker.duty_u16(0)
    #initialize PWM output and change frequency.
    else:
        speaker.duty_u16(2000)
        speaker.freq(frequency)
    #play note for duration seconds
    sleep(duration)
    #off / make no sound
    speaker.duty_u16(0) 

#Take the List of tuples and play each tone, with a small gap between each.
def jingle():
    for note, duration in melody:
        play_tone(note, duration)
        sleep(0.05)  # Short pause between notes

#call jingle to verify function, but also so when module is loaded at boot up function is confirmedddd
jingle()