import slodon.slodonix as slodonix
# with display context manager


class MyApp(slodonix.DisplayAsParent):
    def __init__(self):
        super().__init__()

    def body(self):
        self.move_to(10, 0)
    
    def trigger_mouse(self, event):
        print("Moving")


MyApp().run()
