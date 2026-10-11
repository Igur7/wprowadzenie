
from peripherals2 import ButRead
from time import sleep

while True:
    print(ButRead(3), ButRead(2), ButRead(1), ButRead(0))
    sleep(0.2)
