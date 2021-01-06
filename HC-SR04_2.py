from gpiozero import DistanceSensor
from time import sleep

sensor = DistanceSensor(13,12)

while True:
    print('Distancia: ', sensor.distance*100)
    sleep(1)