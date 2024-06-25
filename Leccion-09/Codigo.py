from machine import Pin, PWM, ADC

# Crear una variable para leer el valor del divisor de voltaje
PinLectura = ADC(Pin(28))

# Crear una variable para usarla como PWM para encender o apagar el  LED
pinLed_pwm = PWM(Pin(0, Pin.OUT), freq=1000)

while True:

    # Leer con el ADC el valor del divisor de voltaje
    valorLeido = PinLectura.read_u16()

    # Crear una variable para usarla como ciclo de trabajo con el PWM
    # Usar la ecuación punto-pendiente para realizar el mapeo
    valor = int((65535 / 18000) * (valorLeido - 39000) + 0)

    # Usar una condicional para usar solo valores en el rango
    if valor >= 0 and valor <= 65535:

        # Encender el LED con el valor usando el PWM
        pinLed_pwm.duty_u16(valor)