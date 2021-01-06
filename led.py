from gpiozero import RGBLED
from time import sleep

led = RGBLED(red = 21, green = 20, blue = 19)

while True:
    letra = input ("""Ingresa la letra correspondiente al color que quieras encender:

    A = Azul
    V = Verde
    R = Rojo
    """)

    if letra == 'A':
        led.color = (1, 1, 0)
    elif letra == 'V':
       led.color = (1, 0, 1)
    elif letra == 'R':
       led.color = (0, 1, 1)
    elif letra == 'O':
        led.color = (1, 1, 1)
    else:
        print('Ingresa una letra valida')
