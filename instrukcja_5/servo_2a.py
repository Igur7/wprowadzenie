from my_peri5 import LedPoint
from peripherals5 import ButRead
from time import sleep

# Punkt swietlny przesuwa sie do chwili wcisniecia przycisku 0 (GP9).
phase = 0
while True:
    LedPoint(phase)
    if ButRead(0):
        break
    sleep(0.1)
    phase = (phase - 1) % 4

# Ostatnia dioda pozostaje zapalona, tak jak zatrzymane uzwojenie.
print("Zatrzymano przyciskiem 0.")
