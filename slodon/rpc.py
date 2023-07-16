# the CLI for slodon, mainly for developers.
import typer
# This project
from slodon.slodonix.systems.wayland.utils import *

app = typer.Typer()


@app.command()
def install_wayland():
    """
    Call the wayland installation script.
    """
    download_lib_wayland(app)


@app.command()
def remove(config_file: bool = True, wayland: bool = True):
    """
    Call the removal script.
    """
    _config_file = "config_file" if config_file else ""
    _wayland = "wayland" if config_file else ""
    _seperator = "&" if wayland and config_file else ""

    ask = typer.prompt(f"Are you sure you want to remove { _wayland } {_seperator} {_config_file}? [y/n]")

    if ask.lower() == "y":
        delete(config_file, wayland)
        raise typer.Exit()
    else:
        typer.echo("Aborted!")


if __name__ == "__main__":
    app()
