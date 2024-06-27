from machine import Pin
import time

# Configurar el pin GPIO con una resistencia de pull-down interna
pulsador = Pin(0, Pin.IN, Pin.PULL_DOWN)
    
while True:

    # Leer el valor del pin (nivel lógico)
    print(pulsador.value())

    # Esperar 100 milisegundos antes de volver a leer
    time.sleep_ms(100)