from slodon.slodonix import *

# with display context manager


class MyApp(DisplayAsParent):
    def __init__(self):
        super().__init__()

    def body(self):
        self.move_to(100, 100, 10)

    def trigger_mouse(self, curr_pos):
        print("moved", curr_pos.y)


MyApp().run()
