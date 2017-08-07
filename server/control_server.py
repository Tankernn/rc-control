#!/usr/bin/python3

import json
from .common import *
from SimpleWebSocketServer import SimpleWebSocketServer, WebSocket

pin_map = {
    87: fwd_pin,    # w
    65: left_pin,   # a
    83: back_pin,   # s
    68: right_pin,  # d
    16: hard_pin    # shift
}

GPIO.setup(list(pin_map.values()), GPIO.OUT)

class SimpleServer(WebSocket):

    def handleMessage(self):
        keys = json.loads(self.data)

        for (key_code, pin) in pin_map.items():
            GPIO.output(pin, key_code in keys)

    def handleConnected(self):
        print(self.address, 'connected')

    def handleClose(self):
        print(self.address, 'closed')
        GPIO.output(pin_map.values(), GPIO.LOW)

server = SimpleWebSocketServer('', 54321, SimpleServer)

if __name__ == '__main__':
    server.serveforever()
