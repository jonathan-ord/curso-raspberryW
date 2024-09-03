from machine import Pin
import time

trigger_pin = Pin(0, Pin.OUT)
echo_pin = Pin(15, Pin.IN)

final, inicio = 0,0

while True:
        # Emitir señal del sensor
        trigger_pin.on()
        time.sleep_ms(10)
        trigger_pin.off()

        # Capturar el inicio y el final de la señal 
        while echo_pin.value() == 0:
            inicio = time.ticks_us()
        while echo_pin.value() == 1:
            final = time.ticks_us()

        distancia = (final - inicio) / 58
        print("Distancia: " + str(int(distancia)) + " Cm")

        time.sleep_ms(500)