from my_peri5 import LedPoint, DetRead
from peripherals5 import PotRead
from time import sleep

TRYB = "potencjometr"

if TRYB not in ("potencjometr", "pozycje"):
    raise ValueError("TRYB musi byc: potencjometr albo pozycje")

MAX_POS = 48
POT_MAX = 65535
STEP_DELAY = 0.01

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
des_pos = 0

positions = (36, 12, 24)
target_index = 0

pot_filtered = PotRead()

print("Pozycja zerowa ustalona. Tryb:", TRYB)

while True:
    if TRYB == "potencjometr":
        pot_raw = max(0, min(POT_MAX, PotRead()))

        pot_filtered = (3 * pot_filtered + pot_raw) // 4

        new_des_pos = MAX_POS - (
            (pot_filtered * MAX_POS + POT_MAX // 2) // POT_MAX
        )
        if (
            abs(new_des_pos - des_pos) >= 2
            or new_des_pos == 0
            or new_des_pos == MAX_POS
        ):
            des_pos = new_des_pos

    else:
        des_pos = positions[target_index]

    previous_pos = curr_pos

    if curr_pos < des_pos:
        curr_pos += 1
    elif curr_pos > des_pos:
        curr_pos -= 1

    LedPoint((zero_phase + curr_pos) % 4)
    sleep(STEP_DELAY)

    if curr_pos != previous_pos and curr_pos == des_pos:
        print(
            "Pozycja:", curr_pos,
            "krokow; kat:", curr_pos * 7.5,
            "stopni"
        )

    if TRYB == "pozycje" and curr_pos == des_pos:
        print("Osiagnieto pozycje", curr_pos)
        sleep(1)

        target_index += 1

        if target_index == len(positions):
            break