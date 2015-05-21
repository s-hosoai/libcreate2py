from ctypes import *
from _ctypes import LoadLibrary, byref

class MyStruct(Structure):
    _fields_ = [("x", c_short),("y", c_short)]
    _pack_ = 1

def test_call_cfunc():
    lib = CDLL("hello.dll")
    lib.hello.restype = c_int
    lib.hello.argtypes = [POINTER(MyStruct)]
    
    arg = MyStruct()
    lib.hello(byref(arg))
    print arg.x

def structureFromByteArray():
    mystruct = MyStruct.from_buffer_copy("\x01\x00\x02\x00")
    print mystruct.x, mystruct.y

structureFromByteArray()