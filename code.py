import time
import board
import pulseio
import digitalio

print("PulseIn Example")

pin = board.GP10
pulse = pulseio.PulseIn(pin, maxlen=10)
led = digitalio.DigitalInOut(board.LED)
led.direction = digitalio.Direction.OUTPUT

while True:
    # Wait until we have at least two pulses
    if len(pulse) >= 2:
        # Store them before clearing the buffer
        high_time = max(pulse[0], pulse[1])
        low_time = min(pulse[0], pulse[1])
        
        # Now we can clear the buffer
        pulse.clear()
        
        # Calculate duty cycle
        total_period = high_time + low_time
        duty_cycle = (high_time / total_period) * 100 if total_period != 0 else 0
        
        # Print results
        print("High Time:", high_time)
        print("Low Time:", low_time)
        print("Duty Cycle:", duty_cycle, "%")
    
    time.sleep(0.1)
    # led.value = not led.value
