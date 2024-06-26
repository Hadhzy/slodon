import dataclasses
import threading

from typing import List


class SlodonixThread(threading.Thread):
    """
    Represents a single thread in the system.
    """

    def __init__(self):
        super().__init__()
        self.listen_to = None
        # control the execution of the thread.
        self.stop_event = threading.Event()

    def run(self):
        """
        trigger when "thread.start()" is called.
        """
        while not self.stop_event.is_set():  # while the thread is not stopped
            self.listen_to()


class DetectMouse(SlodonixThread):
    """
    Thread to detect mouse movement.
    """

    def __init__(self, obj, method, info):
        super().__init__()
        self.obj = obj
        self.method = method
        self.listen_to = self.detect_mouse
        self.info = info

    def detect_mouse(self):
        prev_pos = self.info.position()
        while not self.stop_event.is_set():
            curr_pos = self.info.position()
            if prev_pos != curr_pos:
                _method = getattr(
                    self.obj, self.method
                )  # get the method based on the name
                # position has been changed call with the new one
                _method(curr_pos)
            prev_pos = curr_pos


class Listener:
    """
    Listen to different events.
    Handling threads.
    """

    THREADS: List[threading.Thread] = []

    def __init__(self, _instance) -> None:
        super().__init__()
        self.info = _instance  # _Info() instance

    def add_listener(self, _type: str, method: str, obj) -> None:
        """
        Start a thread to listen for a specific event type.
        ### Arguments:
              - _type (str): The type of event to listen for.
              - method (str): The method to call when the event is triggered.
              - obj: The object to call the method on(DisplayAsParent).
        ### Returns:
           None
        """

        match _type:
            case "mouse":  # In case of mouse event
                movement_thread = DetectMouse(obj, method, self.info)  # create a thread
                movement_thread.start()  # start the thread
                # add the thread to the list
                self.THREADS.append(movement_thread)
            case "key_pressed":
                pass

    @classmethod
    def destroy_threads(cls):
        """
        Destroy all threads.
        """
        for thread in cls.THREADS:
            thread.stop_event.set()
            thread.join()


@dataclasses.dataclass
class Event:
    """ """

    type: str
    time: float
