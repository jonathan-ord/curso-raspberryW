from machine import Pin
import uasyncio

led = Pin(0, Pin.OUT)
ledRasp = Pin("LED", Pin.OUT)

# Crear función asíncrona para el led
async def encender_led():
    while True:
        led.on()
        await uasyncio.sleep_ms(800)
        led.off()
        await uasyncio.sleep_ms(800)

# Crear función asíncrona para el led integrado de la Rpw
async def encender_ledRasp():
    while True:
        ledRasp.on()
        await uasyncio.sleep_ms(150)
        ledRasp.off()
        await uasyncio.sleep_ms(150)

# # Crear función principal
async def main():
    await uasyncio.gather(encender_led(), encender_ledRasp())

# Ejecutar la función principal
uasyncio.run(main())
