from my_peri import LedBar
from time import sleep

while True:
    for i in [0, 1, 2, 3, 4]:
        LedBar(i)
        sleep(0.5)
