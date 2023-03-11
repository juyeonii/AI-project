import serial
import time
import os
from sds011 import SDS011
arduino = serial.Serial('/dev/ttyACM0', 9600)
s = SDS011('/dev/ttyUSB0')
s.sleep(sleep=False)
def get_PM():
    val = s.query()

    PM10 = val[1]

    time.sleep(20)
    return(val[1])

while True:
    pm10 = get_PM()
    f=open('pm.txt','w')
    f.write(PM10)
    f.close
    
    if (pm10<=30):
        c = '1'
        
    elif (30<pm10<150):
        c = '2'
    else : c = '0'
    c = c.encode('utf-8')
    arduino.write(c)

