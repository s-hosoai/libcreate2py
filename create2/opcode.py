# coding: UTF-8

'''
Created on 2015/05/18
@author: hosoai
Create2のコマンド用クラス．
Create2に送信するコマンド類は，CREATE_OPECODESをリフレクション追加．
各コマンドが呼ばれると，マップされているOPCODE番号と引数がCreateに送信される
'''

CREATE_OPCODES = dict(
    softReset = 7,
    start = 128,
    baud = 129,
    control = 130,
    safe = 131,
    full = 132,
    power = 133,
    spot = 134,
    clean = 135,
    maxClean = 136,
    drive = 137,
    motors = 138,
    leds = 139,
    song = 140,
    play = 141,
    query = 142,
    forceSeekingDock = 143,
    pwmMotors = 144,
    driveWheels = 145,
    drivePwm = 146,
    stream = 148,
    queryList = 149,
    doStream = 150,
    schedulingLeds = 162,
    digitLedsRaw = 163,
    digitLedsAscii = 164,
    buttons = 165,
    schedule = 167,
    setDayTime = 168,
    stop = 173
)
BAUD_RATES = (  # In bits per second.
    300,
    600,
    1200,
    2400,
    4800,
    9600,
    14400,
    19200,
    28800,
    38400,
    57600,  # Default.
    115200)

CHARGING_STATES = (
    'not-charging',
    'charging-recovery',
    'charging',
    'trickle-charging',
    'waiting',
    'charging-error')

OI_MODES = (
    'off',
    'passive',
    'safe',
    'full')

class Modes(enumerate):
    OFF=0
    Passive=1
    Safe=2
    Full=4
# From: http://www.harmony-central.com/MIDI/Doc/table2.html
MIDI_TABLE = {'rest': 0, 'R': 0, 'pause': 0,
              'G1': 31, 'G#1': 32, 'A1': 33,
              'A#1': 34, 'B1': 35,

              'C2': 36, 'C#2': 37, 'D2': 38,
              'D#2': 39, 'E2': 40, 'F2': 41,
              'F#2': 42, 'G2': 43, 'G#2': 44,
              'A2': 45, 'A#2': 46, 'B2': 47,

              'C3': 48, 'C#3': 49, 'D3': 50,
              'D#3': 51, 'E3': 52, 'F3': 53,
              'F#3': 54, 'G3': 55, 'G#3': 56,
              'A3': 57, 'A#3': 58, 'B3': 59,

              'C4': 60, 'C#4': 61, 'D4': 62,
              'D#4': 63, 'E4': 64, 'F4': 65,
              'F#4': 66, 'G4': 67, 'G#4': 68,
              'A4': 69, 'A#4': 70, 'B4': 71,

              'C5': 72, 'C#5': 73, 'D5': 74,
              'D#5': 75, 'E5': 76, 'F5': 77,
              'F#5': 78, 'G5': 79, 'G#5': 80,
              'A5': 81, 'A#5': 82, 'B5': 83,

              'C6': 84, 'C#6': 85, 'D6': 86,
              'D#6': 87, 'E6': 88, 'F6': 89,
              'F#6': 90, 'G6': 91, 'G#6': 92,
              'A6': 93, 'A#6': 94, 'B6': 95,

              'C7': 96, 'C#7': 97, 'D7': 98,
              'D#7': 99, 'E7': 100, 'F7': 101,
              'F#7': 102, 'G7': 103, 'G#7': 104,
              'A7': 105, 'A#7': 106, 'B7': 107,

              'C8': 108, 'C#8': 109, 'D8': 110,
              'D#8': 111, 'E8': 112, 'F8': 113,
              'F#8': 114, 'G8': 115, 'G#8': 116,
              'A8': 117, 'A#8': 118, 'B8': 119,

              'C9': 120, 'C#9': 121, 'D9': 122,
              'D#9': 123, 'E9': 124, 'F9': 125,
              'F#9': 126, 'G9': 127}

class Opcode(object):
    def __getattr__(self, name):
        """Creates methods for opcodes on the fly.
        Each opcode method sends the opcode optionally followed by a string of
        bytes.
        """
        if name in self.opcodes:
            def SendOpcode(*data):
                self.sci.send([self.opcodes[name]] + list(*data))
            return SendOpcode
            raise AttributeError
    
    def __init__(self, sci):
        self.sci = sci
        self.opcodes = {}
        self.opcodes.update(CREATE_OPCODES)
