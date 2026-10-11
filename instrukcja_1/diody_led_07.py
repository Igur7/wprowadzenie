
from peripherals import LedSet, LedClr
from time import sleep

def LedPoint(pos):
    for i in range(4):
        LedClr(i)

    if pos is not None:
        LedSet(pos)

i = 0

while i < 4:
    LedPoint(i)
    i += 1
    sleep(1)

LedPoint(None)
