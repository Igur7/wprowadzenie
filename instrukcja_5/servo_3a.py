from my_peri5 import LedPoint, DetRead
from time import sleep

# Kalibracja: ruch w kierunku 0, 3, 2, 1.
# Przycisk 1 zastepuje marker nad detektorem.
print("Kalibracja: wcisnij przycisk 1, aby wskazac pozycje zerowa.")
phase = 0
while True:
    LedPoint(phase)
    if DetRead() == 0:
        break
    sleep(0.1)
    phase = (phase - 1) % 4

# Zapamietujemy faze w chwili kalibracji, aby nie przeskoczyc diody.
zero_phase = phase

# Pozycjonowanie: 12 krokow w kierunku przeciwnym do kalibracji.
# Wedlug PDF 48 krokow = 360 stopni, czyli 12 krokow = 90 stopni.
curr_pos = 0
while curr_pos < 12:
    curr_pos += 1
    LedPoint((zero_phase + curr_pos) % 4)
    print("Pozycja:", curr_pos, "krokow; kat:", curr_pos * 7.5)
    sleep(0.1)

print("Osiagnieto 12 krokow, czyli 90 stopni.")
