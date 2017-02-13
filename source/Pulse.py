"""
The pulse/hearbeat sensor controller.
"""

import RPi.GPIO as GPIO
import sys
import time
from time import sleep

class PulseController(object):
    ADDRESS = 0x00 # TODO: actual address
    VALUE = GPIO.LOW
    OLD_VALUE = GPIO.LOW
    CHANNEL = None
    
    def __init__(self):
        print("Initializing pulse sensor")
        #self.setup()
        #print("Setup")
        
    def setup(self, channel):
        self.CHANNEL = channel
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(channel, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)

    def measure(self):
        GPIO.input( self.CHANNEL)
        if self.VALUE == GPIO.LOW:
            print("Channel %d is LOW\n" % self.CHANNEL)
            return 0
        else:
            print("Channel %d is HIGH\n" % self.CHANNEL)
            return 1

    def edge_detect(self):
        GPIO.wait_for_edge(self.CHANNEL, GPIO.RISING)
        print("Rising edge\n")

    def monitor(self):
        while True:
            self.edge_detect(self)
            Time = time.strftime("%H:%M:%S",time.gmtime())
            print("%s\n" % Time)

    def monitor2(self):
        while True:
            self.VALUE = GPIO.input( self.CHANNEL)
            if self.VALUE != self.OLD_VALUE:
                Time = time.strftime("%H:%M:%S",time.gmtime())
                self.OLD_VALUE = self.VALUE
                if self.VALUE == GPIO.LOW:
                    print("%s LOW" % Time)
                else:
                    print("%s HIGH\n" % Time)
            if self.VALUE == GPIO.HIGH:
                sleep(0.1)

    def visualize(self):
        while True:
            self.VALUE = GPIO.input(self.CHANNEL)
            if self.VALUE == GPIO.LOW:
                print("_____\t%s" % time.strftime("%H:%M:%S",time.gmtime()))
            else:
                print("|||||\t%s" % time.strftime("%H:%M:%S",time.gmtime()))
        
    def cleanup(self):
        GPIO.cleanup(self.CHANNEL)



