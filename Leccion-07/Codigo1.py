from machine import ADC, Pin
import time

# Crear una variable con el pin ADC.
pin_analogico = ADC(Pin(28))

# Definir la variable espera.
espera = 500

while True:

    # Leer el valor analógico con el ADC.
    valorLeido = pin_analogico.read_u16()

    # Imprimir el valor leido por el ADC.
    # print es una funcion para mostrar mensajes en consola.

    print(valorLeido)

    # Aplicar una espera.
    time.sleep_ms(espera)

