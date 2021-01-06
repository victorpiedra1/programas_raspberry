import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
BUZZER= 18
buzzState = False
GPIO.setup(BUZZER, GPIO.OUT)


estado = True
numero = 0
valor = 0
while estado == True:
    print (numero)
    numero = numero + 1
    GPIO.output(BUZZER, True)
    if numero == 100:
        valor = int(input('ingresa un numero'))
        GPIO.output(BUZZER, False)
        if valor == 10:
            GPIO.output(BUZZER, False)
            estado = False
        else:
            numero = 0
            estado = True
        
        
