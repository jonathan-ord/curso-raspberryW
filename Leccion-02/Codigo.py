from machine import Pin
import time

miLed = Pin("LED", Pin.OUT)

while(True):
    miLed.on()
    time.sleep_ms(500)
    miLed.off()
    time.sleep_ms(500)
