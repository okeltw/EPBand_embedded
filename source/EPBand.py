"""
Main File for EP Band embedded code
Authors: Taylor Okel, Andrew Albert, Brandon Poplstein
"""

import smbus
from Pulse import PulseController
from Motion import MotionController
from Bluetooth import BluetoothController
import sys
#import thread
import time
import RPi.GPIO as GPIO
import bluetooth

print('starting')

try:
    PC = PulseController()
    MC = MotionController()
    time.sleep(2)
    BC = BluetoothController()
except ConnectionError as error:
    print(error)
except Exception as error:
    print("An unknown error occured: ")
    print(error)
    quit()

try:
    pulse_channel = 8 #TODO
    motion_int_channel = 7 #TODO

    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(pulse_channel, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
    #GPIO.setup(motion_int_channel, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)

    #Spawn a new thread to monitor this gpio pin. will increment pulse_counter by 1 each rising edge.
    GPIO.add_event_detect(pulse_channel, GPIO.RISING, bouncetime=450, callback=PC.Pulse_callback)

    # Spawn a new thread to monitor MPU interrupts
    #GPIO.add_event_detect(motion_int_channel, GPIO.RISING, callback=MC.Overflow_callback)

    # Set the sample rate to the slowest value
    # Thought here is to prevent buffer overflows.
    # We don't need fine measurements anyways.
    MC.SetSampleRate(255)

    # Enable the FIFO (The buffer intself and the individual measurements)
    #MC.EnableFIFO(('XG','YG','ZG','Accel'))

    # main loop

    counter = 0
    sleep_time = 0.1
    counter_thresh = 10
    elapsed_time = sleep_time * counter_thresh
    time_per_loop = elapsed_time    

    while 1:
        try:
            # Send/Display data once a second
            if counter < counter_thresh:
                counter += 1
            else:
                counter = 0
                PC.Pulse_reading(elapsed_time)
                AD = MC.AccelData
                GD = MC.GyroData
                BC.send(PC.pulse,
                        AD["X_scl"], AD["Y_scl"], AD["Z_scl"],
                        GD["X_scl"], GD["Y_scl"], GD["Z_scl"])
                
                PC.reset()
                MC.clear()

            MC.read()
            #request = BT.monitor()
    
            # Don't overload the PI
            time.sleep(sleep_time)
        except bluetooth.btcommon.BluetoothError:
            print("Connection lost, restarting BT service...")
            BC.reset() 

except KeyboardInterrupt:
    MC.close()
    PC.close()
    BC.close()
    GPIO.cleanup()
    print("Successfully closed the service.")
