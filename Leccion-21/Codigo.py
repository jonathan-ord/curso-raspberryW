from machine import Pin, PWM
import time

control_velocidad = PWM(Pin(0, Pin.OUT), freq=1000)
giro1 = Pin(1, Pin.OUT)
giro2 = Pin(2, Pin.OUT)

#  Rango de velocidades
#   | 15000 | 65535 |

velocidad_giro  = 65535

# Crear funciones para controlar el sentido de giro del motor

def giro_izquierda():
    giro1.on()
    giro2.off()
    control_velocidad.duty_u16(velocidad_giro)
    
def giro_derecha():
    giro1.off()
    giro2.on()
    control_velocidad.duty_u16(velocidad_giro)

def detener_motor():
    giro1.off()
    giro2.off()
    
# Ciclo principal
while(True):
    
    giro_izquierda()
    time.sleep_ms(3000)
    detener_motor()
    time.sleep_ms(3000)
    giro_derecha()
    time.sleep_ms(3000)
    detener_motor()
    time.sleep_ms(3000)


