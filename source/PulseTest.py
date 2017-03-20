from RPi import GPIO
from Pulse import PulseController
import time

PC = PulseController()

GPIO.setmode(GPIO.BOARD)
GPIO.setup(8, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.add_event_detect(8, GPIO.RISING, bouncetime=400, callback=PC.Pulse_callback)

while 1:
    sleep(10)
    PC.Pulse_reading()
    print("Pulse Reading:", PC.pulse)
    print("Number of Samples", PC.num_pulse_times)
