# Taken inspiration from: https://github.com/asweigart/pyautogui/blob/master/pyautogui/_pyautogui_x11.py
from abc import ABC
from abc import abstractmethod
from Xlib.display import Display # type: ignore
from Xlib import X # type: ignore
from Xlib.ext.xtest import fake_input # type: ignore
import time
from typing import Sequence
from typing import Union, Callable

# This project
from slodon.slodonix.systems.x.keyboard_map import full_map as key_map
from slodon.slodonix.systems.windows.constants import LEFT, MIDDLE, RIGHT
from slodon.slodonix.systems.x.structures import Position, SIZE
from slodon.slodonix.slodonix.tween import linear
from slodon.slodonix.systems.windows.utils import slodonix_check
from slodon.slodonix.systems.windows.utils import is_shift_character
from slodon.slodonix.systems.windows.event import Listener

X_TYPE = Union[int, float, None, tuple]
Y_TYPE = Union[int, float, None]
DURATION_TYPE = Union[float, None]
TWEEN_TYPE = Union[Callable, None]  # Callable -> tween function
FAILSAFE_POINTS = [(0, 0)]

MINIMUM_SLEEP = 0.05  # 50 ms
MINIMUM_DURATION = 0.1  # 100 ms

_display = Display()  # X-display

BUTTON_NAME_MAPPING = {
    LEFT: 1,
    MIDDLE: 2,
    RIGHT: 3,
    1: 1,
    2: 2,
    3: 3,
    4: 4,
    5: 5,
    6: 6,
    7: 7,
}  # contains all the buttons


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
        Performs a keyboard key release.
        - https://github.com/asweigart/pyautogui/blob/master/pyautogui/_pyautogui_x11.py#L154
        ### Arguments:
            - key: The key to release
        ### Returns:
           - None
        """
        if key_map[key] is None:
            return

        if type(key) == int:
            keycode = key
        else:
            keycode = key_map[key]

        fake_input(_display, X.KeyRelease, keycode)
        _display.sync()

    # noinspection PyMethodMayBeStatic
    def key_down(self, key: str, with_release=True) -> None:
        """
        - https://github.com/asweigart/pyautogui/blob/master/pyautogui/_pyautogui_x11.py#L121
        ### Arguments:
            - key: The key to press(from key_map)
            - with_release: Whether to release the key after pressing it
        ### Returns:
            - None
        """

        if key_map[key] is None:
            return

        if type(key) == int:
            fake_input(_display, X.KeyPress, key)
            _display.sync()
            return

        needs_shift = is_shift_character(key)
        if needs_shift:
            fake_input(_display, X.KeyPress, key_map["shift"])

        fake_input(_display, X.KeyPress, key_map[key])

        if needs_shift:
            fake_input(_display, X.KeyRelease, key_map["shift"])
        _display.sync()

        if with_release:
            self.key_up(key)

    # noinspection PyMethodMayBeStatic
    def moveto(
        self,
        x: int | None,
        y: int | None,
        x_offset=None,
        y_offset=None,
        duration: int | float = 0,
        tween=linear,
    ) -> None:
        """
        - https://github.com/asweigart/pyautogui/blob/master/pyautogui/_pyautogui_x11.py#L100
        ### Arguments:
            - x(int): The x coordinate to move to
            - y(int): The y coordinate to move to
            - tween(Callable): The tween function to use
            - duration(float): The duration of the tween
            - x_offset(float): The x offset to add to the x coordinate
            - y_offset(float): The y offset to add to the y coordinate

        ### Returns:
            - None
        """
        # x_offset = int(x_offset) if x_offset is not None else 0
        # y_offset = int(y_offset) if y_offset is not None else 0
        #
        # if x is None and y is None and x_offset == 0 and y_offset == 0:
        #     return  # Special case for no mouse movement at all.
        #
        # _position = self.info.position()
        # start_x, start_y = _position.x, _position.y
        #
        # x = int(x) if x is not None else start_x
        # y = int(y) if y is not None else start_y
        #
        # x += x_offset
        # y += y_offset
        #
        # _size = self.info.size()
        #
        # width, height = _size.cx, _size.cy
        #
        # steps = [(x, y)]
        #
        # sleep_amount = MINIMUM_SLEEP
        #
        # if duration > MINIMUM_DURATION:
        #     num_steps = max(width, height)
        #     sleep_amount = duration / num_steps
        #
        #     if sleep_amount < MINIMUM_SLEEP:
        #         num_steps = int(duration / MINIMUM_SLEEP)
        #         sleep_amount = MINIMUM_SLEEP
        #
        #     steps = [
        #         getPointOnLine(start_x, start_y, x, y, tween(n / num_steps))
        #         for n in range(num_steps)
        #     ]
        #
        #     steps.append((x, y))
        #
        # for tween_x, tween_y in steps:
        #     if len(steps) > 1:
        #         time.sleep(sleep_amount)
        #
        #     tween_x = int(round(tween_x))
        #     tween_y = int(round(tween_y))
        #
        #     if (tween_x, tween_y) not in FAILSAFE_POINTS:
        #         fail_safe_check(instance=self.info)
        #
        #     fake_input(_display, X.MotionNotify, x=tween_x, y=tween_y)

        fake_input(_display, X.MotionNotify, x=x, y=y)
        _display.sync()

    def mouse_down(
        self, x: int, y: int, button: str | int, with_release: bool = False
    ) -> None:
        """
        - https://github.com/asweigart/pyautogui/blob/master/pyautogui/_pyautogui_x11.py#L105
        ### Arguments:
            - x: The x coordinate to move to
            - y: The y coordinate to move to
            - button: The button to press
            - with_release: Whether to release the button after pressing it
        ### Returns:
            - None
        """
        assert button in BUTTON_NAME_MAPPING.keys()

        self.moveto(x, y)
        fake_input(_display, X.ButtonPress, BUTTON_NAME_MAPPING[button])
        _display.sync()

        if with_release:
            self.mouse_up(x, y, button)

    def mouse_up(self, x: int, y: int, button: str | int) -> None:
        """
        - https://github.com/asweigart/pyautogui/blob/master/pyautogui/_pyautogui_x11.py#L113
        ### Arguments:
            - x: The x coordinate to move to
            - y: The y coordinate to move to
            - button: The button to press
        ### Returns:
             - None
        """
        assert button in BUTTON_NAME_MAPPING.keys()
        self.moveto(x, y)
        fake_input(_display, X.ButtonRelease, BUTTON_NAME_MAPPING[button])
        _display.sync()

    def click(self, x, y, button, clicks=None) -> None:
        assert button in BUTTON_NAME_MAPPING.keys()
        button = BUTTON_NAME_MAPPING[button]

        if clicks is None:
            self.mouse_down(x, y, button)
        else:
            for _ in range(clicks):
                self.mouse_down(x, y, button)

    def mouse_is_swapped(self):
        """
        TBD
        """
        pass

    def on_screen(self, x, y=None):
        """
        - https://github.com/asweigart/pyautogui/blob/master/pyautogui/__init__.py#L789
        Returns True if the given x and y coordinates are on the screen.
        """

        if y is None:
            x, y = x

        return 0 <= x <= self.info.size().cx and 0 <= y <= self.info.size().cy

        pass

    def scrool(self, clicks, x=None, y=None) -> None:
        """
        - https://github.com/asweigart/pyautogui/blob/master/pyautogui/_pyautogui_x11.py#L68
        . automatically calls vscrool or hscrool
        """
        return self.vscrool(clicks, x, y)

    def vscrool(self, clicks, x=None, y=None) -> None:
        """
        Performs a vertical scroll on windows
        ### Arguments:
             - clicks: The number of "clicks" to scroll, defaults to 1
                - x: The x coordinate to scroll, defaults to the current mouse x coordinate
                - y: The y coordinate to scroll, defaults to the current mouse y coordinate
        ### Returns:
            - None
        """

        clicks = int(clicks)
        if clicks == 0:
            return
        elif clicks > 0:
            button = 4  # scroll up
        else:
            button = 5  # scroll down

        for i in range(abs(clicks)):
            self.click(x, y, button)

    def hscrool(self, clicks, x=None, y=None) -> None:
        """
        Performs a horizontal scroll on windows
        ### Arguments:
            - clicks: The number of "clicks" to scroll, defaults to 1
            - x: The x coordinate to scroll, defaults to the current mouse x coordinate
            - y: The y coordinate to scroll, defaults to the current mouse y coordinate
        ### Returns:
             - None
        """
        clicks = int(clicks)
        if clicks == 0:
            return
        elif clicks > 0:
            button = 7  # scroll right
        else:
            button = 6  # scroll left

        for i in range(abs(clicks)):
            self.click(x, y, button=button)

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
    def position(self) -> Position:
        """
        Returns xy coordinates of the mouse cursor's current position.
        ### Returns:
           (x, y) tuple of the current xy coordinates of the mouse cursor.
        """

        # noinspection PyProtectedMember
        coord = _display.screen().root.query_pointer()._data
        return Position(coord["root_x"], coord["root_y"])

    # noinspection PyMethodMayBeStatic
    def size(self) -> SIZE:
        """
        Returns the size of the screen.
        ### Returns:
            (width, height) tuple of the size.
        """
        return SIZE(
            _display.screen().width_in_pixels, _display.screen().height_in_pixels
        )


class Display: # type: ignore[no-redef] 
    """
    Represents a basic display
    """

    def __init__(self):
        self.info = _Info()
        self._interact = _Interact(self.info)

    @slodonix_check(instance=_Info())
    def click(self, x, y, button, clicks: int) -> None:
        """
        Click at the specified coordinates
        left | middle | right
        """
        self._interact.click(x, y, button, clicks)

    @slodonix_check(instance=_Info())
    def key_press(self, keys, presses=1, interval=0.0) -> None:
        """
        Presses a key press down, followed by a release.
        ### Arguments:
            - key: The key to press
            - presses: The number of times to press the key
            - interval: The interval between each press
        ### Returns:
            None
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
        Performs a keyboard key press down, followed by a release.Performs a keyboard key press down,
        followed by a release,
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

            self._interact.key_down(char, with_release=True)
            time.sleep(interval)

    @slodonix_check(instance=_Info())
    def key_up(self, key, _pause=True) -> None:
        """
        Performs a keyboard key release.
        ### Arguments:
            - key: The key to release
        ### Returns:
            None
        """

        if len(key) > 1:
            key = key.lower()

        self._interact.key_up(key)

    @slodonix_check(instance=_Info())
    def key_down(self, key, with_release=True) -> None:
        """
        Performs a keyboard key press down, followed by a release.
        (without the release afterwards).
        ### Arguments:
            - key: The key to press
            - with_release: Whether to release the key

        ### Returns:
            - None
        """

        if len(key) > 1:
            key = key.lower()

        self._interact.key_down(key, with_release)

    @slodonix_check(instance=_Info())
    def move_to(
        self,
        x: X_TYPE = None,
        y: Y_TYPE = None,
        duration: DURATION_TYPE = 0.0,
        tween: TWEEN_TYPE = linear,
        _pause=True,
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
        self._interact.moveto(x, y, 0, 0, duration=duration, tween=tween)

    @slodonix_check(instance=_Info())
    def mouse_down(
        self, x=None, y=None, button=None, tween=linear, with_release=True
    ) -> None:
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
            -None
        """

        self._interact.moveto(x, y, x_offset=0, y_offset=0, tween=tween)
        self._interact.mouse_down(x, y, button, with_release=with_release)

    @slodonix_check(instance=_Info())
    def mouse_up(self, x=None, y=None, button=None, tween=linear) -> None:
        """
        Performs releasing a mouse button up (but not down beforehand).
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
           None
        """
        self._interact.moveto(x, y, x_offset=0, y_offset=0, tween=tween)
        self._interact.mouse_up(x, y, button)

    @slodonix_check(instance=_Info())
    def on_screen(self, x: int | Position, y: int | None = None) -> bool:
        """
         Returns True if the given x and y coordinates are on the screen.
        ### Arguments:
            - x (int, tuple, Position): The x position on the screen.
            - y (int, optional): The y position on the screen.
        ### Returns:
            - bool: True if the x and y coordinates are on the screen.
        ### Raises:
            - TypeError: If the given x or y coordinates are not integers.
        """
        if isinstance(x, Position):
            x, y = x.x, x.y # type: ignore[attr-defined]

        return self._interact.on_screen(x, y)

    @slodonix_check(instance=_Info())
    def move_rel(
        self, x_offset=None, y_offset=None, duration=0.0, tween=linear
    ) -> None:
        """
        Moves the mouse cursor to a point on the screen, relative to its current
        position.
        ### Arguments:
            - x_offset (int, optional): The x offset relative to the current mouse position.
            - y_offset (int, optional): The y offset relative to the current mouse position.
            - duration (float, optional): The number of seconds to perform the mouse move to the x,y coordinates.
                0, then the mouse cursor is moved
                instantaneously. 0.0 by default.
            - tween (func, optional): The tweening function used if the duration is not
                0. A linear tween is used by default.
        ### Returns:
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
    def drag_to(self, x=None, y=None, duration=0.0, tween=linear, button=None) -> None:
        """
        Performs a mouse drag (mouse movement while a button is held down) to a
        point on the screen.

        The x and y parameters detail where the mouse event happens. If None, the
        current mouse position is used. If a float value, it is rounded down. If
        outside the boundaries of the screen, the event happens at edge of the
        screen.
        ### Arguments:
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
        ### Returns:
             -None
        """
        self._interact.mouse_down(x=x, y=y, button=button, with_release=False)
        self._interact.moveto(
            x=x, y=y, x_offset=0, y_offset=0, duration=duration, tween=tween
        )
        self._interact.mouse_up(x=x, y=y, button=button)

    @slodonix_check(instance=_Info())
    def drag_rel(self, x=None, y=None, duration=0.0, tween=linear, button=None) -> None:
        """
        Performs a mouse drag (mouse movement while a button is held down) to a
        point on the screen(relative).

        The x and y parameters detail where the mouse event happens. If None, the
         current mouse position is used. If a float value, it is rounded down. If
         outside the boundaries of the screen, the event happens at edge of the
         screen.
        ### Arguments:
            x (int, float, None, tuple, optional): How far left (for negative values) or
                right (for positive values) to move the cursor. 0 by default. If tuple, this is used for x and y.
                If x is a str, it's considered a filename of an image to find on
                the screen with locateOnScreen() and click the center of.
            y (int, float, None, optional): How far up (for negative values) or
            tween (func, optional): The tweening function used if the duration is not
                0. A linear tween is used by default.
            button (str, int, optional): The mouse button released.

        ### Returns:
            -None
        """

        self._interact.mouse_down(x=x, y=y, button=button, with_release=False)
        self._interact.moveto(
            None, None, x, y, duration=duration, tween=tween
        )  # only pass in the offset
        self._interact.mouse_up(x=x, y=y, button=button)

    @slodonix_check(instance=_Info())
    def scroll(self, clicks, x=None, y=None) -> None:
        """
        Performs a scrool of the mouse scrool wheel

        Whether this is a vertical or horizontal scroll depends on the underlying
        operating system.

        The x and y parameters detail where the mouse event happens. If None, the
        current mouse position is used. If a float value, it is rounded down. If
        outside the boundaries of the screen, the event happens at edge of the
        screen.

        ### Arguments:
            - clicks (int): The number of scroll units.
            - x (int, float, None, optional): The x position on the screen.
            - y (int, float, None, optional): The y position on the screen.

        ### Returns:
            - None
        """

        if type(x) in (tuple, list):
            x, y = x[0], x[1]

        self._interact.scrool(clicks, x, y)

    @slodonix_check(instance=_Info())
    def hscrool(self, clicks, x=None, y=None) -> None:
        """
        Performs a scrool of the mouse scrool wheel(horizontal)

        Whether this is a vertical or horizontal scroll depends on the underlying
        operating system.

        The x and y parameters detail where the mouse event happens. If None, the
        current mouse position is used. If a float value, it is rounded down. If
        outside the boundaries of the screen, the event happens at edge of the
        screen.

        ### Arguments:
            - clicks (int): The number of scroll units.
            - x (int, float, None, optional): The x position on the screen.
            - y (int, float, None, optional): The y position on the screen.

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
             *args (str): The hotkey combination to press.
             **kwargs (dict): The hotkey combination to press.
        ### Returns
           - None
        """

        self._interact.hot_key(*args, **kwargs)


class DisplayContext(Display, ABC):
    def __init__(self):
        super().__init__()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_tb):
        pass


class DisplayAsParent(Display, ABC):
    """
    Use the display class as a parent for other classes.

    TBD
    """

    def __init__(self):
        super().__init__()
        self.listener = Listener(_Info())

    def _add_listeners(self):
        if hasattr(self, "trigger_mouse"):
            self.listener.add_listener("mouse", "trigger_mouse", self)

    @abstractmethod
    def body(self) -> None:
        """
        Every interaction here
        """

    def trigger_mouse(self, event):
        """
        Shows the mouse coordinates
        event: Position object
        """

    def run(self) -> None:
        """
        Run the main body of the program.
        Starts event listeners if any.
        """
        self._add_listeners()

        try:
            self.body()  # run the main body

            Listener.destroy_threads()  # destroy event listeners

        except Exception as e:
            Listener.destroy_threads()  # destroy event listeners
            raise e


def get_os() -> str:
    return "Linux-x(x11)"
