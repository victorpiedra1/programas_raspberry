from gpiozero import RGBLED
from time import sleep

led = RGBLED(red = 21, green = 20, blue = 19)

led.color = (1, 1, 0)

sleep(3)

led.color = (1, 1, 1)