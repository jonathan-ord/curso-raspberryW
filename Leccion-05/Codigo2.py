from machine import Pin, PWM
import time

# Declarar el pin en el GPO 0
led = Pin(0, Pin.OUT)

# Configurar el pin como PWM con la frecuencia de 1000 Hz
led_pwm = PWM(led, freq=1000)

# Variable de espera
espera = 5

while True:
    # Inicio del bucle para el encendido gradual del LED
    for i in range(0, 65535, 255):
        led_pwm.duty_u16(i)
        time.sleep_ms(espera)

    # Inicio del bucle para el apagado gradual del LED
    for i in range(65535, 0, -255):
        led_pwm.duty_u16(i)
        time.sleep_ms(espera)
