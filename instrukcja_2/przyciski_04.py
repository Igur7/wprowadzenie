
from peripherals2 import ButRead
from my_peri2 import LedPoint

while True:
    k0 = ButRead(0)
    k1 = ButRead(1)

    if not k1 and not k0:
        LedPoint(0)
    elif not k1 and k0:
        LedPoint(1)
    elif k1 and not k0:
        LedPoint(2)
    else:
        LedPoint(3)
