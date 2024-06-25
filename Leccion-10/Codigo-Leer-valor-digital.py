from machine import Pin
import time

# Crear una varibale con el Pin de entrada
pinLectura = Pin(0, Pin.IN)

while True:

    # Leer el valor del pin de lectura
    lecturaDigital = pinLectura.value()

    # Mostrar valor digital leido
    print(lecturaDigital)

    # Crear una espera
    time.sleep(0.05)