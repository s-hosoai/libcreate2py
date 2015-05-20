'''
Created on 2015/05/18

@author: hosoai
'''
import struct

OPCODES =dict()

class FunctionTest(object):
    '''
    classdocs
    '''
    def __init__(self, params):
        '''
        Constructor
        '''
        
    
    def __getattr__(self, name):
        """Creates methods for opcodes on the fly.
    
        Each opcode method sends the opcode optionally followed by a string of
        bytes.
    
        """
        if name in self.opcodes:
            def SendOpcode(*bytes):
                self.Send([self.opcodes[name]] + list(bytes))
                return SendOpcode
            raise AttributeError

    def Send(self, bytes):
        with self.lock:
            self.ser.write(struct.pack('B' * len(bytes), *bytes))
