import subprocess

# This project

__all__ = ["download_wayland", "download_wayland_to_path"]


def download_wayland() -> None:
    """
    Download wayland.

    ### Returns:
          None

    """
    command = ["git", "clone", "https://gitlab.freedesktop.org/wayland/wayland.git"]
    subprocess.run(command)


def download_wayland_to_path(path: str = None) -> None:
    """
    Download wayland in a specific folder.
    ### Arguments:
         path: str = None
    ### Returns:
          None

    """
    command = ["git", "clone", "https://gitlab.freedesktop.org/wayland/wayland.git"]
    subprocess.run(command, cwd=path)
