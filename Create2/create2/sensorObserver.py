'''
Created on 2015/05/18

@author: hosoai
'''
from threading import Thread
from time import sleep
from create2.sensor import Sensor

class SensorObserver(Thread):
    def __init__(self, serial, interval):
        self.serial = serial
        self.interval = interval
        self.running = True

    def run(self):
        bufCount = 0
        sensorBuf = []
        while(self.running):
            data = "\x0F\x01\x01\x01\x01\x01\x01\x1D\xFF\xFF\xFF\xFF\xFF\x7F\xFF\x7F\x06\xFF\xFF\xFF\x7F\x7F\xFF\xFF\xFF\xFF\xFF\x03\xFF\x0F\xFF\x0F\xFF\x0F\xFF\x0F\xFF\xFF\xFF\x03\x03\x04\x01\x6C\xF4\x01\xFF\x7F\xF4\x01\xF4\x01\xFF\xFF\xFF\xFF\x7F\xFF\x0F\xFF\x0F\xFF\x0F\xFF\x0F\xFF\x0F\xFF\x0F\xFF\xFF\xFF\x7F\xFF\x7F\xFF\x7F\xFF\x7F\x01"
            bufCount = 0 #(bufCount+1)%2
            sensorBuf[bufCount] = Sensor.genFromBytes(data)
            sleep(self.interval)

    def stop(self):
        self.running = False
