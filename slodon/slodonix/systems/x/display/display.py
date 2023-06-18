"""Basic display"""
from slodon.slodonix.systems.x.protocol.display import BaseDisplay

__all__ = ["open_display", "Display"]


class Display(BaseDisplay):
    """
    Represents a basic display

    A set of screens for a single user with one keyboards and one pointer(usually a mouse) is called a display.
    """

    def __init__(self, display) -> None:
        super().__init__(display=display)


# Todo: if the default name is none or not provided connect to the default display
def open_display(name=None) -> Display:
    """
    Open a display

    name: The name of the display / os.environ["DISPLAY"]

    Display names:
        - UNIX
        - OPEN VMS Display name

    Returns a display object
    """
    return Display(display=name)
