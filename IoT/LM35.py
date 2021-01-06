from gpiozero import MCP3008
from time import sleep

def convert_temp(gen):
    for value in gen:
        yield(value * (3.3 - 0.5)) * 100

adc = MCP3008(channel=0)

for temp in convert_temp(adc.values):
    temp = round(temp,2)
    print('La temperatura es: ', temp, '°C')
    sleep(1)