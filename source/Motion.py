"""
The Motion (accelerometer && gyro) controller.
"""

from I2C import *
import math

class MotionController(object):
    """docstring for ."""

    # Base address for the data
    ADDRESS = 0x68

    # Address for the powermanagement. Use 1 to wake from sleep. (2 is sleep?? Unconfirmed)
    power_mgmt_1 = 0x6b
    power_mgmt_2 = 0x6c

    # Offsets for the data
    X_accel_addr = 0x3b
    Y_accel_addr = 0x3d
    Z_accel_addr = 0x3f

    X_gryo_addr = 0x43
    Y_gyro_addr = 0x45
    Z_gyro_addr = 0x47

    # Initialize variables
    X_accel = 0
    X_accel_scl = 0
    X_gyro = 0
    X_gyro_scl = 0
    
    Y_accel = 0
    Y_accel_scl = 0
    Y_gyro = 0
    Y_gyro_scl = 0

    Z_accel = 0
    Z_accel_scl = 0
    Z_gyro = 0
    Z_gyro_scl = 0

    accel_scl = 16384.0
    gyro_scl = 131.0

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

    # Basic Math Functions. Self Explanatory.
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
        """
        Use the addresses above to collect and store MPU data
        """
        
        # X Accelerometer
        self.X_accel = read_word_2c(self.ADDRESS, self.X_accel_addr)
        self.X_accel_scl = self.X_accel / self.accel_scl

        # X Gyroscope
        self.X_gyro = read_word_2c(self.ADDRESS, self.X_gryo_addr)
        self.X_gyro_scl = self.X_gyro / self.gyro_scl

        # Y accelerometer
        self.Y_accel = read_word_2c(self.ADDRESS, self.Y_accel_addr)
        self.Y_accel_scl = self.Y_accel / self.accel_scl

        # Y Gyroscope
        self.Y_gyro = read_word_2c(self.ADDRESS, self.Y_gyro_addr)
        self.Y_gyro_scl = self.Y_gyro / self.gyro_scl

        # Z Accelerometer
        self.Z_accel = read_word_2c(self.ADDRESS, self.Z_accel_addr)
        self.Z_accel_scl = self.Z_accel / self.accel_scl

        # Z Gyroscope
        self.Z_gyro = read_word_2c(self.ADDRESS, self.Z_gyro_addr)
        self.Z_gyro_scl = self.Z_gyro / self.gyro_scl
        
        return None

    def wakeup(self):
        """
        Write the active power management state to MPU
        """
        write_byte(self.ADDRESS, self.power_mgmt_1)
