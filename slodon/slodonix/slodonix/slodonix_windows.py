# https://www.win7dll.info/user32_dll.html
# Taken inspiration from: https://github.com/asweigart/pyautogui/blob/master/pyautogui/_pyautogui_win.py
# (pyautogui: see notice.md)
import time
from ctypes import windll as w
import ctypes
from typing import Union, Callable, Any, Sequence
from abc import ABC, abstractmethod

# This project
from slodon.slodonix.systems.windows.keyboard_map import full_map as key_map
from slodon.slodonix.systems.windows.utils import *
from slodon.slodonix.systems.windows.structures import POSITION, SIZE
from slodon.slodonix.systems.windows.constants import *
from slodon.slodonix.slodonix.tween import linear, getPointOnLine
from slodon.slodonix.systems.windows.event import Listener

__all__ = ["Display", "get_os", "DisplayContext", "DisplayAsParent"]

ev = MOUSEEVENTF_LEFTDOWN  # value in hex: 0x0002 -> left mouse button down
ev_up = MOUSEEVENTF_LEFTUP  # value in hex: 0x0004 -> left mouse button up
# value in hex: 0x0002 + 0x0004 -> left mouse button click (down + up = click)
ev_click = MOUSEEVENTF_LEFTCLICK

X_TYPE = Union[int, float, None, tuple]
Y_TYPE = Union[int, float, None]
DURATION_TYPE = Union[float, None]
TWEEN_TYPE = Union[Callable, None]  # Callable -> tween function

KEY_DOWN: bool | str = (
    False  # Represents if a key is down, if so it will be the key name
)
MOUSE_DOWN: bool | str = (
    False  # Represents if a mouse button is down, if so it will be the button name
)


class Screen:
    """
    Represent a screen in a display on windows, it contains information about the screen.
    """

    pass


