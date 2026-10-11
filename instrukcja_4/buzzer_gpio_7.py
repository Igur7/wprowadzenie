
from machine import Pin
from time import sleep_us

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

notes = [
    1319, 1175, 740, 831, 1109, 988, 587,
    659, 988, 880, 554, 659, 880
]

for f in notes:
    beep(f, 0.1)
    sleep_us(100_000)
