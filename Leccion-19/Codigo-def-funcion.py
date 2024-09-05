from machine import Pin
import time

# Configurar pin del LED
led_pin = Pin(0, Pin.OUT)

# Crear una funcion sin parametros
def encender_led():
    led_pin.on()
    time.sleep_ms(300)
    led_pin.off()
    time.sleep_ms(300)

# Crear una funcion con parametros
def encender_led_tiempo(espera):
    led_pin.on()
    time.sleep_ms(espera)
    led_pin.off()
    time.sleep_ms(espera)

while(True):
    # Llamar a la función
    # encender_led()
    encender_led_tiempo(150)
    
