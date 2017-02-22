"""
Bluetooth communication controller.
"""

import bluetooth
import sys
import time
import json

class BluetoothController(object):
    """docstring for ."""

    ADDRESS = "devicename" # TODO: actual address
    sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)

    def __init__(self):
        print("Initializing Bluetooth...")
        self.connect()
        print("Connected")

    def connect(self):
        print("Attempting connection...")

        if(False):
            raise ConnectionError("Failed to connect to Bluetooth Module")
        # TODO

    def get_iPhone(self, name):
        devs = bluetooth.discover_devices()

        for address in devs:
            device_name = bluetooth.lookup_name(address)
            if device_name == name:
                print("Found bluetooth to pair %s at %s\n" % (device_name, address))
                return address
            else:
                print("Could not find the device\n")
                return ""

    def open_Bluetooth(self, device, port):
        self.sock.connect((device, port))
        return sock

    def send_HeartRate( socket, BPM ):
        #TODO: json string for heartrate
        Time = time.strftime("%H:%M:%S",time.gmtime())
        data = {"Data" : "BPM"}
        data = json.dumps(data)
        socket.send(data)

    def send_Accelerometer( socket, x, y, z, rx, ry, rz):
        #TODO: json string for accelerometer
        Time = time.strftime("%H:%M:%S",time.gmtime())
        Linear = str(x) + ',' + str(y) + ',' + str(z)
        Gyro = str(rx) + ',' + str(ry) + ',' + str(rz)
        data = 'Data/' + Time + '/LINEAR' + Linear + '/GYRO/' + Gyro
        print("%s" % data)
        socket.send(data)
