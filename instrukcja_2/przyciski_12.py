
from my_peri2 import ReadKeyboard
from time import sleep

but_previous = None

while True:
    but_current = ReadKeyboard()

    if but_current is not None and but_previous is None:
        print("but", but_current)

    but_previous = but_current
    sleep(0.1)
