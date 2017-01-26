"""
The Motion (accelerometer && gyro) controller.
"""

import read_word_2c from I2C.py

class MotionController(object):
    """docstring for ."""

    ADDRESS = 0x68 # TODO: actual address

    X_addr = 0x43
    Y_addr = 0x45
    Z_addr = 0x47

    X = 0
    X_scl = 0
    Y = 0
    Y_scl = 0
    Z = 0
    Z_scl = 0

    scl_factor = 16384.0

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
        return math.sqrt((a*a)+(b*b))

    def get_y_rotation(x,y,z):
        radians = math.atan2(x, dist(y,z))
        return -math.degrees(radians)

    def get_x_rotation(x,y,z):
        radians = math.atan2(y, dist(x,z))
        return math.degrees

    def read():
        X = read_word_2c(X_addr)
        X_scl = X / scl_factor
        Y = read_word_2c(Y_addr)
        Y_scl = Y / scl_factor
        Z = read_word_2c(Z_addr)
        Z_scl = Z / scl_factor
        return None

    
