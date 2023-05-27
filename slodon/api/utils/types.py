from collections import UserDict
from typing import Union, Dict, Any, List, Type

__all__ = ["JSON"]

JSON = Union[Dict[str, Any], List[Any], int, str, float, bool, Type[None]]
