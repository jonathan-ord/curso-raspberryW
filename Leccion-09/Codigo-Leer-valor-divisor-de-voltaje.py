from machine import Pin, ADC
import time

valorLectura = ADC(Pin(28))

espera = 1000

while True:

    valorLeido = valorLectura.read_u16()
    print(valorLeido)

    time.sleep_ms(espera)