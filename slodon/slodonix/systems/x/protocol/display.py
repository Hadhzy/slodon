import uuid

# This project
from .connect import Connection


class BaseDisplay:
    """Base class for all displays."""

    class Meta:
        """Meta-information for all displays"""

        def __init__(self, **kwargs):
            self.data = kwargs

        def __str__(self):
            return str(self.data)

    def __init__(self, display=None) -> None:
        """
        DISPLAY initialization

        ### Arguments
        - display (str): the full display name(string) -> protocol/hostname:number.screen_number
        ### Returns
        - None
        """
        self.display_name = display  # the display name
        self.default_screen = "TBD"
        self.id = uuid.uuid4()  # obtain custom id
        # Connection here

        self.connection = Connection(display)  # create the connection

        self.meta = self.Meta(
            display_name=self.display_name,
            default_screen=self.default_screen,
            connection=self.connection,
        )

    def close(self):
        """Close the display"""
        self.connection.close()