class _Interact:
    """
    Base class for all interaction functions
    """

    def __init__(self, info) -> None:
        self.info = info

    # noinspection PyMethodMayBeStatic
    def key_up(self, key: str) -> None:
        """
        Performs a keyboard key release  (without the press down beforehand).

        - https://learn.microsoft.com/en-us/windows/win32/inputdev/wm-keyup#parameters
        - https://github.com/asweigart/pyautogui/blob/master/pyautogui/_pyautogui_win.py#L295-L332

        ### Arguments
            - key (str): The key(from key_map) to be released up
        ### Returns
            - None
        """

        if key_map[key] is None:
            return  # the key is not valid

        # check if the key needs shift, meaning that it's either a capital letter or a special character that needs shift to be pressed
        needs_shift = is_shift_character(key)

        # get the mods and the vk_code from the key_map
        mods, vk_code = divmod(key_map[key], 0x100)

        for apply_mod, vk_mod in [
            (mods & 4, 0x12),
            (mods & 2, 0x11),
            (mods & 1 or needs_shift, 0x10),
        ]:  # HANKAKU not supported! mods & 8
            if apply_mod:
                ctypes.windll.user32.keybd_event(vk_mod, 0, 0, 0)  #

        ctypes.windll.user32.keybd_event(vk_code, 0, KEYEVENTF_KEYUP, 0)

        for apply_mod, vk_mod in [
            (mods & 1 or needs_shift, 0x10),
            (mods & 2, 0x11),
            (mods & 4, 0x12),
        ]:  # HANKAKU not supported! mods & 8
            if apply_mod:
                ctypes.windll.user32.keybd_event(
                    vk_mod, 0, KEYEVENTF_KEYUP, 0)

    # Todo: redefine this by using the latest SendInput function
    # noinspection PyMethodMayBeStatic
    def key_down(self, key: str, with_release=False) -> None:
        """
        Performs a keyboard key press down (without the release afterwards).
        - https://learn.microsoft.com/en-us/windows/win32/api/winuser/nf-winuser-sendinput
        - https://github.com/asweigart/pyautogui/blob/master/pyautogui/_pyautogui_win.py#L250-L292
        Key press without release | with release
        ### Arguments
          - key (str): The key(FROM UTILS.KEY_NAMES) to press down
          - with_release (bool): Whether to release the key after press down
        ### Returns
          - None
        """

        if key_map[key] is None:  # the key is not valid
            return

        needs_shift = is_shift_character(key)

        # https://learn.microsoft.com/en-us/windows/win32/inputdev/virtual-key-codes
        mods, vk_code = divmod(key_map[key], 0x100)

        for apply_mod, vk_mod in [
            (mods & 4, 0x12),
            (mods & 2, 0x11),
            (mods & 1 or needs_shift, 0x10),
        ]:  # HANKAKU not supported! mods & 8
            if apply_mod:
                ctypes.windll.user32.keybd_event(
                    vk_mod, 0, KEYEVENTF_KEYDOWN, 0)  #

        ctypes.windll.user32.keybd_event(vk_code, 0, KEYEVENTF_KEYDOWN, 0)
        for apply_mod, vk_mod in [
            (mods & 1 or needs_shift, 0x10),
            (mods & 2, 0x11),
            (mods & 4, 0x12),
        ]:  # HANKAKU not supported! mods & 8
            if apply_mod:
                ctypes.windll.user32.keybd_event(
                    vk_mod, 0, KEYEVENTF_KEYUP, 0)  #

        if with_release:
            self.key_up(key)

    # noinspection PyMethodMayBeStatic
    def moveto(
        self, x: int | None, y: int | None, x_offset, y_offset, duration, tween=linear
    ) -> None:
        """

        Move the mouse to the specified position
        ### Arguments
         - x (int): x position of the mouse
         - y (int): y position of the mouse
         - tween (Callable): The tween function to use
         - duration (float): The amount of time it takes to move the mouse
         - x_offset (int): The x offset of the mouse(how  far left and right move the mouse)
         - y_Offset (int): The y offset of the mouse (how far up and down move the mouse)
         (https://pyautogui.readthedocs.io/en/latest/mouse.html#tween-easing-functions

        ### Returns
         - None
        """
        x_offset = int(x_offset) if x_offset is not None else 0
        y_offset = int(y_offset) if y_offset is not None else 0

        if x is None and y is None and x_offset == 0 and y_offset == 0:
            return  # Special case for no mouse movement at all.

        _position = self.info.position()
        start_x, start_y = _position.x, _position.y

        x = int(x) if x is not None else start_x
        y = int(y) if y is not None else start_y

        x += x_offset
        y += y_offset

        _size = self.info.size()
        width, height = _size.cx, _size.cy

        steps = [(x, y)]

        sleep_amount = MINIMUM_SLEEP

        if duration > MINIMUM_DURATION:
            num_steps = max(width, height)
            sleep_amount = duration / num_steps
            if sleep_amount < MINIMUM_SLEEP:
                num_steps = int(duration / MINIMUM_SLEEP)
                sleep_amount = duration / num_steps

            steps = [
                getPointOnLine(start_x, start_y, x, y, tween(n / num_steps))
                for n in range(num_steps)
            ]
            steps.append((x, y))

        for tween_x, tween_y in steps:
            if len(steps) > 1:
                time.sleep(sleep_amount)

            tween_x = int(round(tween_x))
            tween_y = int(round(tween_y))

            if (tween_x, tween_y) not in FAILSAFE_POINTS:
                fail_safe_check(instance=self.info)

            w.user32.SetCursorPos(tween_x, tween_y)

        w.user32.SetCursorPos(x, y)

    # noinspection PyMethodMayBeStatic
    def mouse_down(self, x=None, y=None, button=LEFT, with_release=False) -> None:
        """
        - https://docs.microsoft.com/en-us/windows/win32/api/winuser/nf-winuser-mouse_event
        - https://github.com/asweigart/pyautogui/blob/master/pyautogui/_pyautogui_win.py#L375-L401

        ### Arguments
          - x (int): The x position of the mouse
          - y (int): The y position of the mouse
          - button (str): The button to press down
        ### Returns
          - None
        """
        global ev
        if button not in (LEFT, MIDDLE, RIGHT):
            raise ValueError(
                'button arg to _click() must be one of "left", "middle", or "right", not %s'
                % button
            )

        if button == LEFT:
            ev = MOUSEEVENTF_LEFTDOWN  # value in hex: 0x0002
        elif button == MIDDLE:
            ev = MOUSEEVENTF_MIDDLEDOWN  # value in hex: 0x0020
        elif button == RIGHT:
            ev = MOUSEEVENTF_RIGHTDOWN  # value in hex: 0x0008

        x = int(x) or self.info.position().x
        y = int(y) or self.info.position().y

        try:
            send_mouse_event(ev, x, y, instance=_Info()
                             )  # instance for the size
        except (PermissionError, OSError):
            # TODO: We need to figure out how to prevent these errors,
            #  see https://github.com/asweigart/pyautogui/issues/60
            pass

        if with_release:
            self.mouse_up(x, y, button)

    # noinspection PyMethodMayBeStatic
    def mouse_up(self, x=None, y=None, button=PRIMARY) -> None:
        """
        - https://docs.microsoft.com/en-us/windows/win32/api/winuser/nf-winuser-mouse_event
        - https://github.com/asweigart/pyautogui/blob/master/pyautogui/_pyautogui_win.py#L404-L429
        Args:
            x (int): The x position of the mouse event.
            y (int): The y position of the mouse event.
            button (str): The mouse button, either 'left', 'middle', or 'right'
        Returns:
          None
        """

        global ev_up
        if button not in (LEFT, MIDDLE, RIGHT):
            raise ValueError(
                'button arg to _click() must be one of "left", "middle", or "right", not %s'
                % button
            )

        if button == LEFT:
            ev_up = MOUSEEVENTF_LEFTUP  # value in hex: 0x0004
        elif button == MIDDLE:
            ev_up = MOUSEEVENTF_MIDDLEUP  # value in hex: 0x0040
        elif button == RIGHT:
            ev_up = MOUSEEVENTF_RIGHTUP  # value in hex: 0x0010

        x = int(x) or self.info.position().x
        y = int(y) or self.info.position().y

        try:
            send_mouse_event(ev_up, x, y, instance=_Info())
        except (
            PermissionError,
            OSError,
        ):  # TODO: We need to figure out how to prevent these errors,
            # see https://github.com/asweigart/pyautogui/issues/60
            pass

    # noinspection PyMethodMayBeStatic
    def click(self, x=None, y=None, button=LEFT, clicks=None) -> None:
        """
        - https://learn.microsoft.com/en-us/windows/win32/learnwin32/mouse-clicks
        - https://github.com/asweigart/pyautogui/blob/master/pyautogui/_pyautogui_win.py#L432-L458
        ### Arguments
            - x (int): The x position of the mouse event.
            - y (int): The y position of the mouse event.
            - button (str): The mouse button, either 'left', 'middle', or 'right' or 'scrool'
            - clicks (int): The number of clicks to send
        ### Returns
            - None
        """

        global ev_click
        if button not in (LEFT, MIDDLE, RIGHT):
            raise ValueError(
                'button arg to _click() must be one of "left", "middle", or "right", not %s'
                % button
            )

        if x is None:
            x = self.info.position().x
        if y is None:
            y = self.info.position().y

        if button == LEFT:
            ev_click = MOUSEEVENTF_LEFTCLICK

        if button == MIDDLE:
            ev_click = MOUSEEVENTF_MIDDLECLICK

        if button == RIGHT:
            ev_click = MOUSEEVENTF_RIGHTCLICK

        try:
            if clicks is not None:
                for i in range(clicks):
                    send_mouse_event(ev_click, x, y, instance=_Info())
            send_mouse_event(ev_click, x, y, instance=_Info())

        except (PermissionError, OSError):
            pass

    # noinspection PyMethodMayBeStatic
    def mouse_is_swapped(self):
        """
        - https://learn.microsoft.com/en-us/windows/win32/api/winuser/nf-winuser-getsystemmetrics (SM_SWAPBUTTON)
        - https://github.com/asweigart/pyautogui/blob/master/pyautogui/_pyautogui_win.py#L461

        Nonzero if the meanings of the left and right mouse buttons are swapped; otherwise, 0.
        # TODO - measure the performance of checking this setting for each click.
        """
        return w.user32.GetSystemMetrics(23) != 0

    def on_screen(self, x, y=None):
        """
        - https://github.com/asweigart/pyautogui/blob/master/pyautogui/__init__.py#L789
        Returns True if the given x and y coordinates are on the screen.
        """
        if y is None:
            x, y = x

        return 0 <= x <= self.info.size().cx and 0 <= y <= self.info.size().cy

    def scrool(self, clicks, x=None, y=None):
        """
        - https://github.com/asweigart/pyautogui/blob/master/pyautogui/_pyautogui_win.py#L507
        """
        _pos = self.info.position()
        _size = self.info.size()
        startx, starty = _pos.x, _pos.y
        width, height = _size.cx, _size.cy

        if x is None:
            x = startx
        else:
            if x < 0:
                x = 0
            elif x >= width:
                x = width - 1
        if y is None:
            y = starty
        else:
            if y < 0:
                y = 0
            elif y >= height:
                y = height - 1

        try:
            send_mouse_event(MOUSEEVENTF_WHEEL, x, y,
                             instance=_Info(), dw_data=clicks)
        except (PermissionError, OSError):
            pass

    def hscrool(self, clicks, x=None, y=None):
        """
        - https://github.com/asweigart/pyautogui/blob/master/pyautogui/_pyautogui_win.py#L544
        """

        return self.scrool(clicks, x, y)

    def vscrool(self, clicks, x=None, y=None):
        """
        - https://github.com/asweigart/pyautogui/blob/master/pyautogui/_pyautogui_win.py#L560
        """

        return self.scrool(clicks, x, y)

    def hot_key(self, *args, **kwargs):
        """
        - https://github.com/asweigart/pyautogui/blob/master/pyautogui/__init__.py#L1693
        Performs key down presses on teh arguments passed in order.

        ### Arguments:
            key(s) (str): The series of keys to press, in order. This can also be a
            list of key strings to press.
            interval (float, optional): The number of seconds in between each press.
            0.0 by default, for no pause in between presses.

        ### Returns:
            None
        """
        interval = float(kwargs.get("interval", 0.0))

        if len(args) and isinstance(args[0], Sequence) and not isinstance(args[0], str):
            # Let the user pass a list of strings
            args = tuple(args[0])

        for c in args:
            if len(c) > 1:
                c = c.lower()
            self.key_down(c)
            time.sleep(interval)
        for c in reversed(args):
            if len(c) > 1:
                c = c.lower()
            self.key_up(c)
            time.sleep(interval)


