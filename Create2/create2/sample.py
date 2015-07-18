from create2.Create2 import Create2
from create2.sensor import Event
import time
def myEventListener(event):
    pass
    for (e, i) in enumerate(event):
        print i

create2 = Create2("COM5", enableThread=True)
create2.add_event_listener(myEventListener)
time.sleep(10)
#create2.Drive(100, 0)
