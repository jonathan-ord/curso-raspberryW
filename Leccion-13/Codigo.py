from machine import Pin
import time

tactil = Pin(0, Pin.IN)

while True:

    print(tactil.value())
    time.sleep_ms(500)

