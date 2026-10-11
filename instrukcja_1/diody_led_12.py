from my_peri import LedPoint
from time import sleep

while True:
    for i in [0, 3, 1, 2, None]:
        LedPoint(i)
        sleep(0.5)