"""
The Motion (accelerometer && gyro) controller.
"""

from I2C import *
from MotionRegs import regs
import math

class MotionController(object):
    """docstring for ."""

    # Base address for the data
    ADDRESS = 0x68

    # Initialize variables
    AccelData = {"X": [], "Y": [], "Z": [], "X_scl": [], "Y_scl": [], "Z_scl": []}
    GyroData = {"X": [], "Y": [], "Z": [], "X_scl": [], "Y_scl": [], "Z_scl": []}

    TempData = []

    accel_scl = 16384.0
    gyro_scl = 131.0

    def __init__(self):
        print("Initializing Motion...")
        self.connect()
        print("Connected")


    def connect(self):
        print("Attempting connection...")
        # Write the active power management state to MPU
        # Disable sleep, temperature sensor
        write_byte(self.ADDRESS, regs['Pwr Mgmt 1'], 0b00001000)
        write_byte(self.ADDRESS, regs['Pwr Mgmt 2'], 0b00001000)

    def close(self):
        # Put motion to sleep
        write_byte(self.ADDRESS, regs['Pwr Mgmt 1'], 0b01000000)

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

    def set(self, register, value):
        write_byte(self.ADDRESS, regs[register], value)

    def read(self):
        """
        Use the addresses above to collect and store MPU data
        """

        val = read_word_2c(self.ADDRESS, regs['Accel X High'])
        self.AccelData["X"] += [val]
        self.AccelData["X_scl"] += [round(val/self.accel_scl, 2) ]

        val = read_word_2c(self.ADDRESS, regs['Accel Y High'])
        self.AccelData["Y"] += [val]
        self.AccelData["Y_scl"] += [round(val/self.accel_scl, 2) ]

        val = read_word_2c(self.ADDRESS, regs['Accel Z High'])
        self.AccelData["Z"] += [val]
        self.AccelData["Z_scl"] += [round(val/self.accel_scl, 2) ]

        val = read_word_2c(self.ADDRESS, regs['Gyro X High'])
        self.GyroData["X"] += [val]
        self.GyroData["X_scl"] += [round(val/self.gyro_scl, 2) ]

        val = read_word_2c(self.ADDRESS, regs['Gyro Y High'])
        self.GyroData["Y"] += [val]
        self.GyroData["Y_scl"] += [round(val/self.gyro_scl, 2) ]

        val = read_word_2c(self.ADDRESS, regs['Gyro Z High'])
        self.GyroData["Z"] += [val]
        self.GyroData["Z_scl"] += [round(val/self.gyro_scl, 2) ]

        #val = read_word_2c(self.ADDRESS, regs['Temp High'])
        #self.TempData += [val/340 + 36.53] # degrees celcius

        return None

    def readFIFO(self):
        """
        Read all the data in the FIFO buffer.
        """
        num_samples = read_word(self.ADDRESS, regs['FIFO Cnt High'])
        #print(num_samples)

        # FIFO Count holds the number of samples.
        # The samples are stored in order from their register values.
        # There are 6 values sampled, so step by 6 as each loop will grab each
        # of these values.
        for sample in range(0,num_samples+1, 6):
            val = read_word_2c(self.ADDRESS, regs['FIFO R/W'])
            self.AccelData["X"] += [val]
            self.AccelData["X_scl"] += [val / self.accel_scl ]

            val = read_word_2c(self.ADDRESS, regs['FIFO R/W'])
            self.AccelData["Y"] += [val]
            self.AccelData["Y_scl"] += [val / self.accel_scl ]

            val = read_word_2c(self.ADDRESS, regs['FIFO R/W'])
            self.AccelData["Z"] += [val]
            self.AccelData["Z_scl"] += [val / self.accel_scl ]

            val = read_word_2c(self.ADDRESS, regs['FIFO R/W'])
            self.GyroData["X"] += [val]
            self.GyroData["X_scl"] += [val / self.gyro_scl ]

            val = read_word_2c(self.ADDRESS, regs['FIFO R/W'])
            self.GyroData["Y"] += [val]
            self.GyroData["Y_scl"] += [val / self.gyro_scl ]

            val = read_word_2c(self.ADDRESS, regs['FIFO R/W'])
            self.GyroData["Z"] += [val]
            self.GyroData["Z_scl"] += [val / self.gyro_scl ]

    def Overflow_callback(self):
        mask = 0b00010000 # Pull out overflow bit
        status = self.GetIntStatus()
        # If the int status is overflow (it should be, no other ints are enabled)
        if status & mask:
            print('Overflow!')
            self.readFIFO()
            self.resetFIFO()
        else:
            print('Unknown Interrupt')

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
        write_byte(self.ADDRESS, regs['Sample Rate'], value)

    def GetSampleDivider(self):
        return read_byte(self.ADDRESS, regs['Sample Rate'])

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
        write_byte(self.ADDRESS, regs['Config'], value)

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
        write_byte(self.ADDRESS, regs['Gyro Config'], value)

    def GetGyroConfig(self):
        return read_byte(self.ADDRESSS, regs['Gyro Config'])

    def GetGyroRange(self):
        mask = 0b00011000
        shift = 3
        return (self.GetGyroConfig() & mask) >> shift

    def SetAccelConfig(self, value):
        write_byte(self.ADDRESS, regs['Accel Config'], value)

    def SetAccelRange(self, value):
        """
        AFS_SEL     Full Scale Range
        0           ± 2g
        1           ± 4g
        2           ± 8g
        3           ± 16g
        """
        currentConfig = self.GetAccelConfig()
        newConfig = currentConfig | (value << 3)
        write_byte(self.ADDRESS, regs['Accel Config'], newConfig)

    def GetAccelConfig(self):
        return read_byte(self.ADDRESS, regs['Accel Config'])

    def GetAccelRange(self):
        mask = 0b00011000
        shift = 3
        return (self.GetAccelConfig() & mask) >> shift

    def SetMotionThreshold(self, value):
        write_byte(self.ADDRESS, regs['Motion Thresh'], value)

    def GetMotionThreshold(self):
        return read_byte(self.ADDRESS, regs['Motion Thresh'])

    def SetFIFOEnable(self, value):
        write_byte(self.ADDRESS, regs['FIFO Enable'], value)

    def GetFIFOEnable(self,):
        return read_byte(self.ADDRESS, regs['FIFO Enable'])

    def EnableFIFO(self, sensors):
        #Enable the FIFO Buffer
        user_control = read_byte(self.ADDRESS, regs['User Ctrl'])
        user_control |= 0b01000000
        write_byte(self.ADDRESS, regs['User Ctrl'], user_control)

        # Dictionary to simplify activating bits
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
        elif type(sensors) == str:
            setting = self.SensorStrToByte(sensors)
        # else set all to 0

        print(setting)
        self.SetFIFOEnable(setting)

    def SetI2CMasterCtrl(self, value):
        write_byte(self.ADDRESS, regs['I2C Mst Ctrl'], value)

    def GetI2CMasterCtrl(self):
        return read_byte(self.ADDRESS, regs['I2C Mst Ctrl'])

    def SetIntPinConfig(self, value):
        write_byte(self.ADDRESS, regs['Int Pin Config'], value)

    def GetIntPinConfig(self):
        return read_byte(self.ADDRESS, regs['Int Pin Config'])

    def SetOverflowInt(self):
        self.SetIntEnable(0b00010000)

    def SetIntEnable(self, value):
        write_byte(self.ADDRESS, regs['Int Enable'], value)

    def GetIntEnable(self):
        return read_byte(self.ADDRESS, regs['Int Enable'])

    def GetIntStatus(self):
        return read_byte(self.ADDRESS, regs['Int Status'])

    def GetFIFOOverflowInt(self):
        mask = 0b00010000
        shift = 4
        return (GetIntStatus() & mask) >> shift

    def resetFIFO(self):
        """
        This bit resets the FIFO buffer when set to 1 while FIFO_EN equals 0.
        This bit automatically clears to 0 after the reset has been triggered.
        """
        # Disable the FIFO and reset the buffer
        user_control = read_byte(self.ADDRESS, regs['User Ctrl'])
        user_control ^= 0b01000100
        write_byte(self.ADDRESS, regs['User Ctrl'], user_control)

        # Sleep to let the FIFO clear? needs testing

        # Reactivate the FIFO
        user_control ^= 0b01000100
        write_byte(self.ADDRESS, regs['User Ctrl'], user_control)

    def Reset(self):
        value = 0b00000111
        write_byte(self.ADDRESS)
