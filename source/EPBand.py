"""
Main File for EP Band embedded code
Authors: Taylor Okel, Andrew Albert, Brandon Poplstein
"""

import smbus
from Pulse import PulseController
from Motion import MotionController
from Bluetooth import BluetoothController
import sys
import time
from RPi.GPIO import GPIO

print('starting')

try:
    PC = PulseController()
    MC = MotionController()
    BC = BluetoothController()
except ConnectionError as error:
    print(error)
except Exception as error:
    print("An unknown error occured: ")
    print(error)
    quit()

channel = 0 #TODO

GPIO.setmode(GPIO.BOARD)
GPIO.setup(channel, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
#Spawn a new thread to monitor this gpio pin. will increment pulse_counter by 1 each rising edge.
GPIO.add_event_detect(channel, GPIO.RISING, callback=PC.Pulse_callback)

# main loop
counter = 0
while 1:
    # Send/Display data once a second
    if counter < 60:
        counter += 1
    else:
        counter = 0
        print(chr(27) + "[2J")
        MC.printall()
        print("\n\nBPM: " PC.Pulse_reading(6))
        MC.clear()
        PC.reset()

    # Tell Motion Controller to read the sensor data
    MC.read()

    # Don't overload the PI
    time.sleep(0.1)
