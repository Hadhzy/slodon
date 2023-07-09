from slodon.slodonix import *

# with display context manager

with DisplayContext() as display:
    display.interact.key_down("h")
    display.interact.key_down("h")

# without display context manager
display = Display()
display.interact.key_down("h")
display.interact.key_down("h")

# with key_release

with DisplayContext() as display:
    display.interact.key_down("h", with_release=True)
    display.interact.key_down("h")

# get current os
print(get_os())
