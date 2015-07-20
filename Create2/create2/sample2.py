# coding: UTF-8
import time
import signal
import sys

from create2 import Create2
from sensor import Event
# Ctrl+CでCreate2を停止させるおまじない．
def signal_handler(signal, frame):
    create2.drive(0,0)
    create2.stop()
    sys.exit(0)
signal.signal(signal.SIGINT, signal_handler)

class States(enumerate):
    WAIT_BUTTON = 1
    MOVE_FORWARD = 2
    TURN1 = 3
    TURN2 = 4
    STOP = 5

state = States.INIT
def eventListener(self, events):
    sensor = create2.get_sensor()
    if(state==States.WAIT_BUTTON):
        if(events.containts(Event.changeButtons) and sensor.buttons & 1):
            create2.set_next_distance(500, True)
            create2.drive(100,0)
            state= States.MOVE_FORWARD
    elif(state==States.MOVE_FORWARD):
        if(events.containts(Event.reachDistance)):
            create2.set_next_angle(180, True)
            create2.drive(100,-1)
            state = States.TURN
    elif(state==States.TURN):
        if(events.containts(Event.reachAngle)):
            create2.set_next_distance(500, True)
            create2.drive(100,0)
            state = States.TURN2
    elif(state==States.TURN2):
        if(events.containts(Event.reachDistance)):
            create2.set_next_angle(0, False)
            create2.drive(100,1)
            state = States.STOP
    elif(state==States.STOP):
        if(events.containts(Event.reachAngle)):
            create2.drive(0,0)
            state = States.WAIT_BUTTON
# Initialize
create2 = Create2(threading=True)
create2.add_event_listener(eventListener)
while(True):
    time.sleep(1)
