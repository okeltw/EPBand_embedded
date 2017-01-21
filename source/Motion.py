"""
The Motion (accelerometer && gyro) controller.
"""

class MotionController(object):
    """docstring for ."""

    ADDRESS = 0x00 # TODO: actual address

    def __init__(self):
        print("Initializing Motion...")
        self.connect()
        print("Connected")

    def connect(self):
        print("Attempting connection...")

        if(False):
            raise ConnectionError("Failed to connect to Motion Sensor")
        # TODO
