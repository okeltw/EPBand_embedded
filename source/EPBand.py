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
while 1:
    #clear the screen.
    print(chr(27) + "[2J")
    
    # Tell Motion Controller to read the sensor data
    MC.read()

    # Use the motion controller object to access the data.
    # Display for user to see.
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
    
    # sleep to give time for the screen to render. We also don't need instantaneous data, so let's not stress the pi.
    time.sleep(1)
