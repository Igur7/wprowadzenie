
from my_peri import LedPoint
from time import sleep

LedPoint(0)
sleep(1)
LedPoint(1)
sleep(1)
LedPoint(2)
sleep(1)
LedPoint(3)
sleep(1)
LedPoint(None)


i = 0

while i < 4:
    LedPoint(i)
    sleep(1)
    i += 1

LedPoint(None)


leds = [0, 1, 2, 3]

for i in leds:
    LedPoint(i)
    sleep(1)

LedPoint(None)

for i in [0, 1, 2, 3, None]:
    LedPoint(i)
    sleep(1)

