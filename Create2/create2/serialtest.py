import serial
import time
import sensor

serial = serial.Serial(port="COM6",baudrate=115200, timeout=2)
data = sensor.Sensor()

for i in range(0,10):
	print "sending:"+str(i)
	serial.write(sensor.toByteArray())
	time.sleep(1)