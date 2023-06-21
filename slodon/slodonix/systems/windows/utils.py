from dataclasses import dataclass

__all__ = ["Position"]


@dataclass
class Position:
    x: int  # x coordinate, in pixels
    y: int  # y coordinate, in pixels

