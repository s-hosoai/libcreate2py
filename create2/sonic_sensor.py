import serial
import struct
import binascii
import time

class SonicSensor(object):
    def __init__(self):
        self.ser = serial.Serial('/dev/ttyS0', 9600)
        self.coefficient = 1.0

    def get_value(self):
        self.ser.write("\x22\x00\x00\x22")
        result = self.ser.read(4)
	return struct.unpack(">H",result[1:3])[0] * self.coefficient

    def set_coefficient(self, coefficient):
	self.coefficient = coefficient

