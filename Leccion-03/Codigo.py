from machine import Pin
import time

led = Pin(1, Pin.OUT) 

while True:
    #Encendido mediante 1 o 0
    # 1 = encendido
    # 0 = apagado

    led.value(1) # ecendido
    led.value(0) # apagado

    # Con la propiedad Toggle
    led.toggle()
    time.sleep_ms(100)
