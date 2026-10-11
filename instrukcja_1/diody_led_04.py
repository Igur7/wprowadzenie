
from peripherals import LedSet, LedClr
from time import sleep

i = 0

while i < 3:
    LedSet(2)
    sleep(1)
    LedClr(2)
    sleep(1)
    i += 1

print("Done")
