import time
from led import LED
from serial_relay import SerialRelay
from remote_control import RemoteControl
from motor_controler import MotorControler

remoteControl = RemoteControl()
led = LED()
relay = SerialRelay()
motorControler = MotorControler(relay)

while True:
    left, right, power = remoteControl.update()
    if(power > 0.1):
        led.on()
        motorControler.update(left, right)
    else:
        led.off()
        relay.update()
    # time.sleep(0.05)
    # led.toggle()