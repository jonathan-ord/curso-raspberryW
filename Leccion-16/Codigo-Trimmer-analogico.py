# By: Jonathan Ord
# Canal de YouTube: https://youtube.com/@sr.newAlt

from machine import ADC
import time

# Configurar el Pin ADC
valor_trimmer = ADC(2)

while(True):
    
    # Leer el valor analógico en 16 bits
    valor_analogico = valor_trimmer.read_u16()

    # Mostrar el valor leido
    print(valor_analogico)

    # Crear una espera
    time.sleep_ms(100)

    