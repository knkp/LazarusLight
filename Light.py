from serial import *
from time import *

class ArduinoIF:
    def __init__(self, _Port, _Baud=9600):
        self.Port = _Port
        self.Baud = _Baud
        self.conn = Serial(port=self.Port, baudrate=self.Baud)
       #self.conn.open()
        self.isOpen = self.conn.isOpen()

    def tickHeart(self):
        if self.isOpen:
            print 'port succeeded'
            self.conn.write(b'1')
        else:
            print('port is not open')

    def resetHeart(self):
        if self.isOpen:
            self.conn.write(b'0')
        else:
            print('port is not open')

    def close(self):
        if self.isOpen:
            self.conn.close()
        else:
            print 'port already closed'

if __name__ == '__main__':
    arduino = ArduinoIF(_Port='COM10')
    sleep(2)
    arduino.tickHeart()
    arduino.close()