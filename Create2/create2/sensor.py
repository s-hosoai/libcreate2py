'''
Created on 2015/05/18
@author: hosoai
'''
from _ctypes import Structure
from ctypes import c_byte, c_ubyte, c_short, c_ushort

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

    @staticmethod
    def genFromBytes(data):
        return Sensor.from_buffer_copy(data)

class Types(enumerate):
    red=1
    blue=2
    yellow=4
