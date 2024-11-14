from machine import Pin, PWM
import uasyncio as asin
import time

# Configurar los pines que se van a usar en el código
servo_Pin = PWM(Pin(16, Pin.OUT), freq=50)
trigger_pin = Pin(15, Pin.OUT)
echo_pin = Pin(17, Pin.IN)
led_pin = Pin(0, Pin.OUT)

async def ultrasonico():

    while True:
        # Emitir señal del sensor
        trigger_pin.on()
        await asin.sleep_ms(5)
        trigger_pin.off()

        # Capturar el inicio y el final de la señal 
        while echo_pin.value() == 0:
            inicio = time.ticks_us()
        while echo_pin.value() == 1:
            final = time.ticks_us()
        
        # Calcular la duración y convertirla a cm
        distancia_cm = (final - inicio) / 58

        # Verificar si se encontro un objeto
        if distancia_cm < 10:
            led_pin.value(1)  # Encender el LED
        else:
            led_pin.value(0)  # Apagar el LED
        
        # Crear una espera asíncrona
        await asin.sleep_ms(5)

async def servo():
    
    while True:
        # Mover el servo de 0 a 180 grados en incrementos de 4 grados
        for ang in range(0, 180, 4):
            # Convertir el ángulo en ciclo de trabajo
            duty_cycle = int((6553 / 180) * ang + 1638)
            # Asignar el el ciclo de trabajo
            servo_Pin.duty_u16(duty_cycle)
            # Crear una espera antes de mover el servo al siguiente ángulo
            await asin.sleep_ms(50)  

        for ang in range(180, 0, -4):
            duty_cycle = int((6553 / 180) * ang + 1638)
            servo_Pin.duty_u16(duty_cycle)
            await asin.sleep_ms(50)

# Crear la funcion main [PRINCIPAL]
async def main():
    # Ejecutar las funciones al mismo tiempo
    await asin.gather(ultrasonico(), servo())

# Iniciar la ejecución
asin.run(main())

