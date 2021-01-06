from gpiozero import Button
from time import sleep

right = Button(6,False)
down = Button(17,False)

while True:
    if right.is_pressed:
        print("Derecha")
        sleep(0.3)
    elif down.is_pressed:
        print("Abajo")
        sleep(0.3)