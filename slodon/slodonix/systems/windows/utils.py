from dataclasses import dataclass

__all__ = ["Position", "is_shift_character"]


@dataclass
class Position:
    x: int  # x coordinate, in pixels
    y: int  # y coordinate, in pixels

    def __str__(self):
        return f"Position(x={self.x}, y={self.y})"

    def __repr__(self):
        return str(self)


def is_shift_character(character: str) -> bool:
    """
    source: https://github.com/asweigart/pyautogui/blob/master/pyautogui/__init__.py#L526-L532
    """
    # NOTE TODO - This will be different for non-qwerty keyboards.
    return character.isupper() or character in set('~!@#$%^&*()_+{}|:"<>?')
