# https://gitlab.freedesktop.org/xorg/lib/libx11/-/blob/master/include/X11/Xresource.h
import uuid


class XResource:
    # Represent a resource in the x window system.
    def __init__(self):
        self.id = uuid.uuid4()  # int

    def __str__(self) -> str:
        return self.__repr__()

    def __repr__(self) -> str:
        return f"<XResource id={self.id}>"

    def __dispose(self) -> uuid.UUID:
        """
        Serve as the resource.
        """
        return self.id
