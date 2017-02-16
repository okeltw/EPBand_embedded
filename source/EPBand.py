"""
Main File for EP Band embedded code
Authors: Taylor Okel, Andrew Albert, Brandon Poplstein
"""

#import smbus
#from Pulse import PulseController
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
    # Tell Motion Controller to read the sensor data

    if counter < 10:
        counter += 10
    else:
        MC.printall()
        MC.clear()

    MC.read()

    time.sleep(0.1)
