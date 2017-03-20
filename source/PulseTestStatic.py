from Pulse import PulseController
import time

PC = PulseController()

### Test one old sample
t = time.time() - 60
PC.add_pulse_time(t)

# Add test points
for i in range(60):
    PC.add_pulse_time(t + i)

print("Number of Samples [61]: ", PC.num_pulse_times)

# Analyze data
PC.Pulse_reading()

print("Pulse reading [around 60]", PC.pulse)
print("Number of Samples: ", PC.num_pulse_times)



