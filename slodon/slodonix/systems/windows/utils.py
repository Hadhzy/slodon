from dataclasses import dataclass
import ctypes
import functools

# This project
from slodon.slodonix.systems.windows.constants import *

__all__ = [
    "Position",
    "is_shift_character",
    "send_mouse_event",
    "linear",
    "fail_safe_check",
    "slodonix_check",
]


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
    return character.isupper() or character in set('~!@#$%^&*()_+{}|:"<>?') # character is either uppercase or in the set


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


def linear(n):
    """
    Returns ``n``, where ``n`` is the float argument between ``0.0`` and ``1.0``. This function is for the default
    linear tween for mouse moving functions.

    This function was copied from PyTweening module, so that it can be called even if PyTweening is not installed.
    """

    if not 0.0 <= n <= 1.0:
        raise Exception("Argument must be between 0.0 and 1.0.")
    return n


def fail_safe_check(fail_safe: bool = True, instance=None):
    """
    As a safety feature, a fail-safe feature is enabled by default. When a PyAutoGUI
    function is called, if the mouse is in any of the four corners of the primary monitor,
    they will raise a pyautogui.FailSafeException.

    - fail_safe (bool): Whether to use the fail-safe feature or not.
    - instance Desktop instance in order to reach methods like size() and position()
    """

    if fail_safe and tuple(instance.position(_tuple=True)) in FAILSAFE_POINTS: # If the mouse is in any of the four corners of the primary monitor 
        raise Exception(
            "Triggered fail-safe. The fail-safe feature is enabled by default and it takes care of checking whether the mouse is in any of the four corners of the primary monitor during the execution the self.body(). To disable this functionality, set fail_safe to False."
        )


def slodonix_check(instance=None):
    """
    A decorator which can be used over all the methods in Desktop.
    Prevent errors.
    
    """

    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            fail_safe_check(instance=instance)
            return func(*args, **kwargs)

        return wrapper

    return decorator


def normalize_button():
    """
    - https://github.com/asweigart/pyautogui/blob/master/pyautogui/__init__.py#L825-L879C22
    """


def normalize_xy_args():
    pass
