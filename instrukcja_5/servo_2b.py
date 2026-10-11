from my_peri5 import LedPoint
from peripherals5 import ButRead
from time import sleep

# Kalibracja bez prawdziwego detektora: wcisnij przycisk 1 (GP8),
# aby oznaczyc aktualna pozycje jako zero i zatrzymac ruch.
print("Kalibracja: wcisnij przycisk 1, aby wskazac pozycje zerowa.")
phase = 0
while True:
    LedPoint(phase)
    if ButRead(1):
        break
    sleep(0.1)
    phase = (phase + 1) % 4

print("Znaleziono pozycje zerowa. Swieci LED", phase)
