import sensor
import opcode
import sensorObserver
import serial
import time
import sci

data = "\x0F\x01\x01\x01\x01\x01\x01\x1D\xFF\xFF\xFF\xFF\xFF\x7F\xFF\x7F\x06\xFF\xFF\xFF\x7F\x7F\xFF\xFF\xFF\xFF\xFF\x03\xFF\x0F\xFF\x0F\xFF\x0F\xFF\x0F\xFF\xFF\xFF\x03\x03\x04\x01\x6C\xF4\x01\xFF\x7F\xF4\x01\xF4\x01\xFF\xFF\xFF\xFF\x7F\xFF\x0F\xFF\x0F\xFF\x0F\xFF\x0F\xFF\x0F\xFF\x0F\xFF\xFF\xFF\x7F\xFF\x7F\xFF\x7F\xFF\x7F\x01"
sensor = sensor.Sensor.genFromBytes(data)
print sensor.current

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

    def DriveStright(self, velocity):
        self.opcode.drive()
    
    def DriveStrightWithDistance(self, velocity, distance):
        self.opcode.drive()

    def GetAllRawSensorData(self):
        return self.observer.getRawSensor()
    
    def AddSensorEventListener(self, listener):
        self.observer.addListener(listener)

create2 = Create2()
time.sleep(10)
