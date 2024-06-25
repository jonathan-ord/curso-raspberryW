from machine import Pin
import time

ledRojo = Pin(0, Pin.OUT)
ledAzul = Pin(1, Pin.OUT)
ledAmarillo = Pin(2, Pin.OUT)

# USO DE VARIABLES
esperaCorta = 60
esperaLarga = 120
esperaEntreCiclo = 500


while(True):

    # Encendido y apagado del led rojo 3 veces [...] {S}
    #1
    ledRojo.on()
    time.sleep_ms(esperaCorta)
    ledRojo.off()
    time.sleep_ms(esperaCorta)
    #2
    ledRojo.on()
    time.sleep_ms(esperaCorta)
    ledRojo.off()
    time.sleep_ms(esperaCorta)
    #3
    ledRojo.on()
    time.sleep_ms(esperaCorta)
    ledRojo.off()
    time.sleep_ms(esperaCorta)

    # Aplicar espera entre el led rojo y el led azul.
    time.sleep_ms(esperaLarga)

    #Encendido y apagado del led azul 3 veces [ - - - ] {O}
    #1
    ledAzul.on()
    time.sleep_ms(esperaLarga)
    ledAzul.off()
    time.sleep_ms(esperaLarga)
    #2
    ledAzul.on()
    time.sleep_ms(esperaLarga)
    ledAzul.off()
    time.sleep_ms(esperaLarga)
    #3
    ledAzul.on()
    time.sleep_ms(esperaLarga)
    ledAzul.off()
    time.sleep_ms(esperaLarga)

    #Encendido y apagado del led amarillo 3 veces [...] {S}
    #1
    ledAmarillo.on()
    time.sleep_ms(esperaCorta)
    ledAmarillo.off()
    time.sleep_ms(esperaCorta)
    #2
    ledAmarillo.on()
    time.sleep_ms(esperaCorta)
    ledAmarillo.off()
    time.sleep_ms(esperaCorta)
    #3
    ledAmarillo.on()
    time.sleep_ms(esperaCorta)
    ledAmarillo.off()
    time.sleep_ms(esperaCorta)


    # Aplicar espera al finalizar [... --- ...]
    time.sleep_ms(esperaEntreCiclo)
