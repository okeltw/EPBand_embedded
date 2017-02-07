"""
The Motion (accelerometer && gyro) controller.
"""

from I2C import *
import math

class MotionController(object):
    """docstring for ."""

    ADDRESS = 0x68 # TODO: actual address

    power_mgmt_1 = 0x6b
    power_mgmt_2 = 0x6c

    X_addr = 0x43
    Y_addr = 0x45
    Z_addr = 0x47

    X = 0
    X_scl = 0
    Y = 0
    Y_scl = 0
    Z = 0
    Z_scl = 0

    scl_factor = 163.0

    def __init__(self):
        print("Initializing Motion...")
        self.connect()
        print("Connected")
       

    def connect(self):
        print("Attempting connection...")
        self.wakeup()

        if(False):
            raise ConnectionError("Failed to connect to Motion Sensor")
        elif(False):
            print("Connected to " + ADDRESS)
        # TODO

    def dist(self, a, b):
        return math.sqrt((a*a)+(b*b))

    def get_y_rotation(self, x,y,z):
        radians = math.atan2(x, self.dist(y,z))
        return -math.degrees(radians)

    def get_x_rotation(self, x,y,z):
        radians = math.atan2(y, self.dist(x,z))
        return math.degrees(radians)

    def get_z_rotation(self, x,y,z):
        radians = math.atan2(z, self.dist(x,y))
        return math.degrees(radians)

    def read(self):
        self.X = read_word_2c(self.ADDRESS, self.X_addr)
        self.X_scl = self.X / self.scl_factor
        self.Y = read_word_2c(self.ADDRESS, self.Y_addr)
        self.Y_scl = self.Y / self.scl_factor
        self.Z = read_word_2c(self.ADDRESS, self.Z_addr)
        self.Z_scl = self.Z / self.scl_factor
        return None

    def wakeup(self):
        write_byte(self.ADDRESS, self.power_mgmt_1)
