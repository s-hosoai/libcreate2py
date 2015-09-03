# coding: UTF-8
import time
import signal
import sys

from create2 import Create2
from sensor import Event

class States(enumerate):
    WAIT_BUTTON = 1
    MOVE_FORWARD = 2
    TURN1 = 3
    TURN2 = 4
    STOP = 5

class Sample2(object):
    def __init__(self):   
        # Ctrl+CでCreate2を停止
        signal.signal(signal.SIGINT, self.signal_handler)
        self.state = States.WAIT_BUTTON
        self.create2 = Create2(threading=True, interval=1000)
        self.create2.add_event_listener(self.eventListener)

    def signal_handler(self, signal, frame):
        self.create2.drive(0,0)
        self.create2.stop()
        sys.exit(0)

    def eventListener(self, events):
        sensor = self.create2.get_sensor()
        if(self.state==States.WAIT_BUTTON):
            if(Event.changeButtons in events and sensor.buttons & 1):
                self.create2.set_next_distance(100, True)
                self.create2.start()
                self.create2.drive(100,0)
                self.state= States.MOVE_FORWARD
                print self.state
        elif(self.state==States.MOVE_FORWARD):
            if(Event.reachDistance in events):
                self.create2.set_next_angle(180, True)
                self.create2.drive(100,1)
                self.state = States.TURN1
                print self.state
        elif(self.state==States.TURN1):
            if(Event.reachAngle in events):
                self.create2.set_next_distance(100, True)
                self.create2.drive(100,0)
                self.state = States.TURN2
                print self.state
        elif(self.state==States.TURN2):
            if(Event.reachDistance in events):
                self.create2.set_next_angle(180, True)
                self.create2.drive(100,1)
                self.state = States.STOP
                print self.state
        elif(self.state==States.STOP):
            if(Event.reachAngle in events):
                self.create2.drive(0,0)
                self.state = States.WAIT_BUTTON
def main():
    sample = Sample2()
    while(True):
#        print sample.create2.get_distance()
#        print sample.create2.get_angle()
        time.sleep(1)

if __name__ == '__main__':
    main()
