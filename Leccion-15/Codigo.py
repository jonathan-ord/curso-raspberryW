from machine import Pin
import time
from dht import DHT11

# Crear el pin usando la clase DHT11
sensor = DHT11(Pin(15))

while(True):
    
    # Actualizar los valores de temperatura y humedad del sensor
    sensor.measure()
    
    # Asignar los valores a las variables
    temp = sensor.temperature()
    hum = sensor.humidity()

    # Mostrar los valores leidos
    print("TEMPERATURA: " + str(temp) + "°C")
    print("HUMEDAD: " + str(hum) + "%")
    print("==================")
    
    # Espera de 2 segundos antes de actualizar el sensor
    time.sleep(2)
