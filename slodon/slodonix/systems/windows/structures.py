import ctypes
from ctypes import wintypes

# Basic structures
# https://coderslegacy.com/structs-with-python-ctypes/


class MOUSEINPUT(ctypes.Structure):
    """
    https://learn.microsoft.com/en-us/windows/win32/api/winuser/ns-winuser-mouseinput
    """
    _fields_ = [
        ("dx", ctypes.wintypes.LONG),
        ("dy", ctypes.wintypes.LONG),
        ("mouseData", ctypes.wintypes.DWORD),
        ("dwFlags", ctypes.wintypes.DWORD),
        ("time", ctypes.wintypes.DWORD),
        ("dwExtraInfo", ctypes.POINTER(ctypes.wintypes.ULONG)),
    ]


# Todo: Define it by using the new one: https://learn.microsoft.com/en-us/windows/win32/api/winuser/nf-winuser-sendinput
class KEYBDINPUT(ctypes.Structure):
    """
    https://learn.microsoft.com/en-us/windows/win32/api/winuser/ns-winuser-keybdinput
    """
    _fields_ = [
        ("wVk", ctypes.wintypes.WORD),
        ("wScan", ctypes.wintypes.WORD),
        ("dwFlags", ctypes.wintypes.DWORD),
        ("time", ctypes.wintypes.DWORD),
        ("dwExtraInfo", ctypes.POINTER(ctypes.wintypes.ULONG)),
    ]


class HARDWAREINPUT(ctypes.Structure):
    """
    https://learn.microsoft.com/en-us/windows/win32/api/winuser/ns-winuser-hardwareinput
    """
    _fields_ = [
        ("uMsg", ctypes.wintypes.DWORD),
        ("wParamL", ctypes.wintypes.WORD),
        ("wParamH", ctypes.wintypes.DWORD),
    ]


class INPUT(ctypes.Structure):
    """
    https://learn.microsoft.com/en-us/windows/win32/api/winuser/ns-winuser-input
    """
    class _I(ctypes.Union):
        _fields_ = [
            ("mi", MOUSEINPUT),
            ("ki", KEYBDINPUT),
            ("hi", HARDWAREINPUT),
        ]

    _anonymous_ = ("i",)
    _fields_ = [
        ("type", ctypes.wintypes.DWORD),
        ("i", _I),
    ]


class POSITION(ctypes.Structure):
    """
    Position of the mouse structure
    """
    _fields_ = [
        ("x", ctypes.c_long),
        ("y", ctypes.c_long),
    ]


class SIZE(ctypes.Structure):
    """
    Size of the window structure
    """
    _fields_ = [
        ("cx", ctypes.c_long),
        ("cy", ctypes.c_long),
    ]

    def __str__(self) -> str:
        return self.__repr__()

    def __repr__(self) -> str:
        return f"<Size: {self.cx}, {self.cy}>"

