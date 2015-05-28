from create2.Create2 import Create2
from create2.sensor import Event

def myEventListener(event):
    for (e, i) in enumerate(event):
        print i

create2 = Create2("COM6")
create2.AddSensorEventListener(myEventListener)
