from my_peri import LedPoint
from time import sleep

while True:
    for i in [0, 1, 2, 3]:
        LedPoint(i)
        sleep(0.5)

    for i in [3, 2, 1, 0]:
        LedPoint(i)
        sleep(0.5)


i = 0
direction = 1

while True:
    LedPoint(i)
    sleep(0.5)

    if i == 0:
        direction = 1
    elif i == 3:
        direction = -1

    i += direction
