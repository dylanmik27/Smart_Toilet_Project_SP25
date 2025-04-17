#This main.py script serves as the central controller for the automated toilet seat project. 
# It integrates inputs from both a PIR sensor and a seat pressure switch with actuator control through a servo and provides audio feedback via a speaker. 
# Upon startup, the script plays a series of tones and performs an initial test by opening and closing the seat. 
# During operation, it continuously polls the PIR sensor, and once motion is detected, 
# it triggers the servo to open the seat and then waits for user interaction via the seat switch—first detecting when someone sits down and then when they stand up. 
# After these inputs, it plays another tone and incorporates delays before closing the seat. 
# In summary, this code orchestrates sensor readings, mechanical seat movements, and sound signals to provide a seamless, automated toilet seat experience.

#print message via UART to confirm proper connection
print("import")

#import necessary dependencies, and other modules designed to be implemented in this script
    #native machine dependencies
import network
import socket
from machine import Pin
import time
    #developed modules
import Servo_Control
import Motion
import Speaker

#network connection
SSID = 'Dylan Phone'
PASSWORD = 'temp1234'

wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(SSID, PASSWORD)
while not wlan.isconnected():
    time.sleep(0.5)
ip = wlan.ifconfig()[0]
print("Wi‑Fi IP:", ip)

#UI
html = """\
<!DOCTYPE html>
<html>
  <head><meta charset="utf-8"><title>Seat Control</title></head>
  <body style="text-align:center;padding:2rem;font-family:sans-serif">
    <h1>Seat Control</h1>
    <button onclick="fetch('/open')"
            style="font-size:1.2rem;padding:1rem 2rem;margin:.5rem;
                   background:#4CAF50;color:#fff;border:none;border-radius:.5rem">
      Open Seat
    </button>
    <button onclick="fetch('/close')"
            style="font-size:1.2rem;padding:1rem 2rem;margin:.5rem;
                   background:#F44336;color:#fff;border:none;border-radius:.5rem">
      Close Seat
    </button>
  </body>
</html>
"""

#server
addr = socket.getaddrinfo('0.0.0.0', 80)[0][-1]
s = socket.socket()
s.bind(addr)
s.listen(1)
s.setblocking(False)
print("Listening on", addr)

#create a input pin for the switch actuated by seat pressure
seat_switch = Pin(15, Pin.IN, Pin.PULL_UP)
#play initialize tones
Speaker.play_tone(660, 0.15)
Speaker.play_tone(880, 0.3)
#print message via UART to confirm proper series
print("loaded")
#test move
Servo_Control.open_servo()
Servo_Control.close_servo()

#Main Loop
while True:
    #html control
    try:
        cl, remote = s.accept()
        req = cl.recv(1024).decode()
        path = req.split(" ")[1]
        if path == "/open":
            Servo_Control.open_servo()
            Speaker.jingle()
            cl.send("HTTP/1.0 200 OK\r\n\r\nSeat opened")
        elif path == "/close":
            Servo_Control.close_servo()
            Speaker.jingle()
            cl.send("HTTP/1.0 200 OK\r\n\r\nSeat closed")
        else:
            cl.send("HTTP/1.0 200 OK\r\nContent-Type: text/html\r\n\r\n" + html)
        cl.close()
    except OSError:
        pass

    #PIR legacy code for self contained device
    #wait between detection
    time.sleep(1)
    Motion.detect_motion()
    if Motion.motion_detected:
        Servo_Control.open_servo()
        #while seat has not been sat on loop with time delay
        while seat_switch.value() != 0:
            time.sleep(0.1)
        #while seat is still sat on loop with time delay
        while seat_switch.value() == 0:
            time.sleep(0.1)
        #play tone to verify closing timer started
        Speaker.play_tone(440,.15)
        time.sleep(5)
        Servo_Control.close_servo()
        #wait until user has left, so PIR no longer experiences input
        time.sleep(5)
    else:
        time.sleep(1)