"""
The Motion (accelerometer && gyro) controller.
"""

import I2C

class MotionController(object):
    """docstring for ."""

    ADDRESS = 0x68 # TODO: actual address
    def __init__(self):
        print("Initializing Motion...")
        self.connect()
        print("Connected")

    def connect(self):
        print("Attempting connection...")

        if(False):
            raise ConnectionError("Failed to connect to Motion Sensor")
        elif(False):
            print("Connected to " + ADDRESS)
        # TODO

