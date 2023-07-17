# the CLI for slodon, mainly for developers.
import typer

# This project
from slodon.slodonix.systems.wayland.utils import *

app = typer.Typer()


@app.command()
def get_wayland() -> None:
    """
    Download wayland in the current dictionary.
    ### Returns:
       None

    """
    download_wayland()


@app.command()
def get_wayland_to(path: str) -> None:
    """
    Download wayland in a specific folder.
    ### Returns:
       None

    """
    download_wayland_to_path(path)


def start_cli() -> None:
    """
    Run the CLI.
    ### Returns:
       None
    """
    app()


if __name__ == "__main__":
    start_cli()
