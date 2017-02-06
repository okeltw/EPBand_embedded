"""
Bluetooth communication controller.
"""

class BluetoothController(object):
    """docstring for ."""

    ADDRESS = "devicename" # TODO: actual address

    def __init__(self):
        print("Initializing Bluetooth...")
        self.connect()
        print("Connected")

    def connect(self):
        print("Attempting connection...")

        if(False):
            raise ConnectionError("Failed to connect to Bluetooth Module")
        # TODO
