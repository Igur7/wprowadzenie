
from peripherals import LedSet, LedClr
from time import sleep

LedSet(1)

while True:
    LedSet(0)
    sleep(0.001)
    LedClr(0)
    sleep(0.019)
#Dioda LED0 świeci 1 ms, a przez 19 ms jest zgaszona. Wypełnienie wynosi 5%.