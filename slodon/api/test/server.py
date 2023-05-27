
from collections import UserDict
def ws_handler(base, path):
    print(base, path)


class Test:
    def serve(self, ws_handler, param1):
        base = ""
        _current = ""
        for i in param1:
            if i == "/":
                base = _current
                _current = ""
            _current += i
        uri = _current
        return ws_handler(base, uri)


websocket = Test()

websocket.serve(ws_handler, "localhost/8756/")


class Test:
    def __init__(self):
        self._data = 12



test1 = Test()

def feed(instance):
    instance._data += 1


feed(test1)
print(test1._data)