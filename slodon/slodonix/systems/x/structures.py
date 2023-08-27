from dataclasses import dataclass

__all__ = ["Position", "SIZE"]


@dataclass
class Position:
    x: int  # x coordinate, in pixels
    y: int  # y coordinate, in pixels

    def __str__(self):
        return f"Position(x={self.x}, y={self.y})"

    def __repr__(self):
        return str(self)


@dataclass
class SIZE:
    cx: int
    cy: int

    def __str__(self) -> str:
        return self.__repr__()

    def __repr__(self) -> str:
        return f"<Size: {self.cx}, {self.cy}>"
