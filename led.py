import digitalio
import board

class LED:
    def __init__(self):
        self.led = digitalio.DigitalInOut(board.LED)
        self.led.direction = digitalio.Direction.OUTPUT

    def on(self):
        self.led.value = True

    def off(self):
        self.led.value = False

    def toggle(self):
        self.led.value = not self.led.value