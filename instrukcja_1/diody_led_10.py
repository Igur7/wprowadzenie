from my_peri import LedPoint
from time import sleep

for i in [0, 1, 2, 3]:
    LedPoint(i)
    sleep(1)

for i in [3, 2, 1, 0]:
    LedPoint(i)
    sleep(1)

LedPoint(None)


i = 0

while i < 8:
    if i < 4:
        j = i
    else:
        j = 7 - i

    LedPoint(j)
    sleep(0.5)
    i += 1

LedPoint(None)