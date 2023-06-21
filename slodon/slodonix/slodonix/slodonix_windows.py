from ctypes import windll as w
# https://www.win7dll.info/user32_dll.html


class _Interact:
    def __init__(self):
        pass

    def key_up(self, key):
        pass

    def key_down(self, key):
        pass

    def position(self):
        pass

    def size(self):
        pass

    def moveto(self):
        pass

    def mouse_down(self):
        pass

    def mouse_up(self):
        pass

    def click(self):
        pass

    def mouse_is_swapped(self):
        pass

    def send_mouse_event(self):
        pass

    def scrool(self):
        pass

    def hscrool(self):
        pass


class Display:
    def __init__(self):
        self.interact = _Interact()

    def __enter__(self):
        pass

    def __exit__(self):
        pass


