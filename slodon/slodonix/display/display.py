"""Basic display"""

import types
import os


def open_display(name=os.environ['DISPLAY']):
    """
    Open a display

    Returns a display object
    """
    return Display(name=name)


class Display:
    """
    Represents a basic display

    A set of screens for a single user with one keyboards and one pointer(usually a mouse) is called a display.
    """
    def __init__(self, name):
        pass