
from peripherals import LedSet, LedClr

def LedPoint(pos):
    for i in range(4):
        LedClr(i)

    if pos is not None:
        LedSet(pos)

def LedBar(led_nr):
    for i in range(4):
        if i < led_nr:
            LedSet(i)
        else:
            LedClr(i)
