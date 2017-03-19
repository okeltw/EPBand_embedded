import RPi.GPIO as GPIO
from Pulse import PulseController
import sys
import time

PC = PulseController()

flag = False

channel = 8

GPIO.setmode(GPIO.BOARD)
GPIO.setup(channel, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
GPIO.add_event_detect(channel, GPIO.RISING, callback=PC.Pulse_callback, bouncetime=550)

t = 10
while 1:
    #do nothing...
    time.sleep(t)
    PC.Pulse_reading(t)
    print(PC.pulse)
    PC.reset()
