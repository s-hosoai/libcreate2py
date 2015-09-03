# coding: UTF-8

'''
Created on 2015/05/21

@author: hosoai
'''
import sys
import time
import threading
import serial
import os

from sensor import Sensor

class SendThread(threading.Thread):
    def __init__(self, sensor):
        super(SendThread, self).__init__()
        self.running = True
        self.sensor = sensor
        
    def stop(self):
        self.running = False

    def run(self):
        sci = serial.Serial(port="COM2",baudrate=38400, timeout=2)
        while(self.running):
            data = sci.read(2)
            if len(data)!=0:
                sci.write(self.sensor.toByteArray())

class KeyObserver(threading.Thread):
    def __init__(self, sensor, sender):
        super(KeyObserver, self).__init__()
        self.running = True
        self.sensor = sensor
        self.sender = sender
        
    def stop(self):
        self.running = False
        
    def run(self):
        while(self.running):
            os.system("CLS")
            sys.stdout.write("\rbumpsWheeldrops     :"+str(self.sensor.bumpsWheeldrops)+"")
            sys.stdout.write("\t\t\twall                :"+str(self.sensor.wall)+"\n")
            sys.stdout.write("\rcliLeft             :"+str(self.sensor.cliLeft)+"")
            sys.stdout.write("\t\t\tcliFrontLeft        :"+str(self.sensor.cliFrontLeft)+"\n")
            sys.stdout.write("\rcliFrontRight       :"+str(self.sensor.cliFrontRight)+"")
            sys.stdout.write("\t\t\tcliRight            :"+str(self.sensor.cliRight)+"\n")
            sys.stdout.write("\rvirtualWall         :"+str(self.sensor.virtualWall)+"")
            sys.stdout.write("\t\t\tovercurrents        :"+str(self.sensor.overcurrents)+"\n")
            sys.stdout.write("\rdirtDetect          :"+str(self.sensor.dirtDetect)+"")
            sys.stdout.write("\t\t\tunused1             :"+str(self.sensor.unused1)+"\n")
            sys.stdout.write("\rirOpcode            :"+str(self.sensor.irOpcode)+"")
            sys.stdout.write("\t\t\tbuttons             :"+str(self.sensor.buttons)+"\n")
            sys.stdout.write("\rdistance            :"+str(self.sensor.distance)+"")
            sys.stdout.write("\t\t\tangle               :"+str(self.sensor.angle)+"\n")
            sys.stdout.write("\rchargingState       :"+str(self.sensor.chargingState)+"")
            sys.stdout.write("\t\t\tvoltage             :"+str(self.sensor.voltage)+"\n")
            sys.stdout.write("\rcurrent             :"+str(self.sensor.current)+"")
            sys.stdout.write("\t\t\ttemperature         :"+str(self.sensor.temperature)+"\n")
            sys.stdout.write("\rbatteryCharge       :"+str(self.sensor.batteryCharge)+"")
            sys.stdout.write("\t\t\tbatteryCapacity     :"+str(self.sensor.batteryCapacity)+"\n")
            sys.stdout.write("\rwallSignal          :"+str(self.sensor.wallSignal)+"")
            sys.stdout.write("\t\t\tcliLeftSignal       :"+str(self.sensor.cliLeftSignal)+"\n")
            sys.stdout.write("\rcliFrontLeftSignal  :"+str(self.sensor.cliFrontLeftSignal)+"")
            sys.stdout.write("\t\t\tcliFrontRightSignal :"+str(self.sensor.cliFrontRightSignal)+"\n")
            sys.stdout.write("\rcliRightSignal      :"+str(self.sensor.cliRightSignal)+"")
            sys.stdout.write("\t\t\tunused2             :"+str(self.sensor.unused2)+"\n")
            sys.stdout.write("\runused3             :"+str(self.sensor.unused3)+"")
            sys.stdout.write("\t\t\tchargerAvailable    :"+str(self.sensor.chargerAvailable)+"\n")
            sys.stdout.write("\ropenInterfaceMode   :"+str(self.sensor.openInterfaceMode)+"")
            sys.stdout.write("\t\t\tsongNumber          :"+str(self.sensor.songNumber)+"\n")
            sys.stdout.write("\rsongPlaying         :"+str(self.sensor.songPlaying)+"")
            sys.stdout.write("\t\t\toiStreamNumPackets  :"+str(self.sensor.oiStreamNumPackets)+"\n")
            sys.stdout.write("\rvelocity            :"+str(self.sensor.velocity)+"")
            sys.stdout.write("\t\t\tradius              :"+str(self.sensor.radius)+"\n")
            sys.stdout.write("\rvelocityRight       :"+str(self.sensor.velocityRight)+"")
            sys.stdout.write("\t\t\tvelocityLeft        :"+str(self.sensor.velocityLeft)+"\n")
            sys.stdout.write("\rencoderCountsLeft   :"+str(self.sensor.encoderCountsLeft)+"")
            sys.stdout.write("\t\t\tencoderCountsRight  :"+str(self.sensor.encoderCountsRight)+"\n")
            sys.stdout.write("\rlightBumper         :"+str(self.sensor.lightBumper)+"")
            sys.stdout.write("\t\t\tlightBumpLeft       :"+str(self.sensor.lightBumpLeft)+"\n")
            sys.stdout.write("\rlightBumpFrontLeft  :"+str(self.sensor.lightBumpFrontLeft)+"")
            sys.stdout.write("\t\t\tlightBumpCenterLeft :"+str(self.sensor.lightBumpCenterLeft)+"\n")
            sys.stdout.write("\rlightBumpCenterRight:"+str(self.sensor.lightBumpCenterRight)+"")
            sys.stdout.write("\t\t\tlightBumpFrontRight :"+str(self.sensor.lightBumpFrontRight)+"\n")
            sys.stdout.write("\rlightBumpRight      :"+str(self.sensor.lightBumpRight)+"")
            sys.stdout.write("\t\t\tirOpcodeLeft        :"+str(self.sensor.irOpcodeLeft)+"\n")
            sys.stdout.write("\rirOpcodeRight       :"+str(self.sensor.irOpcodeRight)+"")
            sys.stdout.write("\t\t\tleftMotorCurrent    :"+str(self.sensor.leftMotorCurrent)+"\n")
            sys.stdout.write("\rrightMotorCurrent   :"+str(self.sensor.rightMotorCurrent)+"")
            sys.stdout.write("\t\t\tmainBrushCurrent    :"+str(self.sensor.mainBrushCurrent)+"\n")
            sys.stdout.write("\rsideBrushCurrent    :"+str(self.sensor.sideBrushCurrent)+"")
            sys.stdout.write("\t\t\tstasis              :"+str(self.sensor.stasis)+"\n")
            sys.stdout.write("\n")
            sys.stdout.write("Update sensor value :  > sensorName value \n")
            sys.stdout.write("Exit  : > exit\n")
            raw = raw_input(">")
            temp = raw.split(" ")
            if(temp[0]=="exit"):
                self.sender.stop()
                self.stop()
                sys.exit()
                break
            elif(len(temp)>1):
                command = temp[0][0].lower() + temp[0][1:]
                arg = temp[1] 
                try:
                    if getattr(self.sensor, command) != None:
                        setattr(self.sensor, command, int(arg))
                        sys.stdout.write("\r update!")
                        time.sleep(0.2)
                except AttributeError:
                    pass
                except ValueError:
                    pass

def main():
    data = Sensor()
    sender = SendThread(data)
    sender.start()
    key = KeyObserver(data, sender)
    key.start()

if __name__ == '__main__':
    main()
