from machine import Pin
import time

sensor_pir=Pin(26, Pin.IN, Pin.PULL_DOWN)
led =Pin(25, Pin.OUT)
def pir_handler(pin):
    time.sleep(0.1)
    if pin.value():
        print(pin.value())
        for i in range (50):
            time.sleep(0.1)
            led.toggle()
sensor_pir.irq(trigger=Pin.IRQ_RISING, handler=pir_handler)

while True:
    print(sensor_pir())
    time.sleep(0.1)
