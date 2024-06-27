from machine import Pin, PWM

# Crear variables para usar los pines
tactil = Pin(0, Pin.IN)
led = PWM(Pin(2, Pin.OUT), freq=1000)

# Variables para el funcionamiento del código
estado = 0
cont = 0
intensidad = [0, 21845, 43690, 65535]

# Variables de verificación
sensor_presionado = False

while True:
    # Leer el valor del sensor táctil
    estado = tactil.value()

    # Si el botón táctil se presiona
    if estado == 1 and sensor_presionado == False:
        cont += 1
        # Aumentar el contador solamente hasta 3
        if cont > 3:
            cont = 0
        sensor_presionado = True
    
    # Si el botón táctil se suelta
    if estado == 0:
        sensor_presionado = False

    # Agregar el valor de intensidad en el led
    led.duty_u16(intensidad[cont])