class _Info:
    """
    Returns back information about the display
    """

    def get_top_window(self):
        pass

    # noinspection PyMethodMayBeStatic
    def position(self, _type=float, _tuple=False) -> Position | tuple[Any, Any]:
        """
        x-y position of the mouse
        ##Arguments
            - _type (type): The type of the x and y coordinates
            - _tuple (bool): If True, returns a tuple of the x and y coordinates

        ### Returns
          - Position object with the x and y coordinates

        """

        pos = POSITION()

        w.user32.GetCursorPos(
            ctypes.byref(pos)
        )  # fill up the pointer with the information

        if _tuple:
            return _type(pos.x), _type(pos.y)

        return Position(pos.x, pos.y)  # access it from the pointer

    # noinspection PyMethodMayBeStatic
    def size(self) -> SIZE:
        """
        - https://learn.microsoft.com/en-us/windows/win32/api/windef/ns-windef-size(?)
        - https://github.com/asweigart/pyautogui/blob/master/pyautogui/_pyautogui_win.py#L348-L354
        """
        return SIZE(
            ctypes.windll.user32.GetSystemMetrics(0),
            ctypes.windll.user32.GetSystemMetrics(1),
        )


class Display:
    """
    Represents a basic display, which is the starting point.
    """

    def __init__(self):
        self.info = _Info()
        self._interact = _Interact(
            info=self.info
        )  # SHOULD NOT BE USED DIRECTLY OUTSIDE THE CLASS

    @slodonix_check(instance=_Info())
    def click(self, x=None, y=None, button=LEFT, clicks: int = 1) -> None:
        """
        Click at the specified coordinates.

        left | middle | right
        """
        self._interact.click(x=x, y=y, button=button, clicks=clicks)

    @slodonix_check(instance=_Info())
    def key_press(self, keys: str | list, presses=1, interval=0.0) -> None:
        """
        Performs a keyboard key press down, followed by a release.
        - https://github.com/asweigart/pyautogui/blob/master/pyautogui/__init__.py#L1581
        ### Arguments:
            - keys (str): The key to be pressed. See the [keys](keys.md) page for valid key strings.
            - presses (int): The number of press repetitions. 1 by default.
            - interval (float): The number of seconds in between each key press. 0.0 by default.

        ### Returns:
            - None
        """
        if type(keys) == str:
            if len(keys) > 1:
                keys = keys.lower()
            keys = [keys]

        else:
            lower_keys = []
            for s in keys:
                if len(s) > 1:
                    lower_keys.append(s.lower())
                else:
                    lower_keys.append(s)
            keys = lower_keys
        interval = float(interval)

        for i in range(presses):
            for k in keys:
                self._interact.key_down(k, with_release=True)
            time.sleep(interval)

    @slodonix_check(instance=_Info())
    def type_write(self, message=None, interval=0) -> None:
        """
        Performs a keyboard key press down, followed by a release.
        for each of
        the characters in message.

        The message argument can also be list of strings, in which case any valid
        keyboard name can be used.

        Since this performs a sequence of keyboard presses and does not hold down
        keys, it cannot be used to perform keyboard shortcuts. Use the hotkey()
        function for that.

        ### Arguments:
            message (str, list): If a string, then the characters to be pressed. If a
                list, then the key names of the keys to press in order. The valid names
                are listed in KEYBOARD_KEYS.
            interval (float, optional): The number of seconds in between each press.
                0.0 by default, for no pause in between presses.
        ### Returns:
            None
        """

        if not message:
            return

        if type(message) == list:
            message = "".join(message)

        for char in message:
            if len(char) > 1:
                char.lower()

            self.key_down(char)

            time.sleep(interval)

    @slodonix_check(instance=_Info())
    def key_up(self, key) -> None:
        """
        Performs a keyboard key release  (without the press down beforehand).

        ### Arguments:
            - key (str): The key to be pressed. See the [keys](keys.md) page for valid key strings.

        ### Returns:
            - None
        """

        if len(key) > 1:
            key = key.lower()

        self._interact.key_up(key)

    @slodonix_check(instance=_Info())
    def key_down(self, key, with_release=True) -> None:
        """
        Performs a keyboard key press down (without the release afterwards).

        ### Arguments:
            - key (str): The key to be pressed. See the [keys](keys.md) page for valid key strings.
            - with_release (bool): If True, the key will be released after the press down.
        ### Returns:
            - None
        """
        if len(key) > 1:
            key = key.lower()

        self._interact.key_down(key, with_release=with_release)

    @slodonix_check(instance=_Info())
    def move_to(
        self,
        x: X_TYPE = None,
        y: Y_TYPE = None,
        duration: DURATION_TYPE = 0.0,
        tween: TWEEN_TYPE = linear,
    ):
        """
        Moves the mouse cursor to a point on the screen.

        The x and y parameters detail where the mouse event happens. If None, the
        current mouse position is used. If a float value, it is rounded down. If
        outside the boundaries of the screen, the event happens at edge of the
        screen.

        ### Arguments:
            - x (int): The x position on the screen where the
                click happens. None by default. If tuple, this is used for x and y.

            - y (int): : The y position on the screen where the
                        click happens. None by default.

            - duration (float): The number of seconds to perform the mouse move to the x,y coordinates.
                0, then the mouse cursor is moved
                instantaneously. 0.0 by default.

            - tween (func, optional): The tweening function used if the duration is not
            0. A linear tween is used by default.

        ### Returns:
            None
        """
        self._interact.moveto(
            x, y, duration=duration, x_offset=0, y_offset=0, tween=tween
        )

    @slodonix_check(instance=_Info())
    def mouse_down(
        self,
        x=None,
        y=None,
        button=LEFT,
        tween=linear,
        _pause=True,
        with_release=True,
    ):
        """
        Performs pressing a mouse button down(but not up).

        The x and y parameters detail where the mouse event happens. If None, the
        current mouse position is used. If a float value, it is rounded down. If
        outside the boundaries of the screen, the event happens at edge of the
        screen.

        ### Arguments:
            x (int, float, None, tuple, optional): The x position on the screen where the
                mouse down happens. None by default. If tuple, this is used for x and y.
                If x is a str, it's considered a filename of an image to find on
                the screen with locateOnScreen() and click the center of.
            y (int, float, None, optional): The y position on the screen where the
                mouse down happens. None by default.

            button (str, int, optional): The mouse button pressed down.

        ### Returns:
            - None
        """

        # move the mouse to the x, y coordinates
        self._interact.moveto(x, y, x_offset=0, y_offset=0,
                              duration=0, tween=tween)
        self._interact.mouse_down(
            x, y, button, with_release=with_release
        )  # press the button

    @slodonix_check(instance=_Info())
    def mouse_up(
        self,
        x=None,
        y=None,
        button=PRIMARY,
        tween=linear,
        _pause=True,
    ):
        """
        Performs releasing a mouse button up (but not down beforehand).
        The x and y parameters detail where the mouse event happens. If None, the
        current mouse position is used. If a float value, it is rounded down. If
        outside the boundaries of the screen, the event happens at edge of the
        screen.

        ### Arguments:
            x (int, float, None, tuple, optional): The x position on the screen where the
                mouse up happens. None by default. If tuple, this is used for x and y.
                If x is a str, it's considered a filename of an image to find on
                the screen with locateOnScreen() and click the center of.
            y (int, float, None, optional): The y position on the screen where the
                mouse up happens. None by default.
            button (str, int, optional): The mouse button released.

        Returns:
          None
        """
        self._interact.moveto(x, y, x_offset=0, y_offset=0,
                              duration=0, tween=tween)
        self._interact.mouse_up(x, y, button)  # release the button

    @slodonix_check(instance=_Info())
    def on_screen(self, x: int | Position, y: int = None) -> bool:
        """
        Returns True if the given x and y coordinates are on the screen.

        ### Arguments:
            - x (int): The x-coordinate of the pixel.
            - y (int): The y-coordinate of the pixel. If None, the current mouse cursor position is used.

        ### Returns:
            - bool

        ### Raises:
            - None
        """

        if isinstance(x, Position):
            x, y = x.x, x.y

        return self._interact.on_screen(x, y)

    @slodonix_check(instance=_Info())
    def move_rel(self, x_offset=None, y_offset=None, duration=0.0, tween=linear):
        """
        Moves the mouse cursor to a point on the screen, relative to its current
        position.

        ### Arguments
        x (int, float, None, tuple, optional): How far left (for negative values) or
            right (for positive values) to move the cursor. 0 by default. If tuple, this is used for x and y.
        y (int, float, None, optional): How far up (for negative values) or
            down (for positive values) to move the cursor. 0 by default.
        duration (float, optional): The amount of time it takes to move the mouse
            cursor to the new xy coordinates. If 0, then the mouse cursor is moved
            instantaneously. 0.0 by default.
        tween (func, optional): The tweening function used if the duration is not
            0. A linear tween is used by default.

        ### Returns
            - None
        """
        self._interact.moveto(
            None,
            None,
            x_offset=x_offset,
            y_offset=y_offset,
            duration=duration,
            tween=tween,
        )

    @slodonix_check(instance=_Info())
    def drag_to(self, x=None, y=None, duration=0.0, tween=linear, button=LEFT) -> None:
        """
        Performs a mouse drag (mouse movement while the mouse button is held down) to a
        point on the screen.

        The x and y parameters detail where the mouse event happens. If None, the
        current mouse position is used. If a float value, it is rounded down. If
        outside the boundaries of the screen, the event happens at edge of the
        screen.

        ### Arguments

            x (int, float, None, tuple, optional): How far left (for negative values) or
                right (for positive values) to move the cursor. 0 by default. If tuple, this is used for x and y.
                If x is a str, it's considered a filename of an image to find on
                the screen with locateOnScreen() and click the center of.
            y (int, float, None, optional): How far up (for negative values) or
                down (for positive values) to move the cursor. 0 by default.
                duration (float, optional): The amount of time it takes to move the mouse
                cursor to the new xy coordinates. If 0, then the mouse cursor is moved
                instantaneously. 0.0 by default.
            tween (func, optional): The tweening function used if the duration is not
                0. A linear tween is used by default.
            button (str, int, optional): The mouse button released.


        ### Returns
         - None

        """

        self._interact.mouse_down(
            x=x, y=y, button=button, with_release=False
        )  # not release automatically
        self._interact.moveto(x, y, None, None, duration=duration, tween=tween)
        self._interact.mouse_up(x=x, y=y, button=button)

    @slodonix_check(instance=_Info())
    def drag_rel(self, x=None, y=None, duration=0.0, tween=linear, button=LEFT) -> None:
        """
         Performs a mouse drag (mouse movement while a button is held down) to a
         point on the screen(relative).

        The x and y parameters detail where the mouse event happens. If None, the
         current mouse position is used. If a float value, it is rounded down. If
         outside the boundaries of the screen, the event happens at edge of the
         screen.

        ### Arguments

             x (int, float, None, tuple, optional): How far left (for negative values) or
                    right (for positive values) to move the cursor. 0 by default. If tuple, this is used for x and y.
                    If x is a str, it's considered a filename of an image to find on
                    the screen with locateOnScreen() and click the center of.
             y (int, float, None, optional): How far up (for negative values) or
                    down (for positive values) to move the cursor. 0 by default.
                    duration (float, optional): The amount of time it takes to move the mouse
                    cursor to the new xy coordinates. If 0, then the mouse cursor is moved
                    instantaneously. 0.0 by default.
            tween (func, optional): The tweening function used if the duration is not
                    0. A linear tween is used by default.
            button (str, int, optional): The mouse button released.

            ### Returns
             - None
        """
        self._interact.mouse_down(x=x, y=y, button=button, with_release=False)
        self._interact.moveto(
            None, None, x, y, duration=duration, tween=tween
        )  # only pass in the offset
        self._interact.mouse_up(x=x, y=y, button=button)

    @slodonix_check(instance=_Info())
    def scrool(self, clicks, x=None, y=None):
        """
        Performs a scrool of the mouse scrool wheel

         Whether this is a vertical or horizontal scroll depends on the underlying
        operating system.

        The x and y parameters detail where the mouse event happens. If None, the
        current mouse position is used. If a float value, it is rounded down. If
        outside the boundaries of the screen, the event happens at edge of the
        screen.

        ### Arguments:
             - clicks (int, float): The amount of scrolling to perform.
             -x (int, float, None, tuple, optional): The x position on the screen where the
                click happens. None by default. If tuple, this is used for x and y.
             -y (int, float, None, optional): The y position on the screen where the
             click happens. None by default.

        ### Returns:
             - None
        """
        if type(x) in (tuple, list):
            x, y = x[0], x[1]

        self._interact.scrool(clicks, x, y)

    @slodonix_check(instance=_Info())
    def hscrool(self, clicks, x=None, y=None):
        """
        Performs a scrool of the mouse scrool wheel(horizontal)

         Whether this is a vertical or horizontal scroll depends on the underlying
         operating system.

        The x and y parameters detail where the mouse event happens. If None, the
        current mouse position is used. If a float value, it is rounded down. If
        outside the boundaries of the screen, the event happens at edge of the
        screen.

        ### Arguments:
             - clicks (int, float): The amount of scrolling to perform.
             -x (int, float, None, tuple, optional): The x position on the screen where the
                click happens. None by default. If tuple, this is used for x and y.
             -y (int, float, None, optional): The y position on the screen where the
             click happens. None by default.

        ### Returns:
             - None
        """

        if type(x) in (tuple, list):
            x, y = x[0], x[1]

        self._interact.scrool(clicks, x, y)

    @slodonix_check(instance=_Info())
    def hot_key(self, *args, **kwargs) -> None:
        """
        Presses hotkey combination.

        ### Arguments:
            - *args (str): The hotkey combination to press.
            - **kwargs (dict): The hotkey combination to press.

        ### Returns:
            - None
        """
        self._interact.hot_key(*args, **kwargs)


class DisplayContext(Display):
    def __init__(self):
        super().__init__()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass


class DisplayAsParent(Display, ABC):
    """
    Use the display class as a parent for other classes.
    This class will be used as a parent for classes to use slodonix.
    """

    def __init__(self) -> None:
        super().__init__()
        self.listener = Listener(_Info())  # initialise the listener

    def _add_listeners(self) -> None:
        if hasattr(self, "trigger_mouse"):
            self.listener.add_listener("mouse", "trigger_mouse", self)

    @abstractmethod
    def body(self) -> None:
        """
        Every interaction here
        """

    def run(self) -> None:
        """
        Run the main body of the program.
        Starts event listeners if any.
        """
        self._add_listeners()  # add event listeners

        try:
            self.body()  # run the main body

            Listener.destroy_threads()  # destroy event listeners

        except Exception as e:
            Listener.destroy_threads()  # destroy event listeners
            raise e


def get_os() -> str:
    """
    Returns back the currently used operating system.
    """
    return "Windows"
