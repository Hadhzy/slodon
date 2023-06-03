
class _BaseDisplay:
    """Base class for all displays."""

    def __init__(self, display=None) -> None:

        self.display_name = display.name
        self.default_screen = "TBD"

        # Connection here

