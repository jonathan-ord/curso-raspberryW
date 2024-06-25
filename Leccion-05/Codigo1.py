from machine import Pin, PWM

# Declarar el pin en el GPO 0
pin = Pin(0, Pin.OUT)

# Declarar el pin PWM
pin_pwm = PWM(pin, freq=1000)

while True:
    # Ciclo de trabajo = desde 0 hasta 65535
    # Un ciclo de trabajo del 60% es igual a 39321

    pin_pwm.duty_u16(39321)
