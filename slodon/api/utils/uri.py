import uuid
import json as _json
__all__ = ["URI"]


class _UriBase:
    """Represent the URI"""
    __slots__ = ["id", "uri"]

    def __init__(self, uri):
        self.id = uuid.uuid4()
        self.uri = uri

    def __repr__(self) -> str:
        """
        Returns the representation of the object(string)
        :return: str
        """
        return f"<{self.__class__.__name__} id={self.id} uri={self.uri}>"

    def __str__(self) -> str:
        """
        Returns the string representation of the object
        :return: str
        """
        return self.__repr__()

    def __eq__(self, other) -> bool:
        """Compare them by their uri"""
        return self.uri == other.uri


class URI(_UriBase):
    pass
