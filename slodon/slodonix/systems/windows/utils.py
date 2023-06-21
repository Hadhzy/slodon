from dataclasses import dataclass

__all__ = ["Position"]


@dataclass
class Position:
    x: int  # x coordinate, in pixels
    y: int  # y coordinate, in pixels

    def __str__(self):
        return f"Position(x={self.x}, y={self.y})"

    def __repr__(self):
        return str(self)
