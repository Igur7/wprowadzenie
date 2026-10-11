
from my_peri import LedPoint
from time import sleep

i = 0

while i < 4:
    LedPoint(i)
    i += 1
    sleep(1)

LedPoint(None)
