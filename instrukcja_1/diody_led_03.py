from peripherals import LedSet, LedClr
from time import sleep

for i in range(4):
    LedSet(i)
    sleep(1)

for i in range(3, -1, -1):
    LedClr(i)
    sleep(1)

print("Done")
