# TEST hadhzy-python-xlib

from slodon.slodonix import *


class Test(DisplayAsParent):
    def body(self):
        self.move_to(100, 100)
        self.press("b")
        self.type_write("Hello World!")
        print(self.on_screen(100, 100))


Test().run()
