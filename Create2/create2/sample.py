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
create2.drive(200,0)
for i in range(0,1000):
    distance = create2.get_distance()
    print "distance:"+str(distance)+"\tL:"+str(create2.get_left_encoder())+"\tR:"+str(create2.get_right_encoder())
    if(distance>1000):
        break
    time.sleep(0.1)

create2.drive(-200,0)
for i in range(0,1000):
    distance = create2.get_distance()
    print "distance:"+str(distance)+"\tL:"+str(create2.get_left_encoder())+"\tR:"+str(create2.get_right_encoder())
    if(distance<0):
        break
    time.sleep(0.1)
create2.drive(0,0)
