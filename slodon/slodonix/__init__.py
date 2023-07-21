import platform
import os
from slodon.slodonix.slodonix import tween
from typing import TYPE_CHECKING
# Configuration files
# WINDOWS_FOLDER = os.path.join(os.environ["APPDATA"], "slodon")
# LINUX_FOLDER = os.path.join(os.environ["HOME"], ".config", "slodon")
# OSX_FOLDER = os.path.join(os.environ["HOME"], "Library", "Application Support", "slodon")


def get_display_server():
    """
    Returns the display server
    """
    display_server = os.environ.get('WAYLAND_DISPLAY')
    if display_server:
        return "wayland"
    else:
        return "x"


_system = platform.system()  # Windows / Linux / Darwin
_display_manager = get_display_server


if _system == 'Windows':
    from slodon.slodonix.slodonix.slodonix_windows import *
elif _system == 'Linux':
    # search for x and wayland
    if _display_manager() == 'x':
        from slodon.slodonix.slodonix.slodonix_linux_x import *

    elif _display_manager() == 'wayland':
        from slodon.slodonix.slodonix.slodonix_linux_wayland import *


elif _system == "Darwin":
    from slodon.slodonix.slodonix.slodonix_osx import *

# after the actual code(for better user experience):
if TYPE_CHECKING:
    from slodon.slodonix.slodonix.slodonix_windows import *



