
from peripherals import LedSet, LedClr
from time import sleep

while True:
    LedSet(0)
    sleep(0.01)
    LedClr(0)
    sleep(0.01)
#Czas pełnego cyklu wynosi około 20 ms, czyli około 50 Hz. Dioda świeci przez połowę okresu.