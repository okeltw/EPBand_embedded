import time
from Bluetooth import BluetoothController
from TestData import BT_test_data as data

BC = BluetoothController()

def buildPacket(point):
    packet =    { "BPM" : [point[0]]*10,
                   "Motion" : {
                       "X" : [point[1]]*10,
                       "Y" : [point[2]]*10,
                       "Z" : [point[3]]*10,
                       "RX": [point[4]]*10,
                       "RY": [point[5]]*10,
                       "RZ": [point[6]]*10
                    }
                } 
    return packet

try:
    # point = [bpm, x,y,z,rx,ry,rz]
    packet = buildPacket(data[0])
    for point in data[1:]:
        packet["BPM"] += [point[0]] *10
        packet["Motion"]["X"] += [point[1]] *10
        packet["Motion"]["Y"] += [point[2]] *10
        packet["Motion"]["Z"] += [point[3]] *10
        packet["Motion"]["RX"]+= [point[4]] *10
        packet["Motion"]["RY"]+= [point[5]] *10
        packet["Motion"]["RZ"]+= [point[6]] *10 
    
    BC.sendDict(BC.client,
                packet)
        
except:
    BC.close()
    raise


