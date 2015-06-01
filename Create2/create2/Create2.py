import sensor
import opcode
import sensorObserver
import serial
import time
import sci
import struct

# create2 tuning parameters

BAUDRATE = 115200
SERIAL_TIMEOUT  = 2
INTERVAL = 1

class Create2:
    def __init__(self, tty="/dev/ttyUSB0", enableThread=True):
        time.sleep(1)
        self.sci = sci.SerialCommandInterface(tty, baudrate=BAUDRATE, timeout=SERIAL_TIMEOUT)
        self.opcode = opcode.Opcode(self.sci)
        if enableThread:
            self.observer = sensorObserver.SensorObserver(self.sci, INTERVAL)
            self.observer.start()

    def Drive(self, velocity, radius):
        velocity = int(velocity) & 0xffff
        radius = int(radius) & 0xffff
        data = struct.unpack('4B', struct.pack('>2H', velocity, radius))
        self.opcode.drive(data)

    def GetAllRawSensorData(self):
        return self.observer.getRawSensor()
    
    def AddSensorEventListener(self, listener):
        self.observer.addListener(listener)
