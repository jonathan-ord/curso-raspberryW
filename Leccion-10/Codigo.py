from machine import Pin
import time

# Crear una varibale con el Pin de entrada
pinLectura = Pin(0, Pin.IN)
# Crear una variable para el led
pinLed = Pin(1, Pin.OUT)

# Guardar el estado anterior del pin de lectura
estado_anterior = 1

while True:

    # Leer el valor del pin de lectura
    lectura = pinLectura.value()

    # Comprobar si hay un cambio de estado y actualizar el LED
    if lectura == 0 and estado_anterior == 1:
        pinLed.toggle()

    # Actualizar el estado anterior
    estado_anterior = lectura

    # Crear una espera
    time.sleep(0.05)