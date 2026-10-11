
from peripherals2 import ButRead
from my_peri2 import LedPoint

while True:
    if ButRead(0):
        LedPoint(0)
    else:
        LedPoint(None)
