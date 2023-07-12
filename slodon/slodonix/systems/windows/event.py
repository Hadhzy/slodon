import dataclasses
import threading
from ctypes import windll as w
from ctypes import Structure
from uuid import uuid4

# This project
from slodon.log import slodon_logger


class SLODODIXThread(threading.Thread):
    """

    """

    def __init__(self, code, structure):

        self.code = code
        self.structure = structure
        self.id = uuid4()  # unique id
        super().__init__()

        self._running = False

    def run(self):
        w.MouseProc(0, )

    def __str__(self) -> str:
        return self.__repr__()

    def __repr__(self) -> str:
        return f"code:{self.code}, structure:{self.structure}, id:{self.id}"


class Listener:

    THREADS: list[threading.Thread] = []  # all threads

    """
    https://learn.microsoft.com/en-us/windows/win32/winmsg/hooks
    """

    def __init__(self) -> None:
        super().__init__()
        self.wait()

    def add_listener(self, code: int, structure: Structure) -> None:
        thread = SLODODIXThread(code, structure)
        thread.start()

        self.THREADS.append(thread)

    def wait(self) -> None:
        for thread in self.THREADS:
            thread.join()

    def __str__(self) -> str:
        return self.__repr__()

    def __repr__(self) -> str:
        return "<Listener: {}>".format(self.THREADS)


@dataclasses.dataclass
class Event:
    """

    """
    type: str
    time: float
