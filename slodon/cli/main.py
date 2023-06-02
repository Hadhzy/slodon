"""Entry point of the project"""
from textual.app import App, ComposeResult, RenderableType
from textual.binding import Binding
from textual.widgets import Footer
from textual.widgets import Static, Label


class _Sync(Static):
    """
    This class is used to synchronize the user, if it is needed.
    """
    def render(self) -> RenderableType:
        return "Syncing..."


class _Task:
    """Used to handle the generated tasks by the user"""


class SlodonCLI(App):
    """The CLI application"""
    BINDINGS = [
        Binding("q", "quit", "Quit")
    ]

    def compose(self) -> ComposeResult:
        yield _Sync()
        yield Footer()


def start_cli():
    SlodonCLI().run()


if __name__ == "__main__":
    start_cli()

