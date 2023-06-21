# https://www.win7dll.info/user32_dll.html
from ctypes import windll as w
import ctypes
# This project
from slodon.slodonix.systems.windows.keyboard_map import full_map as key_map
from slodon.slodonix.systems.windows.utils import *
from slodon.slodonix.systems.windows.structures import POSITION

__all__ = ["Display", "get_os", "DisplayContext"]


class Screen:
    """
    Represent a screen in a display on windows, it contains information about the screen.
    """

    pass


class _Interact:
    """ """

    def __init__(self) -> None:
        """ """

    def key_up(self, key: str) -> None:
        """
        key release
        ### Arguments
            - key (str): The key(FROM UTILS.KEY_NAMES) to release
        ### Returns
            - None
        """

    # Todo: redefine this by using the latest SendInput function
    # noinspection PyMethodMayBeStatic
    def key_down(self, key: str) -> None:
        """
        https://learn.microsoft.com/en-us/windows/win32/api/winuser/nf-winuser-sendinput
        Key press without release
        ### Arguments
          - key (str): The key(FROM UTILS.KEY_NAMES) to press down
        ### Returns
          - None
        """

        if key_map[key] is None:  # the key is not valid
            return

        w.user32.keybd_event(key_map[key], 0, 0, 0)

    def screen(self):
        """ """
        pass

    # noinspection PyMethodMayBeStatic
    def moveto(self, x: int, y: int):
        """
        x-y position of the mouse
        ### Arguments
         - key (str): Return back the mouse position
        ### Returns
         - None
        """
        w.user32.SetCursorPos(x, y)

    def mouse_down(self):
        """ """
        pass

    def mouse_up(self):
        """ """
        pass

    def click(self):
        """ """
        pass

    def mouse_is_swapped(self):
        """ """
        pass

    def send_mouse_event(self):
        """ """
        pass

    def scrool(self):
        """ """
        pass

    def hscrool(self):
        """ """
        pass


class _Info:
    """
    Returns back information about the display
    """

    def get_top_window(self):
        pass

    # noinspection PyMethodMayBeStatic
    def position(self) -> Position:
        """
        x-y position of the mouse
        ### Returns
          - Position object with the x and y coordinates
        """

        pos = POSITION()

        w.user32.GetCursorPos(ctypes.byref(pos))  # fill up the pointer with the information

        return Position(pos.x, pos.y)  # access it from the pointer


class Display:
    """
    Represents a basic display, which is the starting point.
    Acts as a context manager.
    """

    def __init__(self):
        self.interact = _Interact()
        self.info = _Info()


class DisplayContext(Display):
    def __init__(self):
        super().__init__()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass


def get_os() -> str:
    """
    Return back the currently used operating system.
    """
    return "Windows"
