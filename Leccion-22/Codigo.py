from machine import Pin, PWM
import time
from dht import DHT11

# Crear variables para el sensor de temperatura
sensor = DHT11(Pin(15))
temp = 0

# Crear variables para el motor
control_velocidad = PWM(Pin(0, Pin.OUT), freq=1000)
giro1 = Pin(1, Pin.OUT)
giro2 = Pin(2, Pin.OUT)
velocidad_giro = 65535

# Crear variables para los leds
led_azul = Pin(4, Pin.OUT)
led_rojo = Pin(3, Pin.OUT)

# Función de control del leds
def encender_led_rojo():
    led_rojo.on()
    led_azul.off()
    
def encender_led_azul():
    led_azul.on()
    led_rojo.off()

# Función para leer la temperatura
def leerTemp():
    global temp
    sensor.measure()
    temp = sensor.temperature()
    time.sleep(2)
    print("Temperatura: " + str(temp) + " C")
    
# Función para mover el motor
def motor():
    if temp >= 32:
        encender_led_rojo()
        giro1.on()
        giro2.off()
        control_velocidad.duty_u16(velocidad_giro)
    else:
        encender_led_azul()
        giro1.off()
        giro2.off()

# Ciclo principal
while True:
    leerTemp()
    motor()


