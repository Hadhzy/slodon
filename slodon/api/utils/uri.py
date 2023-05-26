import uuid


class _UriBase:
    """Represent the URI"""
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


class Watcher:
    """Serve the websocket connection by sending a response to the client"""


class URI(_UriBase):
    pass
