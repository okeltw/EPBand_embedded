"""
Main File for EP Band embedded code
Authors: Taylor Okel, Andrew Albert, Brandon Poplstein
"""

import smbus
from Pulse import PulseController
from Motion import MotionController
from Bluetooth import BluetoothController
import sys

def main(argv):
    debug = False # send this where necessary to enable/disable debug
    # e.g. if debug: print(<debug info>)

    try:
        opts, args = getopt.getopt(argv)
    except getopt.GetoptError:
        print("Incorrect input options")
        sys.exit(2)

    for opt, arg in opts:
        if opt in ("-d", "--debug"):
            debug = True
            print("Debug mode enabled.")


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
