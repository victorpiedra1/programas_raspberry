import RPi.GPIO as GPIO
from gpiozero import RGBLED
import time

led = RGBLED(red = 21 , green = 20 , blue = 19)
GPIO.setmode(GPIO.BCM)

GPIO_TRIGGER = 12
GPIO_ECHO = 13

GPIO.setup(GPIO_TRIGGER, GPIO.OUT)
GPIO.setup(GPIO_ECHO, GPIO.IN)

def distance():
    GPIO.output(GPIO_TRIGGER, True)

    time.sleep(0.00001)
    GPIO.output(GPIO_TRIGGER, False)

    StartTime = time.time()
    StopTime = time.time()

    while GPIO.input(GPIO_ECHO) == 0:
        StartTime = time.time()

    while GPIO.input(GPIO_ECHO) == 1:
        StopTime = time.time()
        TimeElapsed = StopTime - StartTime
        distance = (TimeElapsed * 34300) / 2

    return distance

if __name__ == '__main__':
#try:
    while True:
        dist = round(distance(),2)
        print ('distancia = {} cm' .format(dist))
        time.sleep(1)
        if dist <=50:
            led.color=(0,1,1)
        else:
            led.color=(1,0,1)
