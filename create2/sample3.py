# coding: UTF-8
import time
import signal
import sys

from create2 import Create2

# Ctrl+CでCreate2を停止させるおまじない．
def signal_handler(signal, frame):
    create2.drive(0,0)
    create2.stop()
    sys.exit(0)
signal.signal(signal.SIGINT, signal_handler)


create2 = Create2(threading=True)
create2.start()
time.sleep(0.1)
create2.drive(100,-1)
startAngle = create2.get_angle()
for i in range(0,1000):
    angle = create2.get_angle()
    print "angle:"+str(angle)
    if(angle-startAngle < -180):
        break
    time.sleep(0.1)

create2.drive(100,1)
startAngle = create2.get_angle()
for i in range(0,1000):
    angle = create2.get_angle()
    print "angle:"+str(angle)
    if(angle-startAngle > 180):
        break
    time.sleep(0.1)
create2.drive(0,0)
