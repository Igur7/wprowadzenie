
from my_peri2 import LedPoint, ReadKeyboard

while True:
    but = ReadKeyboard()

    if but is not None:
        LedPoint(but)
