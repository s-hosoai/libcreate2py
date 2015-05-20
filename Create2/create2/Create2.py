from create2.sensor import Sensor
from create2.opcode import Opcode, OI_MODES, Modes
from create2.sensorObserver import SensorObserver
import serial

data = "\x0F\x01\x01\x01\x01\x01\x01\x1D\xFF\xFF\xFF\xFF\xFF\x7F\xFF\x7F\x06\xFF\xFF\xFF\x7F\x7F\xFF\xFF\xFF\xFF\xFF\x03\xFF\x0F\xFF\x0F\xFF\x0F\xFF\x0F\xFF\xFF\xFF\x03\x03\x04\x01\x6C\xF4\x01\xFF\x7F\xF4\x01\xF4\x01\xFF\xFF\xFF\xFF\x7F\xFF\x0F\xFF\x0F\xFF\x0F\xFF\x0F\xFF\x0F\xFF\x0F\xFF\xFF\xFF\x7F\xFF\x7F\xFF\x7F\xFF\x7F\x01"
sensor = Sensor.genFromBytes(data)

print sensor.current

BAUDRATE = 115200
SERIAL_TIMEOUT  = 2
INTERVAL = 1
class Create2:
    def __init__(self, tty="/dev/ttyUSB0"):
        self.serial = serial.Serial(tty, baudrate=BAUDRATE, timeout=SERIAL_TIMEOUT)
        self.observer = SensorObserver(self.serial, INTERVAL)
        self.opcode = Opcode(self.serial)

create2 = Create2("COM6")
create2.setMode(Modes.Safe)
