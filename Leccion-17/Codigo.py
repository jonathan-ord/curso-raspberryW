from machine import Pin, PWM
import time

# Configrar el pin PWM para el servo motor
servo = PWM(Pin(16, Pin.OUT), freq=50)

while(True):
    
    # Asignar 0 grados
    servo.duty_u16(1638)
    time.sleep_ms(1500)

    # Asignar 180 grados
    servo.duty_u16(8191)
    time.sleep_ms(1500)
    


