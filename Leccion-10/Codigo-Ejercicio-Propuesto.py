from machine import Pin
import time

pinLectura1 = Pin(0, Pin.IN)
pinLed1 = Pin(1, Pin.OUT)
estado_anterior1 = 1

pinLectura2 = Pin(3, Pin.IN)
pinLed2 = Pin(2, Pin.OUT)
estado_anterior2 = 1

while True:

    lectura1 = pinLectura1.value()
    lectura2 = pinLectura2.value()

    if lectura1 == 0 and estado_anterior1 == 1:
        pinLed1.toggle()
    estado_anterior1 = lectura1

    if lectura2 == 0 and estado_anterior2 == 1:
        pinLed2.toggle()
    estado_anterior2 = lectura2

    time.sleep(0.05)
