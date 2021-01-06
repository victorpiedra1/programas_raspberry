from gpiozero import MCP3008
from time import sleep


adc = MCP3008(channel=0)

#print(adc.values)

for x in adc.values:
    print(x)