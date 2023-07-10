from slodon.slodonix import *

# with display context manager

with DisplayContext() as display:
    display.key_down("h")  # release key automatically
    display.key_down("h")
    display.move_to(100, 200)

