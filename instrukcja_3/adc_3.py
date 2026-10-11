
from peripherals3 import PotRead
from time import sleep

while True:
    adc = PotRead()
    pot_norm = (adc - 352) / (65535 - 352)
    print(pot_norm * 3.3)
    sleep(0.5)
