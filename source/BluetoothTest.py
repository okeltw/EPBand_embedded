import time
from Bluetooth import BluetoothController
from TestData import BT_test_data as data

BC = BluetoothController()

try:
    # point = [bpm, x,y,z,rx,ry,rz]
    packet = buildPacket(data[0])
    for point in data[1:]:
        packet["BPM"] += [point[0]
        packet["Motion"]["X"] += [point[1]]
        packet["Motion"]["Y"] += [point[2]]
        packet["Motion"]["Z"] += [point[3]]
        packet["Motion"]["RX"]+= [point[4]]
        packet["Motion"]["RY"]+= [point[5]]
        packet["Motion"]["RZ"]+= [point[6]]
    
    BC.sendDict(BC.client,
                packet)
        
except:
    BC.close()
    raise

def buildPacket(point):
    packet =    { "BPM" : [point[0]],
                   "Motion" : {
                       "X" : [point[1]],
                       "Y" : [point[2]],
                       "Z" : [point[3]],
                       "RX": [point[4]],
                       "RY": [point[5]],
                       "RZ": [point[6]]
                    }
                } 
