'''
Created on 2015/05/18
@author: hosoai
'''
from _ctypes import Structure, sizeof, byref
from ctypes import c_byte, c_ubyte, c_short, c_ushort, c_char, memmove

PACKET_LENGTH = 80

class Sensor(Structure):
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
        bumpsWheeldrops = 0
        wall = 0
        cliLeft = 0
        cliFrontLeft = 0
        cliFrontRight = 0
        cliRight = 0
        virtualWall = 0
        overcurrents = 0
        dirtDetect = 0
        unused1 = 0
        irOpcode = 0
        buttons = 0
        distance = 0
        angle = 0
        chargingState = 0
        voltage = 0
        current = 0
        temperature = 0
        batteryCharge = 0
        batteryCapacity = 0
        wallSignal = 0
        cliLeftSignal = 0
        cliFrontLeftSignal = 0
        cliFrontRightSignal = 0
        cliRightSignal = 0
        unused2 = 0
        unused3 = 0
        chargerAvailable = 0
        openInterfaceMode = 0
        songNumber = 0
        songPlaying = 0
        oiStreamNumPackets = 0
        velocity = 0
        radius = 0
        velocityRight = 0
        velocityLeft = 0
        encoderCountsLeft = 0
        encoderCountsRight = 0
        lightBumper = 0
        lightBumpLeft = 0
        lightBumpFrontLeft = 0
        lightBumpCenterLeft = 0
        lightBumpCenterRight = 0
        lightBumpFrontRight = 0
        lightBumpRight = 0
        irOpcodeLeft = 0
        irOpcodeRight = 0
        leftMotorCurrent = 0
        rightMotorCurrent = 0
        mainBrushCurrent = 0
        sideBrushCurrent = 0
        stasis = 0
    
    def toByteArray(self, f):
        buf = (c_char*80)
        memoryview(buf)[:sizeof(f)] = (c_char*sizeof(f)).from_buffer(f)
#        memmove(buf, byref(f), sizeof(f))
    @staticmethod
    def genFromBytes(data):
        return Sensor.from_buffer_copy(data)
    
    def diff(self, other):
        eventList = []
        if self.bumpsWheeldrops != other.bumpsWheeldrops : eventList += Event.changeBumpsWheeldrops
        if self.wall != other.wall : eventList += Event.changeWall
        if self.cliLeft != other.cliLeft : eventList += Event.changeCliLeft
        if self.cliFrontLeft != other.cliFrontLeft : eventList += Event.changeCliFrontLeft #
        if self.cliFrontRight != other.cliFrontRight : eventList += Event.changeCliFrontRight
        if self.cliRight != other.cliRight : eventList += Event.changeCliRight
        if self.virtualWall != other.virtualWall : eventList += Event.changeVirtualWall
        if self.overcurrents != other.overcurrents : eventList += Event.changeOvercurrents
        if self.dirtDetect != other.dirtDetect : eventList += Event.changeDirtDetect
        if self.unused1 != other.unused1 : eventList += Event.changeUnused
        if self.irOpcode != other.irOpcode : eventList += Event.changeIrOpcode
        if self.buttons != other.buttons : eventList += Event.changeButtons
        if self.distance != other.distance : eventList += Event.changeDistance
        if self.angle != other.angle : eventList += Event.changeAngle
        if self.chargingState != other.chargingState : eventList += Event.changeChargingState
        if self.voltage != other.voltage : eventList += Event.changeVoltage
        if self.current != other.current : eventList += Event.changeCurrent
        if self.temperature != other.temperature : eventList += Event.changeTemperature
        if self.batteryCharge != other.batteryCharge : eventList += Event.changeBatteryCharge
        if self.batteryCapacity != other.batteryCapacity : eventList += Event.changeBatteryCapacity
        if self.wallSignal != other.wallSignal : eventList += Event.changeWallSignal
        if self.cliLeftSignal != other.cliLeftSignal : eventList += Event.changeCliLeftSignal
        if self.cliFrontLeftSignal != other.cliFrontLeftSignal : eventList += Event.changeCliFrontLeftSignal
        if self.cliFrontRightSignal != other.cliFrontRightSignal : eventList += Event.changeCliFrontRightSignal
        if self.cliRightSignal != other.cliRightSignal : eventList += Event.changeCliRightSignal
        if self.unused2 != other.unused2 : eventList += Event.changeUnused
        if self.unused3 != other.unused3 : eventList += Event.changeUnused
        if self.chargerAvailable != other.chargerAvailable : eventList += Event.changeChargerAvailable
        if self.openInterfaceMode != other.openInterfaceMode : eventList += Event.changeOpenInterfaceMode
        if self.songNumber != other.songNumber : eventList += Event.changeSongNumber
        if self.songPlaying != other.songPlaying : eventList += Event.changeSongPlaying
        if self.oiStreamNumPackets != other.oiStreamNumPackets : eventList += Event.changeOiStreamNumPackets
        if self.velocity != other.velocity : eventList += Event.changeVelocity
        if self.radius != other.radius : eventList += Event.changeRadius
        if self.velocityRight != other.velocityRight : eventList += Event.changeVelocityRight
        if self.velocityLeft != other.velocityLeft : eventList += Event.changeVelocityLeft
        if self.encoderCountsLeft != other.encoderCountsLeft : eventList += Event.changeEncoderCountsLeft
        if self.encoderCountsRight != other.encoderCountsRight : eventList += Event.changeEncoderCountsRight
        if self.lightBumper != other.lightBumper : eventList += Event.changeLightBumper
        if self.lightBumpLeft != other.lightBumpLeft : eventList += Event.changeLightBumpLeft
        if self.lightBumpFrontLeft != other.lightBumpFrontLeft : eventList += Event.changeLightBumpFrontLeft
        if self.lightBumpCenterLeft != other.lightBumpCenterLeft : eventList += Event.changeLightBumpCenterLeft
        if self.lightBumpCenterRight != other.lightBumpCenterRight : eventList += Event.changeLightBumpCenterRight
        if self.lightBumpFrontRight != other.lightBumpFrontRight : eventList += Event.changeLightBumpFrontRight
        if self.lightBumpRight != other.lightBumpRight : eventList += Event.changeLightBumpRight
        if self.irOpcodeLeft != other.irOpcodeLeft : eventList += Event.changeIrOpcodeLeft
        if self.irOpcodeRight != other.irOpcodeRight : eventList += Event.changeIrOpcodeRight
        if self.leftMotorCurrent != other.leftMotorCurrent : eventList += Event.changeLeftMotorCurrent
        if self.rightMotorCurrent != other.rightMotorCurrent : eventList += Event.changeRightMotorCurrent
        if self.mainBrushCurrent != other.mainBrushCurrent : eventList += Event.changeMainBrushCurrent
        if self.sideBrushCurrent != other.sideBrushCurrent : eventList += Event.changeSideBrushCurrent
        if self.stasis != other.stasis : eventList += Event.changeStasis

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

sensor = Sensor()
print sensor.stasis
print sensor.toByteArray(sensor)
