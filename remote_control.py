import board
import pulseio

class RemoteControl:
    def __init__(self):
        self.throttle = RemoteInput(board.GP10)
        self.turn = RemoteInput(board.GP11)
        self.power = RemoteInput(board.GP12)
        print("Remote Control Initialized")

    def update(self):
        thottle = self.throttle.update()
        turn = self.turn.update()
        power = self.power.update()
        left, right = self.map_to_motor(thottle, turn, power)
        return left, right, power
    
    def map_to_motor(self, throttle, turn, power):
        power = (power + 1) * 0.5
        turn = turn * 0.5
        left = (throttle * power) + (turn * power)
        right = (throttle * power) - (turn * power)
        return left, right

class RemoteInput:
    def __init__(self, pin):
        self.pulse = pulseio.PulseIn(pin, maxlen=10)
        self.max_low_time = 2000
        self.min_low_time = 1000
        self.last_value = 0

    def update(self):
        duty_cycle = self.last_value
        # Wait until we have at least two pulses
        if len(self.pulse) >= 2:
            low_time = min(self.pulse[0], self.pulse[1])  
            self.pulse.clear()

            # Update if in range
            if low_time < self.max_low_time + 100 and low_time > self.min_low_time - 100:
                mid_low_time = (self.max_low_time + self.min_low_time) / 2
                duty_cycle = (low_time - mid_low_time) / ((self.max_low_time - self.min_low_time) / 2)   

        self.last_value = duty_cycle    
        return duty_cycle