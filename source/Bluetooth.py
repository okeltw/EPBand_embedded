"""
Bluetooth communication controller.
"""

import bluetooth
import sys
import time
import json

class BluetoothController(object):
    """docstring for ."""

    ADDRESS = None # Set during connection
    server_sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
    port = 0
    uuid = "1e0ca4ea-299d-4335-93eb-27fcfe7fa848" #does it matter what this is?

    client_sock = 0
    client_address = 0

    def __init__(self):
        print("Initializing Bluetooth...")
        self.connect()
        print("Connected")

    def connect(self):
        print("Attempting connection...")
        self.port = bluetooth.get_available_port(bluetooth.RFCOMM)
        self.server_sock.bind("", port)
        self.server_sock.listen(1)
        print("Listening on port ", self.port)
        bluetooth.advertise_service(self.server_sock, "EP Band", uuid)
        self.client_sock,self.client_address = self.server_sock.accept()
        print("Connected to " self.client_address)

    def close(self):
        client_sock.close()
        server_sock.close()

    def send_HeartRate(self, socket, BPM ):
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

    def send(self, socket, BPM, x, y, z, rx, ry, rz):
        Time = time.strftime("%H:%M%S", time.gmtime())
        data = {"Time"  : Time,
                "BPM"   : str(BPM),
                "Motion": {
                    "X" : str(x),
                    "Y" : str(y),
                    "Z" : str(z),
                    "RX": str(rx),
                    "RY": str(ry),
                    "RZ": str(rz)
                }
        }
        data = json.dumps(data)
        socket.send(data)
