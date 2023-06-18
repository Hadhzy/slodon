# https://tronche.com/gui/x/xlib/events/
from dataclasses import dataclass
from typing import TYPE_CHECKING
# This project
if TYPE_CHECKING:
    from slodon.slodonix.systems.x.display.display import Display
    from slodon.slodonix.systems.x.xobjects.window import XWindow


@dataclass
class _EventType:
    """
    Represents an X event:
    https://tronche.com/gui/x/xlib/events/structures.html
    """

    type: int  # The type of event
    serial: int  # last request processed by serve
    send_event: bool
    display: Display
    window: XWindow


class _XEvent:
    pass
