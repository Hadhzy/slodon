# https://tronche.com/gui/x/xlib/pixmap-and-cursor/
# https://tronche.com/gui/x/xlib/color/#colormap

__all__ = ["create_color_map"]

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from slodon.slodonix.systems.x.display.display import Display


class _ColorMap:
    def __init__(self, display: Display, screen_number) -> None:
        """
        https://tronche.com/gui/x/xlib/display/display-macros.html#DefaultColormap
        """
        self.display = display
        self.screen_number = screen_number


def create_color_map(display: Display, w, visual, alloc: int) -> _ColorMap:
    """
    # Based on: https://tronche.com/gui/x/xlib/color/XCreateColormap.html
    ColorMap initialization
        ### Arguments
        - display (str): Specifies the connection to the X server.
        - w (Window): 	Specifies the window on whose screen you want to create a colormap.
        - visual (Visual): If the visual type is not one supported by the screen, a BadMatch error results.
        - alloc (int): 	Specifies the colormap entries to be allocated. You can pass AllocNone or AllocAll.
        ### Returns
            - None
    """

    return _ColorMap(display=display, screen_number=w.screen_number)
