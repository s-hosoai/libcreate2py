# coding: UTF-8
'''
Created on 2015/05/18
@author: hosoai
センサ用構造体
全センサデータ（PacketID100）で得られる80Byteのバイト列を
この構造体にキャストする．（genFromBytes参照）
'''
from ctypes import c_byte, c_ubyte, c_short, c_ushort, sizeof, BigEndianStructure

PACKET_LENGTH = 80

class Sensor(BigEndianStructure):
    _pack_ = 1
    _fields_ = [
    ("bumpsWheeldrops",c_byte),
    ("wall",c_ubyte),
    ("cliLeft",c_ubyte),
    ("cliFrontLeft",c_ubyte),
    ("cliFrontRight",c_ubyte),
    ("cliRight",c_ubyte),
    ("virtualWall",c_ubyte),
    ("overcurrents",c_ubyte),
    ("dirtDetect",c_ubyte),
    ("unused1",c_ubyte),
    ("irOpcode",c_ubyte),
    ("buttons",c_ubyte),
    ("distance",c_short),
    ("angle",c_short),
    ("chargingState",c_ubyte),
    ("voltage",c_ushort),
    ("current",c_short),
    ("temperature",c_byte),
    ("batteryCharge",c_ushort),
    ("batteryCapacity",c_ushort),
    ("wallSignal",c_ushort),
    ("cliLeftSignal",c_ushort),
    ("cliFrontLeftSignal",c_ushort),
    ("cliFrontRightSignal",c_ushort),
    ("cliRightSignal",c_ushort),
    ("unused2",c_ubyte),
    ("unused3",c_ushort),
    ("chargerAvailable",c_ubyte),
    ("openInterfaceMode",c_ubyte),
    ("songNumber",c_ubyte),
    ("songPlaying",c_ubyte),
    ("oiStreamNumPackets",c_ubyte),
    ("velocity",c_short),
    ("radius",c_short),
    ("velocityRight",c_short),
    ("velocityLeft",c_short),
    ("encoderCountsLeft",c_ushort),
    ("encoderCountsRight",c_ushort),
    ("lightBumper",c_ubyte),
    ("lightBumpLeft",c_ushort),
    ("lightBumpFrontLeft",c_ushort),
    ("lightBumpCenterLeft",c_ushort),
    ("lightBumpCenterRight",c_ushort),
    ("lightBumpFrontRight",c_ushort),
    ("lightBumpRight",c_ushort),
    ("irOpcodeLeft",c_ubyte),
    ("irOpcodeRight",c_ubyte),
    ("leftMotorCurrent",c_short),
    ("rightMotorCurrent",c_short),
    ("mainBrushCurrent",c_short),
    ("sideBrushCurrent",c_short),
    ("stasis",c_ubyte)]

    def __init__(self):
        self.bumpsWheeldrops = 0
        self.wall = 0
        self.cliLeft = 0
        self.cliFrontLeft = 0
        self.cliFrontRight = 0
        self.cliRight = 0
        self.virtualWall = 0
        self.overcurrents = 0
        self.dirtDetect = 0
        self.unused1 = 0
        self.irOpcode = 0
        self.buttons = 0
        self.distance = 0
        self.angle = 0
        self.chargingState = 0
        self.voltage = 0
        self.current = 0
        self.temperature = 0
        self.batteryCharge = 0
        self.batteryCapacity = 0
        self.wallSignal = 0
        self.cliLeftSignal = 0
        self.cliFrontLeftSignal = 0
        self.cliFrontRightSignal = 0
        self.cliRightSignal = 0
        self.unused2 = 0
        self.unused3 = 0
        self.chargerAvailable = 0
        self.openInterfaceMode = 0
        self.songNumber = 0
        self.songPlaying = 0
        self.oiStreamNumPackets = 0
        self.velocity = 0
        self.radius = 0
        self.velocityRight = 0
        self.velocityLeft = 0
        self.encoderCountsLeft = 0
        self.encoderCountsRight = 0
        self.lightBumper = 0
        self.lightBumpLeft = 0
        self.lightBumpFrontLeft = 0
        self.lightBumpCenterLeft = 0
        self.lightBumpCenterRight = 0
        self.lightBumpFrontRight = 0
        self.lightBumpRight = 0
        self.irOpcodeLeft = 0
        self.irOpcodeRight = 0
        self.leftMotorCurrent = 0
        self.rightMotorCurrent = 0
        self.mainBrushCurrent = 0
        self.sideBrushCurrent = 0
        self.stasis = 0

    def toByteArray(self):
        return buffer(self)[:]
