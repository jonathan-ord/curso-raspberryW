from machine import ADC, Pin
import time

# Crear una variable con el pin ADC.
pin_analogico = ADC(Pin(28))

# Definir la variable espera.
espera = 500

while True:

    # Leer el valor analógico con el ADC.
    valorLeido = pin_analogico.read_u16()

    # Calcular el voltaje basado en el valor leído.
    voltaje = (3.3 / 65535) * valorLeido

    # Imprimir el valor del voltaje con un decimal.
    print(f"{voltaje:.1f} Voltios")

    # Aplicar una espera
    time.sleep_ms(espera)
