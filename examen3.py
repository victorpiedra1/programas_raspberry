from gpiozero import RGBLED
from gpiozero import Servo
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

BUZZER = 18
GPIO.setup(BUZZER,GPIO.OUT)
led = RGBLED(red = 21, green = 20, blue = 19)
servo = Servo(25)

bandera = True
numero = 0

def datosCorrectos():
    led.color = (1, 0, 1)
    servo.max()
    GPIO.output(BUZZER,False)
    
def datosIncorrectos():
    led.color = (0, 1, 1)
    servo.min()
    GPIO.output(BUZZER,True)

if __name__ == "__main__":
    r_user = input('Registra tu nombre de usuario: ')
    r_password = input ('Registra tu contraseña: ')
    print('Registro exitoso!')
    v_user = input('Ingresa tu usuario: ')
    v_password = input('Ingresa tu contraseña: ')

    if(r_user == v_user and r_password == v_password):
        print('Validación exitosa')
        datosCorrectos()
        
    else:
        print('Error en validación')
        datosIncorrectos()
        
        while bandera == True:
            numero = numero + 1
            
            if numero == 100:
                e_user = input('Ingresa de nuevo tu usuario: ')
                e_password =  input ('Ingresa de nuevo tu contraseña: ')
                
                if(r_user == e_user and r_password == e_password):
                    print('Validación correcta')
                    datosCorrectos()
                    
                else:
                    print('El error continua')
                    datosIncorrectos()
        
        
        