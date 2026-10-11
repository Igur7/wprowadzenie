 
from peripherals2 import ButRead
from my_peri2 import LedBar

#while True:
    #count = ButRead(0) + ButRead(1) + ButRead(2) + ButRead(3)
    #LedBar(count)


while True:
    count = 0

    for i in range(4):
        count += ButRead(i)

    LedBar(count)
