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
import math

from sensor import Sensor

ENC_TO_DISTANCE = 72 * math.pi / 508.8 # タイヤ径72ｯm * Pi / 一周エンコーダ数 ：理論値なので，実計測で調整すること．

class SensorObserver(threading.Thread):
    def __init__(self, sci, interval):
        super(SensorObserver, self).__init__()
        self.sci = sci
        self.interval = interval
        self.running = True
        self.prevSensor = Sensor()
        self.listeners = []
        self.leftEncoder = 0
        self.rightEncoder = 0
        self.totalDistance = 0

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
                
                # 現状Create2からは正しいDistance値が取得できない．
                # エンコーダ値は，正回転でも逆回転でも増加する．オーバーフローの処理後，回転方向に応じて加減し，走行距離に換算する．
                leftDiff = self.sensor.encoderCountsLeft - self.prevSensor.encoderCountsRight
                rightDiff = self.sensor.encoderCountsRight - self.prevSensor.encoderCountsRight    
                # overflow check
                if(leftDiff<0):
                    leftDiff += 65536
                if(rightDiff<0):
                    rightDiff += 65536
                # 回転方向
                if(self.sensor.velocityLeft<0) :
                    leftDiff = -leftDiff
                if(self.sensor.encoderCountsRight<0):
                    rightDiff = -rightDiff
                self.leftEncoder += leftDiff
                self.rightEncoder += rightDiff
                self.totalDistance += (leftDiff + rightDiff)/2 * ENC_TO_DISTANCE
                print "Distance"+str(self.totalDistance)
                
                # distance, angle系イベント
                
            self.prevSensor = self.sensor
            time.sleep(self.interval/1000)

# test
#observer = SensorObserver(serial.Serial("COM6", baudrate=115200, timeout=2), 1)
#observer.start()
