"""
The pulse/heartbeat sensor controller.
"""

class PulseController(object):
    """docstring for ."""

    ADDRESS = 0x00 # TODO: actual address

    def __init__(self):
        print("Initializing Pulse...")
        self.connect()
        print("Connected")

    def connect(self):
        print("Attempting connection...")

        if(False):
            raise ConnectionError("Failed to connect to Pulse Sensor")
        # TODO
