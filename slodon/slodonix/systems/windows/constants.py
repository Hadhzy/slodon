# https://github.com/asweigart/pyautogui/blob/master/pyautogui/_pyautogui_win.py#L35-L56

"""
    Constants for the Windows platform.
    Each of them is represented by hex value. They are used to convey specific information about the event.
    In the Windows API, each event type is associated with a unique numeric constant in this case a hex value.
    For example the constant 0x002 is a specific event type that represents a left mouse button down event. 
    This value is part of the Windows API's set of predefined mouse event constants.
    For example if you were to call a function like mouse_event() that comes from the windows api and pass in the constant 0x002, it would simulate a left mouse button down event.
    Here we are just predefining these constants for later use.
"""

__all__ = [
    "KEYEVENTF_KEYDOWN",
    "KEYEVENTF_KEYUP",
    "LEFT",
    "RIGHT",
    "MIDDLE",
    "MOUSEEVENTF_LEFTDOWN",
    "MOUSEEVENTF_MIDDLEDOWN",
    "MOUSEEVENTF_RIGHTDOWN",
    "MOUSEEVENTF_LEFTUP",
    "MOUSEEVENTF_RIGHTUP",
    "MOUSEEVENTF_MIDDLEUP",
    "MOUSEEVENTF_LEFTCLICK",
    "MOUSEEVENTF_RIGHTCLICK",
    "MOUSEEVENTF_MIDDLECLICK",
    "PRIMARY",
    "FAILSAFE_POINTS",
    "MINIMUM_DURATION",
    "MINIMUM_SLEEP",
    "MOUSEEVENTF_WHEEL",
]

KEYEVENTF_KEYDOWN = (
    0x0000  # keydown event, specifies the key that has been pressed down.
)
KEYEVENTF_KEYUP = 0x0002  # keyup event, specifies the key that has been released.

# Constants for the mouse button names:
LEFT = "left"  # left mouse button
MIDDLE = "middle"  # middle mouse button
RIGHT = "right"  # right mouse button
PRIMARY = "primary"  # primary mouse button
SECONDARY = "secondary"  # secondary mouse button

MINIMUM_DURATION = 0.1  # 100 ms
MINIMUM_SLEEP = 0.05  # 50 ms

# Event codes to be passed into the mouse_event() win32 function.
# Documented here: http://msdn.microsoft.com/en-us/library/windows/desktop/ms646273(v=vs.85).aspx
MOUSEEVENTF_MOVE = 0x0001  # mouse movement
MOUSEEVENTF_LEFTDOWN = 0x0002  # left mouse button down
MOUSEEVENTF_LEFTUP = 0x0004  # left mouse button up
MOUSEEVENTF_LEFTCLICK = (
    MOUSEEVENTF_LEFTDOWN + MOUSEEVENTF_LEFTUP
)  # left mouse button click (down then up = full click)
MOUSEEVENTF_RIGHTDOWN = 0x0008  # right mouse button down
MOUSEEVENTF_RIGHTUP = 0x0010  # right mouse button up
MOUSEEVENTF_RIGHTCLICK = (
    MOUSEEVENTF_RIGHTDOWN + MOUSEEVENTF_RIGHTUP
)  # right mouse button click (down then up = full click)
MOUSEEVENTF_MIDDLEDOWN = 0x0020  # middle mouse button down
MOUSEEVENTF_MIDDLEUP = 0x0040  # middle mouse button up
MOUSEEVENTF_MIDDLECLICK = (
    MOUSEEVENTF_MIDDLEDOWN + MOUSEEVENTF_MIDDLEUP
)  # middle mouse button click (down then up = full click)
MOUSEEVENTF_ABSOLUTE = 0x8000  # defines the absolute coordinates of the mouse event. Read more about it here(under the parameters headline): https://docs.microsoft.com/en-us/windows/win32/api/winuser/ns-winuser-mouseinput
MOUSEEVENTF_WHEEL = 0x0800  # mouse wheel movement
MOUSEEVENTF_HWHEEL = 0x01000  # mouse horizontal wheel movement


FAILSAFE_POINTS = [
    (
        0,
        0,
    )  # Moving the mouse to 0,0 in case of emergency, this will prevent the mouse from moving further, or stuck in a loop.
]  # https://github.com/asweigart/pyautogui/blob/master/pyautogui/__init__.py#L573C27-L573C27
