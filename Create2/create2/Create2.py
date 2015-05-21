from create2.sensor import Sensor
from create2.opcode import Opcode, OI_MODES, Modes
from create2.sensorObserver import SensorObserver
import serial
from time import sleep

data = "\x0F\x01\x01\x01\x01\x01\x01\x1D\xFF\xFF\xFF\xFF\xFF\x7F\xFF\x7F\x06\xFF\xFF\xFF\x7F\x7F\xFF\xFF\xFF\xFF\xFF\x03\xFF\x0F\xFF\x0F\xFF\x0F\xFF\x0F\xFF\xFF\xFF\x03\x03\x04\x01\x6C\xF4\x01\xFF\x7F\xF4\x01\xF4\x01\xFF\xFF\xFF\xFF\x7F\xFF\x0F\xFF\x0F\xFF\x0F\xFF\x0F\xFF\x0F\xFF\x0F\xFF\xFF\xFF\x7F\xFF\x7F\xFF\x7F\xFF\x7F\x01"
sensor = Sensor.genFromBytes(data)

print sensor.current

# create2 tuning parameters





BAUDRATE = 115200
SERIAL_TIMEOUT  = 2
INTERVAL = 1

class Create2:
    def __init__(self, tty="/dev/ttyUSB0", enableThread=True):
        sleep(1)
        self.serial = serial.Serial(tty, baudrate=BAUDRATE, timeout=SERIAL_TIMEOUT)
        self.opcode = Opcode(self.serial)
        if enableThread:
            self.observer = SensorObserver(self.serial, INTERVAL)
            self.observer.start()

    def DriveStright(self, velocity):
        self.opcode.drive()
    
    def DriveStrightWithDistance(self, velocity, distance):
        self.opcode.drive()

    def GetAllRawSensorData(self):
        return self.observer.getRawSensor()
    
    def AddSensorEventListener(self, listener):
        self.observer.addListener(listener)

def myListener(eventList):
    print "Event Raised!"

create2 = Create2(tty="COM6")
create2.AddSensorEventListener(myListener)

