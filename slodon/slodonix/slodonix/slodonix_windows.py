# https://www.win7dll.info/user32_dll.html
from ctypes import windll as w

# This project
from slodon.slodonix.systems.windows.keyboard_map import key_map

__all__ = ["Display", "get_os"]


class Screen:
    """
    Represent a screen in a display on windows, it contains information about the screen.
    """
    pass


class _Interact:
    """

    """
    def __init__(self) -> None:
        """

        """
        pass

    def key_up(self, key) -> None:
        """
         key release
         ### Arguments
            - key (str): The key to release
         ### Returns
            - None
        """

    def key_down(self, key) -> None:
        """
        Key press without release
        ### Arguments
          - key (str): The key to press down
        ### Returns
          - None
        """

    def position(self) -> None:
        """
        x-y position of the mouse
        ### Arguments
          - key (str): Return back the mouse position
        ### Returns
          - None
        """

    def screen(self):
        """

        """
        pass

    def moveto(self):
        """
        x-y position of the mouse
        ### Arguments
         - key (str): Return back the mouse position
        ### Returns
         - None
         """

    def mouse_down(self):
        """

        """
        pass

    def mouse_up(self):
        """

        """
        pass

    def click(self):
        """

        """
        pass

    def mouse_is_swapped(self):
        """

        """
        pass

    def send_mouse_event(self):
        """

        """
        pass

    def scrool(self):
        """

        """
        pass

    def hscrool(self):
        """

        """
        pass


class _Info:
    """
    Returns back information about the display
    """

    def get_top_window(self):
        pass


class Display:
    """

    """
    def __init__(self):
        self.interact = _Interact()
        self.info = _Info()

    def __enter__(self):
        pass

    def __exit__(self):
        pass


def get_os() -> str:
    """
    Return back the currently used operating system.
    """
    return "Windows"
