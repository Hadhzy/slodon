import platform

_system = platform.system()  # Windows / Linux / Darwin

if _system == 'Windows':
    from slodon.slodonix.slodonix.slodonix_windows import *

elif _system == 'Linux':
    # search for x and wayland
    pass

elif _system == "Darwin":
    from slodon.slodonix.slodonix.slodonix_osx import *

