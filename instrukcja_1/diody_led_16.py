
from peripherals import LedSet, LedClr
from time import sleep

def LedDimm(pwm, duration):
    #0.020 bo częstoliwosc TWM wynosi 50 Hz, czyli okres wynosi 20 ms
    time_on = (pwm / 100) * 0.020
    time_off = 0.020 - time_on

    for i in range(round(50 * duration)):
        LedSet(0)
        sleep(time_on)
        LedClr(0)
        sleep(time_off)

while True:
    for pwm in [5, 10, 15, 20, 15, 10]:
        LedDimm(pwm, 0.5)
