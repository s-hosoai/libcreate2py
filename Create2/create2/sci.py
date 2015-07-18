# coding: UTF-8
'''
Created on 2015/05/18
@author: hosoai
シリアル用クラス
主にシリアルのロック処理と送受信時のバイト変換を行う
'''
import serial
import threading
import struct
import time

class SerialCommandInterface:
    def __init__(self, com, baudrate, timeout):
        self.ser = serial.Serial(port=com, baudrate=baudrate, timeout=timeout)
        self.lock = threading.RLock()
        
    def send(self, data):
        with self.lock:
            self.ser.write(struct.pack('B' * len(data), *data))

    def read(self, num_bytes):
        with self.lock:
            data = self.ser.read(num_bytes)
            if not data:
                raise Exception
            if len(data) != num_bytes:
                raise Exception
            return data
    
    def flash_input(self):
        self.ser.flushInput()
    
    def wake(self):
        """wake up robot."""
        self.ser.setRTS(0)
        time.sleep(0.25)
        self.ser.setRTS(1)
        time.sleep(1)  # Technically it should wake after 500ms.
