import slodon.slodonix as slodonix
# with display context manager


class MyApp(slodonix.DisplayAsParent):
    def __init__(self):
        super().__init__()

    def body(self):
        self.move_to(100, 100)

    def trigger_mouse(self, curr_pos):
        print("moved", curr_pos.y)


MyApp().run()
