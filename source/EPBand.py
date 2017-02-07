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

    print("Gyro Data")
    print("---------")

    print("Gyro X: ", MC.X_gyro, " scaled:", MC.X_gyro_scl)
    print("Gyro Y: ", MC.Y_gyro, " scaled:", MC.Y_gyro_scl)
    print("Gyro Z: ", MC.Z_gyro, " scaled:", MC.Z_gyro_scl)

    print("Accelerometer Data")
    print("------------------")
    print("acceleration X :", MC.X_accel, " scaled: ", MC.X_accel_scl)
    print("acceleration Y :", MC.Y_accel, " scaled: ", MC.Y_accel_scl)
    print("acceleration Z :", MC.Z_accel, " scaled: ", MC.Z_accel_scl)

    print("Rotation X: ", MC.get_x_rotation(MC.X_accel_scl, MC.Y_accel_scl, MC.Z_accel_scl))
    print("Rotation Y: ", MC.get_y_rotation(MC.X_accel_scl, MC.Y_accel_scl, MC.Z_accel_scl))
    print("Rotation Z: ", MC.get_z_rotation(MC.X_accel_scl, MC.Y_accel_scl, MC.Z_accel_scl))
    time.sleep(1)
