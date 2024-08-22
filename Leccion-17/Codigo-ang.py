from machine import Pin, PWM

# Configrar el pin PWM para el servo motor
servo = PWM(Pin(16, Pin.OUT), freq=50)

while(True):
    # Preguntar el ángulo a ingresar
    ang = int(input(("Ingresa el valor del ángulo: ")))

    # Verificar que el valor este entre 0 y 180

    if(ang >= 0 and ang <= 180):

        # Uso de la ecuación punto pendiente
        pos = (6553 / 180) * ang + 1638
        
        # Asignar el ciclo de trabajo al servo motor
        servo.duty_u16(int(pos))

    else:
        print("\n**** Ingresa un valor entre 0 y 180 ****\n")

