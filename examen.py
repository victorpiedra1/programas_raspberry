from gpiozero import RGBLED, Servo
from time import sleep
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
BUZZER= 18
buzzState = False
GPIO.setup(BUZZER, GPIO.OUT)

led = RGBLED(red = 21, green = 20, blue = 19)
servo = Servo(25)

bandera = True
numero = 0
r_user , r_password, v_user, v_password = 0, 0, 0, 0

def exito ():
    print('Exito! usuario y contraseña correctos')
    GPIO.output(BUZZER, False)
    led.color = (1, 0, 1)
    servo.max()
    
def error():
    print('Error! Datos incorrectos, intenta de nuevo')
    GPIO.output(BUZZER, True)
    led.color = (0, 1, 1)
    servo.min()
    

        
if __name__ == "__main__":
   
    r_user = input('Registra tu nombre de usuario: ')
    r_password = input('Registra tu contraseña: ')

    print("Usuario Registrado")

    v_user = input('Ingresa tu nombre de usuario: ')
    v_password = input('Ingresa tu contraseña: ')

    if(r_user == v_user and r_password == v_password):
        exito()
    else:
        error()
        while bandera == True:
            numero = numero+1
            if numero == 100:
                e_user = input('Ingresa de nuevo tu usuario: ')
                e_password = input('Ingresa de nuevo tu contraseña: ')
                if(r_user == e_user and r_password == e_password):
                    bandera = False
                    exito()
                
            
        
    
    