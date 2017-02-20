"""
The Motion (accelerometer && gyro) controller.
"""

from I2C import *
import math

class MotionController(object):
    """docstring for ."""

    # Base address for the data
    ADDRESS = 0x68

    # Initialize variables
    AccelData = {"X": [], "Y": [], "Z": [], "X_scl": [], "Y_scl": [], "Z_scl": []}
    GyroData = {"X": [], "Y": [], "Z": [], "X_scl": [], "Y_scl": [], "Z_scl": []}

    accel_scl = 16384.0
    gyro_scl = 131.0

    def __init__(self):
        print("Initializing Motion...")
        self.connect()
        print("Connected")


    def connect(self):
        print("Attempting connection...")
        # Write the active power management state to MPU
        write_byte(self.ADDRESS, regs['Pwr Mgmt 1'], 0)

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

        val = read_word_2c(self.ADDRESS, regs['Accel X High'])
        self.AccelData["X"] += [val]
        self.AccelData["X_scl"] += [val / self.accel_scl ]

        val = read_word_2c(self.ADDRESS, regs['Accel Y High'])
        self.AccelData["Y"] += [val]
        self.AccelData["Y_scl"] += [val / self.accel_scl ]

        val = read_word_2c(self.ADDRESS, regs['Accel Z High'])
        self.AccelData["Z"] += [val]
        self.AccelData["Z_scl"] += [val / self.accel_scl ]

        val = read_word_2c(self.ADDRESS, regs['Gyro X High'])
        self.GyroData["X"] += [val]
        self.GyroData["X_scl"] += [val / self.gyro_scl ]

        val = read_word_2c(self.ADDRESS, regs['Gyro Y High'])
        self.GyroData["Y"] += [val]
        self.GyroData["Y_scl"] += [val / self.gyro_scl ]

        val = read_word_2c(self.ADDRESS, regs['Gyro Z High'])
        self.GyroData["Z"] += [val]
        self.GyroData["Z_scl"] += [val / self.gyro_scl ]

        return None

    def clear(self):
        """
        Reset dictionaries to empty lists.
        """
        self.AccelData = {"X": [], "Y": [], "Z": [], "X_scl": [], "Y_scl": [], "Z_scl": []}
        self.GyroData = {"X": [], "Y": [], "Z": [], "X_scl": [], "Y_scl": [], "Z_scl": []}
        return None

    def printall(self):
        print("Gyroscope:")
        print("----------")
        for d in ("X", "Y", "Z"):
            print("Gyro ", d, ":\n", self.GyroData[d])
            print("Gyro ", d, " Scaled:\n", self.GyroData[d + "_scl"])
            print()

        print("\nAccelerometer:")
        print("--------------")
        for d in ("X", "Y", "Z"):
            print("Accel ", d, ":\n", self.AccelData[d])
            print("Accel ", d, " Scaled:\n", self.AccelData[d + "_scl"])

    def SetSampleRate(self, value):
        write_byte(self.ADDRESS, reg['Sample Rate'], value)

    def GetSampleDivider(self):
        return read_byte(self.ADDRESS, reg['Sample Rate'])

    def GetSampleRate(self):
        div = self.GetSampleDivider()
        mask = 0b00000111 # Read only the last 3 bits
        DLPF_Config = read_byte(self.ADDRESS, regs['Config']) & mask

        if DLPF_Config == 0 or DLPF_Config == 7:
            gyro_rate = 8000 # Hz
        else:
            gyro_rate = 1000 # Hz

        return gyro_rate/(1+div)

    def SetConfig(self, value):
        """
        Bits 7,6 N/A
        Bits 5-3 EXT_SYNC_SET[2:0]
        Bits 2-0 DLPF_CFG[2:0]
        """
        write_byte(self.ADDRESS, reg['Config'], value)

    def GetConfig(self):
        return read_byte(self.ADDRESS, regs['Config'])

    def GetConfigExtSync(self):
        mask = 0b00111000
        shift = 3
        return (self.GetConfig() & mask) >> shift

    def GetConfigDLPFConfig(self):
        mask = 0b00000111
        return self.GetConfig() & mask

    def SetGyroConfig(self, value):
        write_byte(self.ADDRESS, reg['Gyro Config'], value)

    def GetGyroConfig(self):
        return read_byte(self.ADDRESSS, reg['Gyro Config'])

    def GetGyroRange(self):
        mask = 0b00011000
        shift = 3
        return (self.GetGyroConfig() & mask) >> shift

    def SetAccelConfig(self, value):
        write_byte(self.ADDRESS, reg['Accel Config'], value)

    def GetAccelConfig(self):
        return read_byte(self.ADDRESS, reg['Accel Config'])

    def GetAccelRange(self):
        mask = 0b00011000
        shift = 3
        return (self.GetAccelConfig() & mask) >> shift

    def SetMotionThreshold(self, value):
        write_byte(self.ADDRESS, reg['Motion Thresh'], value)

    def GetMotionThreshold(self):
        return read_byte(self.ADDRESS, reg['Motion Thresh'])

    def SetFIFOEnable(self, value):
        write_byte(self.ADDRESS, reg['FIFO Enable'], value)

    def GetFIFOEnable(self, value):
        return read_byte(self.ADDRESS, reg['FIFO Enable'])

    def EnableFIFO(self, sensors):
        sensor_dict = {
            'Temp'  : 0b10000000,
            'XG'    : 0b01000000,
            'YG'    : 0b00100000,
            'ZG'    : 0b00010000,
            'Accel' : 0b00001000
        } #purposefully leaving off SLVs (doubt they will be utilized)

        setting = 0b00000000
        if type(sensors) == list:
            for sensor in sensors:
                setting |= sensor_dict[sensor]
        elif type(sensors == str)
            setting = self.SensorStrToByte(sensors)
        # else set all to 0

        self.SetFIFOEnable(setting)

    def SetSingleMaster(self):
