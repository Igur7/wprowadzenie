from my_peri5 import LedPoint, DetRead
from time import sleep

# DetRead z biblioteki zastepuje bezposredni odczyt detektora.
# Zwraca 0 po wcisnieciu przycisku 1 (GP8).
print("Kalibracja: wcisnij przycisk 1, aby wskazac pozycje zerowa.")
phase = 0
while True:
    LedPoint(phase)
    if DetRead() == 0:
        break
    sleep(0.1)
    phase = (phase + 1) % 4

print("Znaleziono pozycje zerowa. Swieci LED", phase)
