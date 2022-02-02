from machine import Pin
import time
dpin = pin(15, Pin.IN)
while True:
    print(pin.value())
