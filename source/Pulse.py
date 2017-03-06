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

    pulse_counter = 0
    pulse = 0

    def __init__(self):
        print("Initializing pulse sensor")
        #self.setup()
        #print("Setup")

    def setup(self, channel):
        """
        I'm moving all of this to main. Unsure how an interrupt would work if
        this remains in this class.
        self.CHANNEL = channel
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(channel, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
        """

    def close(self):
        # Do nothing...for now

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

    def Pulse_callback(self):
        """
        Set the GPIO pin as an interrupt. Use this function as a callback.
        Each time it is called, pulse_counter is incremented once.
        Thus, multiply pulse_counter by a ratio of 60s/elapsed_time to get a BPM.
        """
        pulse_counter += 1

    def Pulse_reading(self, Time):
        """
        Return a reading following the formula.
        Recommend calling reset immediately following this call.
        """
        pulse = pulse_counter * (60/Time)

    def Validate(self, reading):
        """
        Sanity check on the reading.
        If it is out of a normal heart range, or is drastically different (TODO),
        reject the reading (display "Not Available" or some such)
        """
        if reading < low_thresh or reading > high_thresh
            return False
        else:
            return True

    def reset(self):
        pulse_counter = 0

    def cleanup(self):
        GPIO.cleanup(self.CHANNEL)
