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

# main loop
counter = 0
while 1:
    # Send/Display data once a second
    if counter < 10:
        counter += 1
    else:
        counter = 0
        print(chr(27) + "[2J")
        MC.printall()
        MC.clear()

    # Tell Motion Controller to read the sensor data
    MC.read()

    # Don't overload the PI
    time.sleep(0.1)
