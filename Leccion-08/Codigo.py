from machine import Pin, ADC  

# Crear una lista de números de pin
lista_pins = [0, 1, 2, 3, 4, 5]  

# Inicializar una lista vacía para almacenar instancias de LED
lista_leds = []  

# Iterar sobre los números de pin en la lista_pins
for numero_pin in lista_pins:  

    # Crear instancias de Pin para LEDs y agregarlas a lista_leds
    lista_leds.append(Pin(numero_pin, Pin.OUT))  

# Crear una instancia de ADC para el pin 28
potenciometro = ADC(Pin(28))  

while True:
    # Leer el valor del potenciómetro
    valor = potenciometro.read_u16()

    # Iterar sobre los valores y los índices en la lista_pins
    for i, valorEnIndice in enumerate(lista_pins):
        
        # Encender o apagar el LED según el valor del potenciómetro
        if valor >= (65000 - i * 10833):
            lista_leds[i].on()
        else:
            lista_leds[i].off()
