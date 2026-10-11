
from peripherals3 import PotRead
from my_peri3 import LedPoint

while True:
    adc = PotRead()
    pot_norm = (adc - 352) / (65535 - 352)

    # Ograniczenie wartości do zakresu 0-1
    pot_norm = max(0, min(1, pot_norm))

    led_pos = 3 - int(pot_norm * 3)

    LedPoint(led_pos)
