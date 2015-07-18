# coding: UTF-8
'''
Created on 2015/05/18

@author: hosoai
センサ監視用スレッド
intervalで指定したmsごとに全センサ値を要求する．
取得したセンサ値は保持し，前回取得した値と比較，
差分が合った場合は，リスナー登録されている関数に通知する．
'''
import threading
import time

from sensor import Sensor

class SensorObserver(threading.Thread):
    def __init__(self, sci, interval):
        super(SensorObserver, self).__init__()
        self.sci = sci
        self.interval = interval
        self.running = True
        self.prevSensor = Sensor()
        self.listeners = []

    def add_listener(self, listener):
        self.listeners.append(listener)

    def stop(self):
        self.running = False

    def get_sensor(self):
        return self.sensor

    def get_raw_sensor(self):
        return self.data

    def _request_sensor(self):
        self.sci.flash_input()
        requestBytes = [142, 100]
        self.sci.send(requestBytes)

    def _raise_event(self, eventList):
#        print "Raise Event"
        for listener in self.listeners:
            listener(eventList)

    def run(self):
        while(self.running):
            self._request_sensor()
            self.data = self.sci.read(80)
            self.sensor = Sensor.gen_from_bytes(self.data)
            if self.prevSensor != None:
                eventList = self.sensor.diff(self.prevSensor)
                if (eventList != None and len(eventList)>0):
                    self._raise_event(eventList)
            self.prevSensor = self.sensor
            print self.sensor.wallSignal
            time.sleep(self.interval)

# test
#observer = SensorObserver(serial.Serial("COM6", baudrate=115200, timeout=2), 1)
#observer.start()
