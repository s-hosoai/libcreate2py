'''
Created on 2015/05/18

@author: hosoai
'''
import serial
import struct
from create2.sensor import Sensor

baudrate = 115200
SERIAL_TIMEOUT = 2

serial = serial.Serial(port="COM6",baudrate=baudrate, timeout=SERIAL_TIMEOUT)

serial.write(struct.pack('B', 142))
data = serial.read(80)

sensor = Sensor.gen_from_bytes(data)
print sensor.distance