#        buf = (c_char*80)
#        memoryview(buf)[:sizeof(f)] = (c_char*sizeof(f)).from_buffer(f)
#        memmove(buf, byref(f), sizeof(f))

    @staticmethod
    def gen_from_bytes(data):
        if len(data)!=sizeof(Sensor):
            return None # or RaiseException
        return Sensor.from_buffer_copy(data)
    
    def diff(self, other):
        eventList = []
        if self.bumpsWheeldrops != other.bumpsWheeldrops : 
            eventList.append(Event.changeBumpsWheeldrops)
            bumps = other.bumpsWheeldrops & 3
            if bumps == 1 : eventList.append(Event.pushBumperLeft)
            if bumps == 2 : eventList.append(Event.pushBumperRight)
            if bumps == 3 : eventList.append(Event.pushBumperCenter)
        if self.wall != other.wall : eventList.append(Event.changeWall)
        if self.cliLeft != other.cliLeft : eventList.append(Event.changeCliLeft)
        if self.cliFrontLeft != other.cliFrontLeft : eventList.append(Event.changeCliFrontLeft)
        if self.cliFrontRight != other.cliFrontRight : eventList.append(Event.changeCliFrontRight)
        if self.cliRight != other.cliRight : eventList.append(Event.changeCliRight)
        if self.virtualWall != other.virtualWall : eventList.append(Event.changeVirtualWall)
        if self.overcurrents != other.overcurrents : eventList.append(Event.changeOvercurrents)
        if self.dirtDetect != other.dirtDetect : eventList.append(Event.changeDirtDetect)
        if self.unused1 != other.unused1 : eventList.append(Event.changeUnused1)
        if self.irOpcode != other.irOpcode : eventList.append(Event.changeIrOpcode)
        if self.buttons != other.buttons : eventList.append(Event.changeButtons)
        if self.distance != other.distance : eventList.append(Event.changeDistance)
        if self.angle != other.angle : eventList.append(Event.changeAngle)
        if self.chargingState != other.chargingState : eventList.append(Event.changeChargingState)
        if self.voltage != other.voltage : eventList.append(Event.changeVoltage)
        if self.current != other.current : eventList.append(Event.changeCurrent)
        if self.temperature != other.temperature : eventList.append(Event.changeTemperature)
        if self.batteryCharge != other.batteryCharge : eventList.append(Event.changeBatteryCharge)
        if self.batteryCapacity != other.batteryCapacity : eventList.append(Event.changeBatteryCapacity)
        if self.wallSignal != other.wallSignal : eventList.append(Event.changeWallSignal)
        if self.cliLeftSignal != other.cliLeftSignal : eventList.append(Event.changeCliLeftSignal)
        if self.cliFrontLeftSignal != other.cliFrontLeftSignal : eventList.append(Event.changeCliFrontLeftSignal)
        if self.cliFrontRightSignal != other.cliFrontRightSignal : eventList.append(Event.changeCliFrontRightSignal)
        if self.cliRightSignal != other.cliRightSignal : eventList.append(Event.changeCliRightSignal)
        if self.unused2 != other.unused2 : eventList.append(Event.changeUnused2)
        if self.unused3 != other.unused3 : eventList.append(Event.changeUnused3)
        if self.chargerAvailable != other.chargerAvailable : eventList.append(Event.changeChargerAvailable)
        if self.openInterfaceMode != other.openInterfaceMode : eventList.append(Event.changeOpenInterfaceMode)
        if self.songNumber != other.songNumber : eventList.append(Event.changeSongNumber)
        if self.songPlaying != other.songPlaying : eventList.append(Event.changeSongPlaying)
        if self.oiStreamNumPackets != other.oiStreamNumPackets : eventList.append(Event.changeOiStreamNumPackets)
        if self.velocity != other.velocity : eventList.append(Event.changeVelocity)
        if self.radius != other.radius : eventList.append(Event.changeRadius)
        if self.velocityRight != other.velocityRight : eventList.append(Event.changeVelocityRight)
        if self.velocityLeft != other.velocityLeft : eventList.append(Event.changeVelocityLeft)
        if self.encoderCountsLeft != other.encoderCountsLeft : eventList.append(Event.changeEncoderCountsLeft)
        if self.encoderCountsRight != other.encoderCountsRight : eventList.append(Event.changeEncoderCountsRight)
        if self.lightBumper != other.lightBumper : eventList.append(Event.changeLightBumper)
        if self.lightBumpLeft != other.lightBumpLeft : eventList.append(Event.changeLightBumpLeft)
        if self.lightBumpFrontLeft != other.lightBumpFrontLeft : eventList.append(Event.changeLightBumpFrontLeft)
        if self.lightBumpCenterLeft != other.lightBumpCenterLeft : eventList.append(Event.changeLightBumpCenterLeft)
        if self.lightBumpCenterRight != other.lightBumpCenterRight : eventList.append(Event.changeLightBumpCenterRight)
        if self.lightBumpFrontRight != other.lightBumpFrontRight : eventList.append(Event.changeLightBumpFrontRight)
        if self.lightBumpRight != other.lightBumpRight : eventList.append(Event.changeLightBumpRight)
        if self.irOpcodeLeft != other.irOpcodeLeft : eventList.append(Event.changeIrOpcodeLeft)
        if self.irOpcodeRight != other.irOpcodeRight : eventList.append(Event.changeIrOpcodeRight)
        if self.leftMotorCurrent != other.leftMotorCurrent : eventList.append(Event.changeLeftMotorCurrent)
        if self.rightMotorCurrent != other.rightMotorCurrent : eventList.append(Event.changeRightMotorCurrent)
        if self.mainBrushCurrent != other.mainBrushCurrent : eventList.append(Event.changeMainBrushCurrent)
        if self.sideBrushCurrent != other.sideBrushCurrent : eventList.append(Event.changeSideBrushCurrent)
        if self.stasis != other.stasis : eventList.append(Event.changeStasis)
        return eventList

