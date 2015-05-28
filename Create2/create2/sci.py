import serial
import threading
import struct
import time

class SerialCommandInterface:
    def __init__(self, com, baudrate, timeout):
        self.ser = serial.Serial(port=com, baudrate=baudrate, timeout=timeout)
        self.lock = threading.RLock()
        
    def Send(self, data):
        with self.lock:
            self.ser.write(struct.pack('B' * len(data), *data))
    
    def Read(self, num_bytes):
        with self.lock:
            data = self.ser.read(num_bytes)
            if not data:
                raise Exception
            if len(data) != num_bytes:
                raise Exception
            return data
    
    def FlushInput(self):
        self.ser.flushInput()
    
    def Wake(self):
        """Wake up robot."""
        self.ser.setRTS(0)
        time.sleep(0.25)
        self.ser.setRTS(1)
        time.sleep(1)  # Technically it should wake after 500ms.
