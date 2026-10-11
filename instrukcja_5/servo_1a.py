from my_peri5 import LedPoint
from time import sleep

# LED-y zastepuja uzwojenia silnika: kolejno swieci 0, 1, 2, 3.
# Jeden krok co 0.1 s oznacza czestotliwosc 10 Hz.
while True:
    LedPoint(0)
    sleep(0.1)
    LedPoint(1)
    sleep(0.1)
    LedPoint(2)
    sleep(0.1)
    LedPoint(3)
    sleep(0.1)
