# By: Jonathan Ord

from machine import Pin

# Configurar los pines
sensor_sonido = Pin(0, Pin.IN)
led = Pin(15, Pin.OUT)

while(True):
    
    # Leer el valor 1 - 0  del sensor de sonido
    valor_digital = sensor_sonido.value()

    # Aplicar el valor leido al pin del LED
    led.value(valor_digital)
