from collections import UserDict
from typing import Union, Dict, Any, List, Type, TypedDict

__all__ = ["JSON", "Response"]

JSON = Union[Dict[str, Any], List[Any], int, str, float, bool, Type[None]]


class Response(TypedDict):
    """
    Represent a Slodon server response
    """

    status: int
    message: str
    content: JSON
