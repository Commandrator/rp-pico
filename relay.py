from machine import Pin
import time
Button_1 = Pin(14, Pin.IN, Pin.PULL_DOWN)
relay = Pin(15, Pin.OUT, Pin.PULL_DOWN)
while True:
    if Button_1.value():
        print("Relay Status:", relay.value())
        relay.toggle()
    time.sleep(0.2)
