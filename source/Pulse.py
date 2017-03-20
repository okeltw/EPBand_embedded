"""
The pulse/hearbeat sensor controller.
"""

#import RPi.GPIO as GPIO
import sys
import time
from time import sleep

class PulseController(object):
    ADDRESS = 0x00 # TODO: actual address
    #VALUE = GPIO.LOW
    #OLD_VALUE = GPIO.LOW
    CHANNEL = None

    pulse_counter = 0
    pulse = 0

    start_time = time.time()

    pulse_times = []
    num_pulse_times = 0

    # Oldest sample; max number of seconds
    oldest_sample = 60 

    def __init__(self):
        print("Initializing pulse sensor")
        self.clear_pulse_times()    
   
    def clear_pulse_times(self):
        self.pulse_times = []
        self.num_pulse_times = 0
    
    def add_pulse_time(self, t):
        """
        Append a time sample, t, to the pulse_time list
        """
        self.pulse_times += [t]
        self.num_pulse_times += 1

    def record_pulse(self):
        """
        Append a time sample from time.time() to the pulse_time list
        """
        self.add_pulse_time(time.time())
        
    def close(self):
        self.cleanup()
        return

    def Pulse_callback(self, param):
        """
        Set the GPIO pin as an interrupt. Use this function as a callback.
        Append a time sample to a list.
        """
        #self.pulse_counter += 1
        self.record_pulse()

    def Pulse_reading(self):
        """
        Return a reading following the formula.
        """
        #self.pulse = self.pulse_counter * (60/Time)
        
        # Get the number of seconds elapsed
        elapsed_time_sec = self.pulse_times[-1] - self.pulse_times[0]

        # Determine the BPM by the number of samples over the elapsed time (minutes)
        self.pulse = self.num_pulse_times / (elapsed_time_sec / 60)

        # Obtain current time
        current_time = time.time()

        # Obtain a list in the opposite order
        # I.e. Oldest sample to newest sample
        old_pulse_times = self.pulse_times

        # Purge the list of any samples older than sample threshold
        for sample in old_pulse_times:
            # Assuming the list is inorder from newest->oldest
            if (current_time - sample) > self.oldest_sample:
                # Sample is older than the threshold. Remove.               
                self.pulse_times = self.pulse_times[0:-1]
                self.num_pulse_times -= 1
            else:
                # Sample is not older than the threshold, keep. 
                # The remaining samples should likewise be valid, so we can break here.
                break

    def Validate(self, reading):
        """
        Sanity check on the reading.
        If it is out of a normal heart range, or is drastically different (TODO),
        reject the reading (display "Not Available" or some such)
        """
        if reading < low_thresh or reading > high_thresh:
            return False
        else:
            return True

    def reset(self):
        self.pulse_counter = 0
    

    def cleanup(self):
        GPIO.cleanup(self.CHANNEL)
