"""
Main File for EP Band embedded code
Authors: Taylor Okel, Andrew Albert, Brandon Poplstein
"""

#import serial
from Pulse import PulseController
from Motion import MotionController
from Bluetooth import BluetoothController

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
