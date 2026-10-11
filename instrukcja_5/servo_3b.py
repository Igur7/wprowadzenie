from my_peri5 import LedPoint, DetRead
from peripherals5 import PotRead
from time import sleep

TRYB = "potencjometr"

if TRYB not in ("potencjometr", "pozycje"):
    raise ValueError("TRYB musi byc: potencjometr albo pozycje")

print("Kalibracja: wcisnij przycisk 1, aby wskazac pozycje zerowa.")
phase = 0
while True:
    LedPoint(phase)
    if DetRead() == 0:
        break
    sleep(0.1)
    phase = (phase - 1) % 4

zero_phase = phase
curr_pos = 0
positions = (36, 12, 24)
target_index = 0
print("Pozycja zerowa ustalona. Tryb:", TRYB)

while True:
    if TRYB == "potencjometr":
        des_pos = 48 - (PotRead() * 48 // 65535)
    else:
        des_pos = positions[target_index]

    previous_pos = curr_pos
    if des_pos > curr_pos:
        curr_pos += 1
    elif des_pos < curr_pos:
        curr_pos -= 1

    LedPoint((zero_phase + curr_pos) % 4)
    if curr_pos != previous_pos:
        print("Pozycja:", curr_pos, "krokow; kat:", curr_pos * 7.5,
              "stopni; cel:", des_pos)
    sleep(0.1)

    if TRYB == "pozycje" and curr_pos == des_pos:
        print("Osiagnieto pozycje", curr_pos)
        sleep(1)
        target_index += 1
        if target_index == len(positions):
            break
