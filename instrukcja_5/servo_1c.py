from my_peri5 import LedPoint
from time import sleep

# Odejmowanie odwraca kierunek: 0, 3, 2, 1, 0, ...
phase = 0
while True:
    LedPoint(phase)
    sleep(0.1)
    phase = (phase - 1) % 4
