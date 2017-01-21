"""
The Motion (accelerometer && gyro) controller.
"""

class MotionController(object):
    """docstring for ."""

    ADDRESS = 0x00 # TODO: actual address

    debug = False

    def __init__(self, dbug):
        print("Initializing Motion...")
        self.connect()
        print("Connected")
        debug = dbug

    def connect(self):
        print("Attempting connection...")

        if(False):
            raise ConnectionError("Failed to connect to Motion Sensor")
        elif(debug)
            print("Connected to " + ADDRESS)
        # TODO