class Event(enumerate):
    changeBumpsWheeldrops = 1
    changeWall = 2
    changeCliLeft = 3
    changeCliFrontLeft = 4
    changeCliFrontRight = 5
    changeCliRight = 6
    changeVirtualWall = 7
    changeOvercurrents = 8
    changeDirtDetect = 9
    changeUnused1 = 10
    changeIrOpcode = 11
    changeButtons = 12
    changeDistance = 13
    changeAngle = 14
    changeChargingState = 15
    changeVoltage = 16
    changeCurrent = 17
    changeTemperature = 18
    changeBatteryCharge = 19
    changeBatteryCapacity = 20
    changeWallSignal = 21
    changeCliLeftSignal = 22
    changeCliFrontLeftSignal = 23
    changeCliFrontRightSignal = 24
    changeCliRightSignal = 25
    changeUnused2 = 26
    changeUnused3 = 27
    changeChargerAvailable = 28
    changeOpenInterfaceMode = 29
    changeSongNumber = 30
    changeSongPlaying = 31
    changeOiStreamNumPackets = 32
    changeVelocity = 33
    changeRadius = 34
    changeVelocityRight = 35
    changeVelocityLeft = 36
    changeEncoderCountsLeft = 37
    changeEncoderCountsRight = 38
    changeLightBumper = 39
    changeLightBumpLeft = 40
    changeLightBumpFrontLeft = 41
    changeLightBumpCenterLeft = 42
    changeLightBumpCenterRight = 43
    changeLightBumpFrontRight = 44
    changeLightBumpRight = 45
    changeIrOpcodeLeft = 46
    changeIrOpcodeRight = 47
    changeLeftMotorCurrent = 48
    changeRightMotorCurrent = 49
    changeMainBrushCurrent = 50
    changeSideBrushCurrent = 51
    changeStasis = 52
    reachDistance = 53
    reachAngle = 54
    timeout = 55
    pushBumperLeft = 56
    pushBumperCenter = 57
    pushBumperRight = 58
