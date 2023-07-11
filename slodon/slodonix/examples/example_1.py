from slodon.slodonix import *
# with display context manager

with DisplayContext() as display:
    display.key_down("h")  # release key automatically
    display.key_down("h")
    display.move_to(0, 200, tween=tween.easeInOutQuad, duration=2)

