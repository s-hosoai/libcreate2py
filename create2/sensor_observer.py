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
from sensor import Event

ENC_TO_DISTANCE = 72 * math.pi / 508.8 # タイヤ径72mm * Pi / 一周エンコーダ数 ：理論値なので，実計測で調整すること．
WHEEL_BASE = 117.5
class SensorObserver(threading.Thread):
    def __init__(self, sci, interval):
        super(SensorObserver, self).__init__()
        self.sci = sci
        self.interval = interval
        self.running = True
        self.sensor = None
        self.prevSensor = None
        self.listeners = []
        self.leftEncoder = 0
        self.rightEncoder = 0
        self.totalDistance = 0
        self.totalAngle = 0
        self.nextDistance=None
        self.nextDistanceCompare=None
        self.nextAngle=None
        self.nextAngleCompare=None
        self.daemon = True

    def add_listener(self, listener):
        self.listeners.append(listener)

    def stop(self):
        self.running = False

    def get_sensor(self):
        return self.sensor
    def get_left_encoder(self):
        return self.leftEncoder
    def get_right_encoder(self):
        return self.rightEncoder
    def get_distance(self):
        return self.totalDistance
    def get_angle(self):
        return self.totalAngle

    def get_raw_sensor(self):
        return self.data

    def _request_sensor(self):
        self.sci.flash_input()
        requestBytes = [142, 100]
        self.sci.send(requestBytes)

    def set_next_distance(self, distance, greater=True):
        self.nextDistance = self.totalDistance + distance
        self.nextDistanceCompare = greater

    def set_next_angle(self, angle, greater=True):
        self.nextAngle = self.totalAngle + angle
        self.nextAngleCompare = greater

    def _raise_event(self, eventList):
        for listener in self.listeners:
            listener(eventList)

    def run(self):
        while(self.running):
            self._request_sensor()
            self.data = self.sci.read(80)
            self.sensor = Sensor.gen_from_bytes(self.data)
            if self.prevSensor :
                eventList = self.sensor.diff(self.prevSensor)
                if (eventList and len(eventList)>0):
                    self._raise_event(eventList)
                
                # 現状Create2からは正しいDistance値が取得できないため，encoderから計算する
                leftDiff = self.sensor.encoderCountsLeft - self.prevSensor.encoderCountsLeft
                rightDiff = self.sensor.encoderCountsRight - self.prevSensor.encoderCountsRight    
                # overflow check
                if(leftDiff<-10000):
                    leftDiff += 65536
                elif(leftDiff>10000):
                    leftDiff -= 65536
                if(rightDiff<-10000):
                    rightDiff += 65536
                elif(rightDiff>10000):
                    rightDiff -= 65536

                self.leftEncoder += leftDiff
                self.rightEncoder += rightDiff
                self.totalDistance += (leftDiff + rightDiff)/2 * ENC_TO_DISTANCE
		
		l = leftDiff * ENC_TO_DISTANCE
		r = rightDiff * ENC_TO_DISTANCE
		angleDiff = -(l-r) * 180/(WHEEL_BASE*2)/math.pi

                self.totalAngle += angleDiff

                # check reachDistance Event
                if(self.nextDistance):
                    if(self.nextDistanceCompare):
                        if(self.totalDistance>self.nextDistance):
                            self.nextDistance=None
                            self.nextDistanceCompare=None
                            self._raise_event([Event.reachDistance])
                            #print "raise reachDistance1"
                    else:
                        if(self.totalDistance<self.nextDistance):
                            self.nextDistance=None
                            self.nextDistanceCompare=None
                            self._raise_event([Event.reachDistance])
                            #print "raise reachDistance2"

                # check reachAngle Event
                if(self.nextAngle):
                    if(self.nextAngleCompare):
                        if(self.totalAngle>self.nextAngle):
                            self.nextAngle=None
                            self.nextAngleCompare=None
                            self._raise_event([Event.reachAngle])
                    else:
                        if(self.totalAngle<self.nextAngle):
                            self.nextAngle=None
                            self.nextAngleCompare=None
                            self._raise_event([Event.reachAngle])
                
            self.prevSensor = self.sensor
            time.sleep(self.interval/1000)
