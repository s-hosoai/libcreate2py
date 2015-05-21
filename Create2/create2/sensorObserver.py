'''
Created on 2015/05/18

@author: hosoai
'''
from threading import Thread
from time import sleep
from create2.sensor import Sensor, PACKET_LENGTH
import serial
import struct

class SensorObserver(Thread):
    def __init__(self, serial, interval):
        super(SensorObserver, self).__init__()
        self.sci = serial
        self.interval = interval
        self.running = True
        self.prevSensor = None
        self.listeners = {}

    def addListener(self, listener):
        self.listeners += listener
    def stop(self):
        self.running = False
    def getSensor(self):
        return self.sensor
    def getRawSensor(self):
        return self.data
    def requestSensor(self):
        self.sci.flushInput()
        requestBytes = [142, 100]
        self.sci.write(requestBytes)
    def raiseEvent(self, eventList):
        for listener in self.listeners:
            listener(eventList)

    def run(self):
        bufCount = 0
        sensorBuf = []
        while(self.running):
#            self.sci.flashinput()
            self.sci.write([142])
#            struct.Struct.pack('B' * len(bytes), *bytes)
#            self.sci.write()
            self.data = self.sci.read(PACKET_LENGTH)
            #data = "\x0F\x01\x01\x01\x01\x01\x01\x1D\xFF\xFF\xFF\xFF\xFF\x7F\xFF\x7F\x06\xFF\xFF\xFF\x7F\x7F\xFF\xFF\xFF\xFF\xFF\x03\xFF\x0F\xFF\x0F\xFF\x0F\xFF\x0F\xFF\xFF\xFF\x03\x03\x04\x01\x6C\xF4\x01\xFF\x7F\xF4\x01\xF4\x01\xFF\xFF\xFF\xFF\x7F\xFF\x0F\xFF\x0F\xFF\x0F\xFF\x0F\xFF\x0F\xFF\x0F\xFF\xFF\xFF\x7F\xFF\x7F\xFF\x7F\xFF\x7F\x01"
            bufCount = 0 #(bufCount+1)%2
            self.sensor = Sensor.genFromBytes(self.data)
            if self.prevSensor != None:
                eventList = self.sensor.diff(self.prevSensor)
                if (eventList != None and len(eventList)!=0):
                    self.raiseEvent(eventList)
            self.prevSensor = self.sensor
            print self.sensor.distance
            sleep(self.interval)

# test
observer = SensorObserver(serial.Serial("COM6", baudrate=115200, timeout=2), 1)
observer.start()
