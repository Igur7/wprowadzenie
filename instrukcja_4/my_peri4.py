
from peripherals4 import LedSet, LedClr, ButRead
from machine import Pin
from time import sleep_us

def LedPoint(pos):
    for i in range(4):
        LedClr(i)

    if pos is not None:
        LedSet(pos)


def LedBar(led_nr):
    for i in range(4):
        if i < led_nr:
            LedSet(i)
        else:
            LedClr(i)


def ReadKeyboard():
    for i in range(4):
        if ButRead(i):
            return i
    return None


buzzer_a = Pin(10, Pin.OUT)
buzzer_b = Pin(11, Pin.OUT)

buzzer_a.value(0)
buzzer_b.value(1)


def beep(f_Hz, t_s):
    T_us = 1_000_000 / f_Hz

    for i in range(round(2 * t_s * f_Hz)):
        buzzer_a.toggle()
        buzzer_b.toggle()
        sleep_us(int(T_us / 2))
