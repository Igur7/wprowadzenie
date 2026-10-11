from my_peri5 import LedPoint
from time import sleep

# Jedno wywolanie LedPoint; modulo 4 zawija numer LED-a z 3 na 0.
phase = 0
while True:
    LedPoint(phase)
    sleep(0.1)
    phase = (phase + 1) % 4
