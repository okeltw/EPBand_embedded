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

    def dist(a,b):
        """
        Calculate distance of two points

        Doctests:
        >>> dist(0,0)
        0
        >>> dist(666,13.37) #From Tommy, bc he is the devil.
        666.1341883584718
        """
        return math.sqrt((a*a)+(b*b))
