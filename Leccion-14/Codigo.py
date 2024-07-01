from machine import ADC
import time

# Configurar el pin ADC
sensor_temperatura = ADC(2)

while True:

    # Leer el valor del pin ADC en 16 bits
    valor_adc = sensor_temperatura.read_u16()
    
    # Convertir el valor del ADC a voltaje (en voltios)
    voltaje = valor_adc * 3.3 / 65535
    
    # Convertir el voltaje a temperatura (en grados Celsius)
    temperatura = int(voltaje * 100)
    
    # Mostrar la temperatura
    print("Temperatura: " + str(temperatura) + "°C")
    
    # Generar una espera
    time.sleep_ms(1000)
