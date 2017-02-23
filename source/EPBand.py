"""
Main File for EP Band embedded code
Authors: Taylor Okel, Andrew Albert, Brandon Poplstein
"""

import smbus
from Pulse import PulseController
from Motion import MotionController
from Bluetooth import BluetoothController
import sys
import time
from RPi.GPIO import GPIO

print('starting')

try:
    PC = PulseController()
    MC = MotionController()
    BC = BluetoothController()
except ConnectionError as error:
    print(error)
except Exception as error:
    print("An unknown error occured: ")
    print(error)
    quit()

BT.open_Bluetooth

pulse_channel = 0 #TODO
motion_int_channel = 0 #TODO

GPIO.setmode(GPIO.BOARD)
GPIO.setup(pulse_channel, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
GPIO.setup(motion_int_channel, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)

#Spawn a new thread to monitor this gpio pin. will increment pulse_counter by 1 each rising edge.
GPIO.add_event_detect(pulse_channel, GPIO.RISING, callback=PC.Pulse_callback)

# Spawn a new thread to monitor MPU interrupts
GPIO.add_event_detect(motion_int_channel, GPIO.RISING, callback=MC.Overflow_callback)

# Set the sample rate to the slowest value
# Thought here is to prevent buffer overflows.
# We don't need fine measurements anyways.
MC.SetSampleRate(255)

# Enable the FIFO (The buffer intself and the individual measurements)
MC.EnableFIFO(('XG','YG','ZG','Accel'))

# main loop

counter = 0
sleep_time = 0.1
counter_thresh = 60
elapsed_time = sleep_time * counter_thresh
while 1:
    # Send/Display data once a second
    if counter < counter_thresh:
        counter += 1
    else:
        counter = 0
        print(chr(27) + "[2J")
        MC.printall()
        print("\n\nBPM: " PC.Pulse_reading(elapsed_time))
        MC.clear()
        PC.reset()

    # Tell Motion Controller to read the sensor data (FIFO Buffer)
    MC.readFIFO()
    # Clear the FIFO Buffer
    MC.resetFIFO()

    BT.send

    # Don't overload the PI
    time.sleep(0.1)
