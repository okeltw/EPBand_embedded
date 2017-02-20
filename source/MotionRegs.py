"""
A dictionary that holds all the registers for MPU6050

Shorthand Notes:
[R]     == Read Only
[W]     == Write Only
[R/W]   == Read/Write
MST     == master
Thresh  == threshold
DO      == Data Output (?)
DI      == Data Input (?)
Int     == Interrupt
"""

regs = {
    'Self Test X'   : 0x0D, # [R/W] Gyroscope/accelerometer self test
    'Self Test Y'   : 0x0E,
    'Self Test Z'   : 0x0F,
    'Self Test A'   : 0x10, # [R/W] Self test gyro/accel switch (?)
    'Sample Rate'   : 0x19, # [R/W] Control sample rate; higher is slower
    'Config'        : 0x1A, # [R/W] Configure FSYNC pin and DLPF
    'Gyro Config'   : 0x1B, # [R/W] Used to trigger gyro self test and scale range
    'Accel Config'  : 0x1C, # [R/W] Used to trigger Accel self test and scale range
    'Motion Tresh'  : 0x1F, # [R/W] Configure detection threshold for motion interrupt
    'FIFO Enable'   : 0x23, # [R/W] Determines which measurements are loaded into buffer
    'I2C Mst Ctrl'  : 0x24, # [R/W] Configure for single or multi master I2C
    'I2C Slv0 Addr' : 0x25, # [R/W] Configure data transfer sequence for Slave 0
    'I2C Slv0 Reg'  : 0x26,
    'I2C Slv0 Ctrl' : 0x27,
    'I2C Slv1 Addr' : 0x28, # [R/W] Configure data transfer sequence for Slave 1
    'I2C Slv1 Reg'  : 0x29,
    'I2C Slv1 Ctrl' : 0x2A,
    'I2C Slv2 Addr' : 0x2B, # [R/W] Configure data transfer sequence for Slave 2
    'I2C Slv2 Reg'  : 0x2C,
    'I2C Slv2 Ctrl' : 0x2D,
    'I2C Slv3 Addr' : 0x2E, # [R/W] Configure data transfer sequence for Slave 0
    'I2C Slv3 Reg'  : 0x2F,
    'I2C Slv3 Ctrl' : 0x30,
    'I2C Slv4 Addr' : 0x31, # [R/W] Configure data transfer sequence for Slave 4
    'I2C Slv4 Reg'  : 0x32,
    'I2C Slv4 DO'   : 0x33,
    'I2C Slv4 Ctrl' : 0x34,
    'I2C Slv4 DI'   : 0x35,
    'I2C Mst Staus' : 0x36, # [R] Shows the status of the interrupt generating signals
    'Int Pin Config': 0x37, # [R/W] Configures the behavior of the interrupt signals
    'Int Enable'    : 0x38, # [R/W]Enables/Disables interrupt generation
    'Int Status'    : 0x3A, # [R] Shows the interupt status of each source
    'Accel X High'  : 0x3B, # [R] Stores the most recent accel measurements
    'Accel X Low'   : 0x3C,
    'Accel Y High'  : 0x3D,
    'Accel Y Low'   : 0x3E,
    'Accel Z High'  : 0x3F,
    'Accel Z Low'   : 0x40,
    'Temp High'     : 0x41, # [R] Stores the most recent temp measurement
    'Temp Low'      : 0x42,
    'Gyro X High'   : 0x43, # [R] Stores the most recent gyro measurements
    'Gyro X Low'    : 0x44,
    'Gyro Y High'   : 0x45,
    'Gyro Y Low'    : 0x46,
    'Gyro Z High'   : 0x47,
    'Gyro Z Low'    : 0x48,
    'Ext Sensor 0'  : 0x49, #[R] Stores data read from external sensors
    'Ext Sensor 1'  : 0x4A,
    'Ext Sensor 2'  : 0x4B,
    'Ext Sensor 3'  : 0x4C,
    'Ext Sensor 4'  : 0x4D,
    'Ext Sensor 5'  : 0x4E,
    'Ext Sensor 6'  : 0x4F,
    'Ext Sensor 7'  : 0x50,
    'Ext Sensor 8'  : 0x51,
    'Ext Sensor 9'  : 0x52,
    'Ext Sensor 10' : 0x53,
    'Ext Sensor 11' : 0x54,
    'Ext Sensor 12' : 0x55,
    'Ext Sensor 13' : 0x56,
    'Ext Sensor 14' : 0x57,
    'Ext Sensor 15' : 0x58,
    'Ext Sensor 16' : 0x59,
    'Ext Sensor 17' : 0x5A,
    'Ext Sensor 18' : 0x5B,
    'Ext Sensor 19' : 0x5C,
    'Ext Sensor 20' : 0x5D,
    'Ext Sensor 21' : 0x5E,
    'Ext Sensor 22' : 0x5F,
    'Ext Sensor 23' : 0x60,
    'I2C Slv0 DO'   : 0x63, # [R/W] Holds output data written into Slave when in write mode
    'I2C Slv1 DO'   : 0x64,
    'I2C Slv2 DO'   : 0x65,
    'I2C Slv3 DO'   : 0x66,
    'I2C Mst Delay' : 0x67, # [R/W] Used to specify timing of ext sensor data shadowing, decrease access rate of slave devices relative to sample rate
    'Sig Path Rst'  : 0x68, # [W] Used to reset the A/D signal paths of internal sensors
    'Mot Dtect Ctrl': 0x69, # [R/W] Add delay to accel power on time, configure detection decrement rate
    'User Ctrl'     : 0x6A, # [R/W] Enable/Disable FIFO, I2C Master, and primary I2C interface.
    'Pwr Mgmt 1'    : 0x6B, # [R/W] Configure power mode and clock source
    'Pwr Mgmt 2'    : 0x6C, # [R/W] Frequency of wake-ups in Accel only low pwr mode. Put individual axes into standby mode.
    'FIFO Cnt High' : 0x72, # [R] Keep track of the current number of samples in the buffer
    'FIFO Cnt Low'  : 0x73,
    'FIFO R/W'      : 0x74, # [R/W] Read/Write data on FIFO buffer
    'Who Am I'      : 0x75, # [R] Verify identity of device (I2C address)
}
