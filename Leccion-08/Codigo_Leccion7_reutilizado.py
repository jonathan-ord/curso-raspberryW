from machine import ADC, Pin
import time

pin_analogico = ADC(Pin(28))
espera = 500

while True:
    valorLeido = pin_analogico.read_u16()
    print(valorLeido)
    time.sleep_ms(espera)
    