import time
from Bluetooth import BluetoothController
BC = BluetoothController()

print('a')
try:
    print('b')
    while 1:
        print('sending')
        BC._send()
        print('sent')
        time.sleep(1)
except:
    BC.close()
    raise
