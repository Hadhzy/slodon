from dataclasses import dataclass
import ctypes

__all__ = ["Position", "is_shift_character", "send_mouse_event"]


@dataclass
class Position:
    x: int  # x coordinate, in pixels
    y: int  # y coordinate, in pixels

    def __str__(self):
        return f"Position(x={self.x}, y={self.y})"

    def __repr__(self):
        return str(self)


def is_shift_character(character: str) -> bool:
    """
    source: https://github.com/asweigart/pyautogui/blob/master/pyautogui/__init__.py#L526-L532
    """
    # NOTE TODO - This will be different for non-qwerty keyboards.
    return character.isupper() or character in set('~!@#$%^&*()_+{}|:"<>?')


def send_mouse_event(ev, x, y, dw_data=0, instance=None):
    """
    - https://github.com/asweigart/pyautogui/blob/master/pyautogui/_pyautogui_win.py#L466C1-L504
    - https://learn.microsoft.com/en-us/windows/win32/api/winuser/nf-winuser-mouse_event

    ### Arguments:
       - ev (int): The win32 code for the mouse event. Use one of the MOUSEEVENTF_*
       constants for this argument.
       - x (int): The x position of the mouse event.
       - y (int): The y position of the mouse event.
       - instance: The info class instance to get the size method from.
        dw_data (int): The argument for mouse_event()'s dwData parameter. So far
        this is only used by mouse scrolling.

    ### Returns:
      None

    """
    assert x is not None and y is not None, "x and y cannot be set to None"
    # mouseStruct = MOUSEINPUT()
    # mouseStruct.dx = x
    # mouseStruct.dy = y
    # mouseStruct.mouseData = ev
    # mouseStruct.time = 0

    # inputStruct = INPUT()
    # inputStruct.mi = mouseStruct
    # inputStruct.type = INPUT_MOUSE
    # ctypes.windll.user32.SendInput(1, ctypes.pointer(inputStruct), ctypes.sizeof(inputStruct))

    # TODO Note: We need to handle additional buttons, which I believe is documented here:
    # https://docs.microsoft.com/en-us/windows/desktop/api/winuser/nf-winuser-mouse_event
    instance_info = instance.size()  # SIZE STRUCTURE
    width, height = instance_info.cx, instance_info.cy

    converted_x = 65536 * x // width + 1
    converted_y = 65536 * y // height + 1
    ctypes.windll.user32.mouse_event(
        ev, ctypes.c_long(converted_x), ctypes.c_long(converted_y), dw_data, 0
    )

    # TODO: Too many false positives with this code: See: https://github.com/asweigart/pyautogui/issues/108
    # if ctypes.windll.kernel32.GetLastError() != 0:
    #    raise ctypes.WinError()
