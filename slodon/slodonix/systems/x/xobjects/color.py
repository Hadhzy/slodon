# https://tronche.com/gui/x/xlib/color/structures.html


class _XColor:
    """
    Represents a color.
    """

    def __init__(self, pixel: int, red: int, green: int, blue: int, flags, pad) -> None:
        """
        :param pixel: The pixel value of the color.
        :param red: The red value of the color.
        :param green: The green value of the color.
        :param blue: The blue value of the color.
        """
        self.pixel = pixel
        self.red = red
        self.green = green
        self.blue = blue
        self.flags = flags
        self.pad = pad

    def __str__(self):
        return self.__repr__()

    def __repr__(self):
        return f"<XColor pixel={self.pixel}, red={self.red}, green={self.green}, blue={self.blue}"


# Todo: Color strings? https://tronche.com/gui/x/xlib/color/strings/
