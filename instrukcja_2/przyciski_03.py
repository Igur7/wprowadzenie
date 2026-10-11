from peripherals2 import ButRead
from my_peri2 import LedPoint

while True:
    k0 = ButRead(0)
    k1 = ButRead(1)
    k2 = ButRead(2)
    k3 = ButRead(3)

    if k0 and k3 and not k1 and not k2:
        LedPoint(0)
    elif k1 and k2 and not k0 and not k3:
        LedPoint(1)
    else:
        LedPoint(None)
