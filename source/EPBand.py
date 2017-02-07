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

while 1:
    print(chr(27) + "[2J")
    MC.read()
    print("acceleration X :", MC.X, " scaled: ", MC.X_scl)
    print("acceleration Y :", MC.Y, " scaled: ", MC.Y_scl)
    print("acceleration Z :", MC.Z, " scaled: ", MC.Z_scl)

    print("Rotation X: ", MC.get_x_rotation(MC.X_scl, MC.Y_scl, MC.Z_scl))
    print("Rotation Y: ", MC.get_y_rotation(MC.X_scl, MC.Y_scl, MC.Z_scl))
    print("Rotation Z: ", MC.get_z_rotation(MC.X_scl, MC.Y_scl, MC.Z_scl))
    time.sleep(0.5)
