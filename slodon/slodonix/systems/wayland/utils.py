from pathlib import Path
import warnings
import json
import urllib.request
# This project

from slodon.slodonix.systems.wayland.constants import *

__all__ = ["create_config", "download_lib_wayland", "remove"]

SCHEME = {
    "path_to_download_from":  WAYLAND_SITE,
    "path_to_download_to": DOWNLOAD_TO,
    "current_path": CURRENT_PATHS,
}


def create_config(manual: bool = False) -> None:
    """
    Create basic configuration file for the wayland library.
    ### Arguments:
          - manual (bool): If True, the user will be asked to enter the details manually.
    ### Returns:
        - None
    """

    _path = Path("wayland.json")

    if not _path.exists():

        with open("wayland.json", "w") as file:
            file.write("" if manual else json.dumps(SCHEME, indent=4))  # write json

    else:
        warnings.warn(f"Configuration file already exists: ->{_path.absolute()}", UserWarning)


def remove(_config: bool = False, _wayland: bool = False) -> None:
    """
    Remove the configuration file or the wayland library or both.

    ### Arguments:
        - _config (bool): If True, the configuration file will be removed.
        - _wayland (bool): If True, the wayland library will be removed.

    ### Returns:
        - None
    """

    _json = json.loads(Path("wayland.json").read_text())
    try:

        # delete wayland FIRST
        if _wayland:
            _file_path = _json["current_path"]
            Path(_file_path).rmdir()

        if _config:
            Path("wayland.json").unlink()  # remove the file

    except Exception as e:
        raise Exception(f"Error while removing the wayland library | wayland.json: {e}")


def download_lib_wayland() -> None:
    """
    Download the wayland library.
    """
    try:
        url = URL
        download_to = Path(DOWNLOAD_TO).expanduser().absolute()

        urllib.request.urlretrieve(url, download_to)

    except Exception as e:
        raise Exception(f"Error while downloading the wayland library: {e}",
                        "url:", URL, "download_to: ", DOWNLOAD_TO)
