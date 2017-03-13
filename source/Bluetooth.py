"""
Bluetooth communication controller.
"""

import bluetooth
import sys
import time
import json
import uuid as uuidHelper

GET = "{req:GET}"
SET = "{req:SET}"

class BluetoothController(object):
    """docstring for ."""

    ADDRESS = None # Set during connection
    server = None
    port = 0
    MAC = None # set during init
    uuidStr = "1e0ca4ea-299d-4335-93eb-27fcfe7fa848" #does it matter what this is?
    uuidHex = ''

    client = None
    clientInfo = None

    def __init__(self):
        self.server =  bluetooth.BluetoothSocket(bluetooth.RFCOMM)
        self.MAC = uuidHelper.getnode()
        print("MAC: ", hex(self.MAC))
        self.uuidHex = uuidHelper.UUID("{" + self.uuidStr + "}")
        print("UUID (String): ", self.uuidStr)
        print("UUID (Hex): ", self.uuidHex)
        self.connect()

    def connect(self):
        print("Attempting connection...")
        self.port = 0
        self.server.bind(("", self.port))
        self.port = self.server.getsockname()[1]
        self.server.listen(1)
        print("Listening on port ", self.port)
        bluetooth.advertise_service(self.server, "EP Band", self.uuidStr)
        print("Waiting for connection...")
        self.client,self.clientInfo = self.server.accept()
        print("Connected to ", self.clientInfo)

    def monitor(self):
        try:
            request = client.recv(size)
            if request:
                return json.loads(request)
            else:
                return None
        except:
            print("Closing Socket")
            self.close()
            return "ERR!"

    def close(self):
        self.client.close()
        self.server.close()

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

    def sendDict(self, socket, data):
        data["Time"] = time.strftime("%H:%M%S", time.gmtime())
        data = json.dumps(data)
        socket.send(data)

    def _send(self):
        Time = time.strftime("%H:%M%S", time.gmtime())
        data = { "Time:" : Time }
        data = json.dumps(data)
        self.client.send(data)
