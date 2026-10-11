
from my_peri2 import ReadKeyboard
from time import sleep
'''
counter = 0
but_previous = None

while True:
    but_current = ReadKeyboard()

    if but_current is not None and but_previous is None:
        counter += 1
        print("Licznik:", counter)

    but_previous = but_current
    sleep(0.1)

'''
'''
from my_peri2 import ReadKeyboard, LedBar
from time import sleep

counter = 0
but_previous = None

LedBar(counter)

while True:
    but_current = ReadKeyboard()

    if but_current is not None and but_previous is None:
        counter = (counter + 1) % 5
        LedBar(counter)

    but_previous = but_current
    sleep(0.1)
'''

from my_peri2 import ReadKeyboard, LedBar
from time import sleep

counter = 0
but_previous = None

LedBar(counter)

while True:
    but_current = ReadKeyboard()

    if but_current is not None and but_previous is None:
        if but_current == 0:
            counter -= 1
        elif but_current == 1:
            counter += 1

        if counter < 0:
            counter = 0
        elif counter > 4:
            counter = 4

        print(counter)
        LedBar(counter)

    but_previous = but_current
    sleep(0.1)
