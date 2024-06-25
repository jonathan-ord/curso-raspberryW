from machine import Pin
import time

ledRojo = Pin(0, Pin.OUT)
ledVerde = Pin(1, Pin.OUT)
ledAzul = Pin(2, Pin.OUT)

espera = 800

while True:

    ledRojo.off()
    ledVerde.off()
    ledAzul.off()

    time.sleep_ms(espera)

    ledRojo.on()
    ledVerde.off()
    ledAzul.off()

    time.sleep_ms(espera)

    ledRojo.off()
    ledVerde.on()
    ledAzul.off()

    time.sleep_ms(espera)

    ledRojo.off()
    ledVerde.off()
    ledAzul.on()

    time.sleep_ms(espera)
