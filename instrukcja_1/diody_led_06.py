
from peripherals import LedSet, LedClr
from time import sleep

LedSet(1)

while True:
    LedSet(2)
    sleep(0.002)
    LedClr(2)
    sleep(0.018)
 