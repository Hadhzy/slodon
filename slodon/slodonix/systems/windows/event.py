import dataclasses
import threading

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from slodon.slodonix.slodonix.slodonix_windows import _Info
    from slodon.slodonix.slodonix.slodonix_windows import DisplayAsParent


class Listener:

    """
    https://learn.microsoft.com/en-us/windows/win32/winmsg/hooks
    """

    def __init__(self, _instance: "_Info") -> None:
        super().__init__()
        self.info = _instance  # _Info() instance

    def add_listener(self, _type: str, method: callable, obj: "DisplayAsParent") -> None:

        """
        Start a thread to listen for a specific event type.
        ### Arguments:
              - _type (str): The type of event to listen for.
              - method (callable): The method to call when the event is triggered.
              - obj: The object to call the method on.
        ### Returns:
           None
        """

        match _type:
            case "mouse":  # In case of mouse event
                movement_thread = threading.Thread(target=self._detect_mouse(method, obj))  # create a thread
                movement_thread.start()  # start the thread
            case "key_pressed":
                pass

    def _detect_mouse(self, method: callable, obj):
        prev_pos = self.info.position()
        while True:
            curr_pos = self.info.position()
            if prev_pos != curr_pos:
                _method = getattr(obj, method)  # get the method based on the name
                _method(curr_pos)  # position has been changed call with the new one
            prev_pos = curr_pos


@dataclasses.dataclass
class Event:
    """

    """
    type: str
    time: float
