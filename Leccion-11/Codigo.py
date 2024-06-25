from machine import Pin, ADC, PWM
import time

# Configuración de los pines del LED RGB
ledRojo = PWM(Pin(0), freq=1000)  
ledVerde = PWM(Pin(1), freq=1000) 
ledAzul = PWM(Pin(2), freq=1000) 

# Configuración del pin de lectura digital del boton PULL-UP
pulsador = Pin(3, Pin.IN)

# Configuración del pin ADC para leer el valor del potenciometro
potenciometro = ADC(28)  

# Crear variable para el tiempo de espera
espera = 250  
# Crear variable para verificar el led seleccionado
cont = 1 

while True:
    # Leer la intensidad del color desde el potenciometro
    IntensidadColor = potenciometro.read_u16()

    # Escalar el valor de IntensidadColor de 0-65535 a 0-100
    IntensidadColor_escala = IntensidadColor * 100 // 65535

    # Incrementar el contador al presionar el botón
    if pulsador.value() == 0:
        cont += 1
    # Verificar que se limite a 3 el contador
    if cont > 3:
        cont = 0

    # Asignar la intensidad del color correspondiente al LED respectivo
    if cont == 1:
        ledRojo.duty_u16(IntensidadColor)
        print("ROJO: " + str(IntensidadColor_escala) + "%")
    elif cont == 2:
        ledVerde.duty_u16(IntensidadColor)
        print("VERDE: " + str(IntensidadColor_escala) + "%")
    elif cont == 3:
        ledAzul.duty_u16(IntensidadColor)
        print("AZUL: " + str(IntensidadColor_escala) + "%")

    # Crear una espera
    time.sleep_ms(espera)
