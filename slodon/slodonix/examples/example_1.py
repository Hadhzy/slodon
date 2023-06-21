from slodon.slodonix import *


with DisplayContext() as display:
    print(display.info.position())
    display.interact.moveto(100, 100)


print(get_os())