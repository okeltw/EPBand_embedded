"""
I2C general functions

The following is a link to smbus2, which is claimed to be syntactically similar.
As such, it is a good source to figure out what these calls do.
https://pypi.python.org/pypi/smbus2/0.1.2
"""

import smbus

bus = smbus.SMBus(1) # or 0 for rev1

def write_byte(address, register, data):
    """
    Write a single byte [data] to register at address.
    """
    bus.write_byte_data(address, register, data)
    return None

def read_byte(address, register):
    """
    Reads a single byte from register at address
    """
    return bus.read_byte_data(address, register)

def read_word(address, register):
    """
    Read a word from register at address
    """
    high = bus.read_byte_data(address, register)
    low = bus.read_byte_data(address, register+1)
    val = (high << 8) + low # Shift upper byte and append lower byte
    return val

"""
Read a word and 2's complement it
"""
def read_word_2c(address, register):
    val = read_word(address, register)
    if (val >= 0x8000):
        return -((65535 - val) +1)
    else:
        return val

def close():
    """
    Close the i2c bus
    """
    global bus #global needed to alter global var
    bus.close()
