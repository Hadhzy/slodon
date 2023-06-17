#: https://tronche.com/gui/x/xlib/event-handling/protocol-errors/default-handlers.html
from typing import TYPE_CHECKING

# this project
if TYPE_CHECKING:
    from slodon.slodonix.systems.x.display.display import Display


class XError(Exception):
    """Main error class for x errors"""
    def __init__(self, error_type: int, display: Display, serial: int, error_code: str, request_code,
                 minor_code: str, resource_id: int) -> None:
        """
        XError initialization
        ### Arguments
        - error_type (int): the error type
        - display (Display): the display
        - serial (int): the serial number
        - error_code (str): the error code
        - request_code (int): the request code
        - minor_code (str): the minor code
        - resource_id (int): the resource id
        ### Returns
        - None
        """

        self.error_type = error_type
        self.display = display
        self.serial = serial
        self.error_code = error_code
        self.request_code = request_code
        self.minor_code = minor_code
        self.resource_id = resource_id


class BadAccess(XError):
    """
    - A client attempts to grab a key/button combination already grabbed by another client.
    - A client attempts to free a colormap entry that it had not already allocated.
    - A client attempts to store into a read-only or unallocated colormap entry.
    - A client attempts to modify the access control list from other than the local (or otherwise authorized) host.
    """


class BadAlloc(XError):
    """
    The server fails to allocate the requested resource.
    """


class BadAtom(XError):
    """
    A value for an atom argument does not name a defined atom.
    """


class BadColor(XError):
    """
    A value for a colormap argument does not name a defined colormap.
    """


class BadCursor(XError):
    """
    A value for a cursor argument does not name a defined cursor.
    """


class BadDrawable(XError):
    """
    A value for a drawable argument does not name a defined window or pixmap.
    """


class BadFont(XError):
    """
    A value for a font argument does not name a defined font (or, in some cases, GContext).
    """


class BadGC(XError):
    """
    A value for a GContext argument does not name a defined GContext .
    """


class BadIDChoice(XError):
    """
    The value chosen for a resource identifier either is not included.
    """


class BadImplementation(XError):
    """
    The server does not implement some aspect of the request.
    """


class BadLength(XError):
    """
    The length of a request is shorter or longer than that required to contain the arguments.
    """


class BadMatch(XError):
    """
    In a graphics request, the root and depth of the graphics context does not match that of the drawable.
    """


class BadName(XError):
    """
    A font or color of the specified name does not exist.
    """


class BadPixmap(XError):
    """
    A value for a pixmap argument does not name a defined pixmap.
    """


class BadRequest(XError):
    """
    The major or minor opcode does not specify a valid request. This usually is an Xlib or server error.
    """


class BadValue(XError):
    """
    Some numeric value falls outside of the range of values accepted by the request.
    """


class BadWindow(XError):
    """
    A value for a window argument does not name a defined window
    """

