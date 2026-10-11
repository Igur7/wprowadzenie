from peripherals2 import ButRead
from my_peri2 import LedPoint
from time import sleep

while True:
    k0 = ButRead(0)
    k1 = ButRead(1)

    if not k1 and not k0:
        pos = 0
    elif not k1 and k0:
        pos = 1
    elif k1 and not k0:
        pos = 2
    else:
        pos = 3

    LedPoint(pos)
    sleep(0.05)

    if ButRead(3):
        LedPoint(None)

    sleep(0.05)
