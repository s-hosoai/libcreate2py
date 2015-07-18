import sensor
import opcode
import sensorObserver
import time
import sci
import struct

# create2 tuning parameters
BAUDRATE = 115200
SERIAL_TIMEOUT  = 2
INTERVAL = 1

class Create2:
    def __init__(self, tty="/dev/ttyUSB0", enableThread=False):
        time.sleep(1)
        self.sci = sci.SerialCommandInterface(tty, baudrate=BAUDRATE, timeout=SERIAL_TIMEOUT)
        self.opcode = opcode.Opcode(self.sci)
        if enableThread:
            self.observer = sensorObserver.SensorObserver(self.sci, INTERVAL)
            self.observer.start()
        self.opcode.start()
        self.opcode.safe()

    def Drive(self, velocity, radius):
        velocity = int(velocity) & 0xffff
        radius = int(radius) & 0xffff
        data = struct.unpack('4B', struct.pack('>2H', velocity, radius))
        self.opcode.drive(data)
    
    def GetAllSensorData(self):
        self.requestSensor()
        self.data = self.sci.read(80)
        return sensor.Sensor.genFromBytes(self.data)
    
    def requestSensor(self):
        self.sci.flash_input()
        requestBytes = [142, 100]
        self.sci.send(requestBytes)

# for multithread
    def GetAllRawSensorData(self):
        return self.observer.getRawSensor()
    def AddSensorEventListener(self, listener):
        self.observer.addListener(listener)
